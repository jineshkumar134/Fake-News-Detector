from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
import logging
from datetime import datetime

from fact_check import check_claims_google, extract_claims
from image_analysis import reverse_image_search, extract_image_metadata
from domain_check import check_domain_reputation
from headline_corroboration import corroborate_headline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fake News Detector", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisResult(BaseModel):
    headline: str
    source_url: str
    text_analysis: dict
    domain_analysis: dict
    headline_corroboration: dict
    image_analysis: Optional[dict] = None
    overall_credibility_score: float
    risk_level: str
    flags: List[str]
    timestamp: str

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_article(
    headline: str = Form(...),
    content: str = Form(default=""),
    source_url: str = Form(...),
    author: str = Form(default=""),
    image: Optional[UploadFile] = File(None)
):
    """Comprehensive multi-modal analysis of article."""
    try:
        headline = headline.strip()
        source_url = source_url.strip()
        content = content.strip()
        author = author.strip()
        
        if not headline:
            raise HTTPException(status_code=400, detail="Headline is required")
        if not source_url:
            raise HTTPException(status_code=400, detail="Source URL is required")
        
        flags = []
        scores = []
        
        # 1. Text analysis
        logger.info(f"Analyzing headline: {headline}")
        claims = extract_claims(headline)
        text_analysis = await check_claims_google(headline, claims)
        
        if text_analysis.get("verification_matches", 0) == 0:
            flags.append("No fact-checks found for this claim")
            text_score = 0.5
        elif text_analysis.get("false_count", 0) > 0:
            false_count = text_analysis.get("false_count", 0)
            total = text_analysis.get("verification_matches", 1)
            false_ratio = false_count / total
            flags.append(f"{false_count} out of {total} claims flagged as false")
            text_score = 0.2 if false_ratio > 0.5 else 0.4
        elif text_analysis.get("verified_count", 0) > 0:
            verified = text_analysis.get("verified_count", 0)
            total = text_analysis.get("verification_matches", 1)
            verified_ratio = verified / total
            flags.append(f"{verified} out of {total} claims verified as true")
            text_score = 0.85 if verified_ratio > 0.7 else 0.7
        else:
            flags.append("Claims marked as mixed or partially true")
            text_score = 0.5
        
        scores.append(text_score)
        
        # 2. Domain analysis
        logger.info(f"Checking domain: {source_url}")
        domain_analysis = await check_domain_reputation(source_url)
        
        domain_score = 0.5
        if domain_analysis.get("is_suspicious_domain"):
            flags.append("Domain flagged as suspicious or very new")
            domain_score = 0.2
        elif domain_analysis.get("is_satirical"):
            flags.append("Domain known for satirical/parody content")
            domain_score = 0.1
        else:
            if domain_analysis.get("domain_age_days", 0) > 365:
                domain_score = 0.85
                flags.append("Domain is well-established")
            elif domain_analysis.get("domain_age_days", 0) > 180:
                domain_score = 0.7
            else:
                domain_score = 0.5
        
        if domain_analysis.get("is_https"):
            flags.append("Uses HTTPS (secure connection)")
        
        scores.append(domain_score)
        
        # 3. Headline corroboration
        logger.info(f"Checking headline corroboration")
        headline_corroboration = await corroborate_headline(headline)
        
        corroborating_sources = headline_corroboration.get("corroborating_sources", 0)
        
        if corroborating_sources >= 5:
            flags.append(f"Widely reported by {corroborating_sources} sources")
            corroboration_score = 0.9
        elif corroborating_sources >= 3:
            flags.append(f"Reported by {corroborating_sources} credible sources")
            corroboration_score = 0.8
        elif corroborating_sources >= 1:
            flags.append(f"Found {corroborating_sources} corroborating source(s)")
            corroboration_score = 0.6
        else:
            flags.append("No corroborating sources found - claim may be unique or unverified")
            corroboration_score = 0.3
        
        scores.append(corroboration_score)
        
        # 4. Image analysis
        image_analysis = None
        if image:
            try:
                logger.info("Analyzing provided image")
                image_path = f"/tmp/{image.filename}"
                with open(image_path, "wb") as f:
                    f.write(await image.read())
                
                metadata = extract_image_metadata(image_path)
                reverse_results = reverse_image_search(image_path)
                
                image_analysis = {
                    "metadata": metadata,
                    "reverse_search_matches": reverse_results.get("matches", 0),
                    "original_sources": reverse_results.get("sources", []),
                    "authenticity_flag": reverse_results.get("authenticity_flag", "unknown")
                }
                
                image_score = 0.5
                if reverse_results.get("authenticity_flag") == "manipulated":
                    flags.append("Image appears to be manipulated or out-of-context")
                    image_score = 0.2
                elif reverse_results.get("matches", 0) > 5:
                    flags.append(f"Image found in {reverse_results.get('matches', 0)} other sources")
                    image_score = 0.85
                elif reverse_results.get("matches", 0) > 0:
                    flags.append("Image appears in other sources")
                    image_score = 0.7
                else:
                    flags.append("Image not found in reverse search (may be new or unique)")
                    image_score = 0.5
                
                scores.append(image_score)
                
                try:
                    os.remove(image_path)
                except:
                    pass
            except Exception as e:
                logger.warning(f"Image analysis failed: {e}")
        
        # Calculate overall credibility score (0-100)
        overall_credibility_score = (sum(scores) / len(scores) * 100) if scores else 50
        
        # Risk level: HIGH SCORE = LOW RISK, LOW SCORE = HIGH RISK
        if overall_credibility_score >= 75:
            risk_level = "low"
        elif overall_credibility_score >= 50:
            risk_level = "medium"
        else:
            risk_level = "high"
        
        if not flags:
            flags.append("Analysis complete")
        
        return AnalysisResult(
            headline=headline,
            source_url=source_url,
            text_analysis=text_analysis,
            domain_analysis=domain_analysis,
            headline_corroboration=headline_corroboration,
            image_analysis=image_analysis,
            overall_credibility_score=round(overall_credibility_score, 1),
            risk_level=risk_level,
            flags=flags,
            timestamp=datetime.utcnow().isoformat()
        )
    
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Analysis error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

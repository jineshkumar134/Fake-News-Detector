import os
import logging
from typing import Dict
from datetime import datetime, timezone
import socket

logger = logging.getLogger(__name__)

SATIRICAL_DOMAINS = {
    "theonion.com", "babylonbee.com", "thespoof.com", "newsthump.com",
    "postmodernpostman.com", "dailycurrant.com", "nationalreport.net"
}

async def check_domain_reputation(url: str) -> Dict:
    """Check domain age, HTTPS, and reputation."""
    logger.info(f"Checking domain: {url}")
    
    try:
        # Extract domain
        domain = url.replace("https://", "").replace("http://", "").split('/')[0].lower()
        
        results = {
            "domain": domain,
            "is_satirical": domain in SATIRICAL_DOMAINS,
            "is_suspicious_domain": False,
            "domain_age_days": 365,  # Default
            "reputation_flags": [],
            "is_https": url.startswith("https://")
        }
        
        # Check HTTPS
        if not results["is_https"]:
            results["reputation_flags"].append("Uses HTTP instead of HTTPS")
        
        # Try WHOIS lookup
        try:
            import whois
            domain_info = whois.whois(domain)
            
            if domain_info.creation_date:
                if isinstance(domain_info.creation_date, list):
                    creation_date = domain_info.creation_date[0]
                else:
                    creation_date = domain_info.creation_date
                
                # Make datetime aware for comparison
                if creation_date.tzinfo is None:
                    creation_date = creation_date.replace(tzinfo=timezone.utc)
                
                now = datetime.now(timezone.utc)
                age = (now - creation_date).days
                results["domain_age_days"] = max(0, age)
                
                if age < 30:
                    results["is_suspicious_domain"] = True
                    results["reputation_flags"].append(f"Very new domain ({age} days old)")
                elif age < 90:
                    results["reputation_flags"].append(f"New domain ({age} days old)")
        except Exception as e:
            logger.warning(f"WHOIS lookup failed: {e}, using defaults")
            results["domain_age_days"] = 365
        
        return results
    
    except Exception as e:
        logger.error(f"Domain check error: {e}")
        return {
            "domain": "unknown",
            "is_satirical": False,
            "is_suspicious_domain": False,
            "domain_age_days": 365,
            "reputation_flags": [],
            "is_https": url.startswith("https://")
        }

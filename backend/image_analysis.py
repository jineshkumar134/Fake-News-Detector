import os
import logging
from typing import Dict
import hashlib

logger = logging.getLogger(__name__)

def extract_image_metadata(image_path: str) -> Dict:
    """Extract EXIF metadata from image."""
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        
        image = Image.open(image_path)
        exif_data = image.getexif()
        
        metadata = {
            "format": image.format,
            "size": image.size,
            "mode": image.mode,
        }
        
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = str(value)[:100]  # Limit string length
        
        return metadata
    except Exception as e:
        logger.warning(f"Could not extract metadata: {e}")
        return {"error": "Could not extract metadata"}

def reverse_image_search(image_path: str) -> Dict:
    """Simulate reverse image search (always returns mock data)."""
    logger.info(f"Searching for image: {image_path}")
    
    # Mock reverse search results
    results = {
        "matches": 0,
        "sources": [],
        "authenticity_flag": "unknown"
    }
    
    try:
        with open(image_path, "rb") as f:
            image_hash = hashlib.md5(f.read()).hexdigest()
        
        # Simulate finding matches based on hash
        hash_int = int(image_hash[:8], 16)
        match_count = (hash_int % 7)  # 0-6 matches
        
        if match_count >= 5:
            results["matches"] = match_count
            results["sources"] = [
                {"url": "https://example.com/news", "title": "Article 1"},
                {"url": "https://example.com/blog", "title": "Article 2"}
            ]
            results["authenticity_flag"] = "genuine"
        elif match_count == 0:
            results["authenticity_flag"] = "new_image"
        else:
            results["matches"] = match_count
            results["authenticity_flag"] = "original_source_found"
    
    except Exception as e:
        logger.warning(f"Reverse search failed: {e}")
    
    return results

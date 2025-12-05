"""
Test the Extrusion_Issue merge with sample images.
"""
import asyncio
import logging
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.app.services.vision_service import VisionService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_extrusion_samples():
    """Test with samples from the merged extrusion_issue directory."""
    vision_service = VisionService()
    
    if not vision_service.is_configured():
        logger.error("Vision API not configured")
        return
    
    # Get 5 images from extrusion_issue
    image_dir = Path("backend/validation_data/extrusion_issue/images")
    image_paths = list(image_dir.glob("*.jpg"))[:5]
    
    logger.info(f"\nTesting with {len(image_paths)} images from extrusion_issue")
    logger.info("=" * 70)
    
    for img_path in image_paths:
        logger.info(f"\n📸 Testing: {img_path.name}")
        
        with open(img_path, "rb") as f:
            image_data = f.read()
        
        try:
            result = await vision_service.analyze_image(image_data)
            
            logger.info(f"✅ Classification: {result['classification']}")
            logger.info(f"   Confidence: {result['confidence']}")
            logger.info(f"   Observations: {result['observations'][:2]}")  # First 2
            
            # Check if correctly identified as extrusion issue
            if result['classification'] == 'Extrusion_Issue':
                logger.info("   ✓ Correctly identified as Extrusion_Issue")
            else:
                logger.warning(f"   ⚠️  Classified as {result['classification']} instead")
                
        except Exception as e:
            logger.error(f"❌ Error: {e}")
    
    logger.info("\n" + "=" * 70)


if __name__ == "__main__":
    asyncio.run(test_extrusion_samples())

#!/usr/bin/env python3
"""Quick test script for Gemini 2.0 Flash with sample images."""

import asyncio
import logging
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from app.core.config import settings
from app.services.validation import VisionValidator
from app.services.vision_service import VisionService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main():
    """Test vision service with 10 sample images."""

    logger.info(f"Using model: {settings.GEMINI_MODEL}")
    logger.info(f"API key configured: {bool(settings.GOOGLE_GENAI_API_KEY)}")

    # Initialize services
    vision_service = VisionService()
    validator = VisionValidator(
        vision_service=vision_service, dataset_path="backend/validation_data"
    )

    # Get first 10 images from under_extrusion
    image_dir = Path("backend/validation_data/under_extrusion/images")
    image_paths = list(image_dir.glob("*.jpg"))[:10]

    logger.info(f"\nTesting with {len(image_paths)} images from under_extrusion")
    logger.info("=" * 60)

    results = []
    for i, image_path in enumerate(image_paths, 1):
        metadata = validator.load_metadata(image_path)
        if metadata is None:
            logger.warning(f"Skipping {image_path.name} - no metadata")
            continue

        logger.info(f"\n[{i}/{len(image_paths)}] Processing: {image_path.name}")

        try:
            result = await validator.validate_image(image_path, metadata)
            results.append(result)

            status = "✓" if result.correct else "✗"
            logger.info(f"  {status} Expected: {result.expected_defect}")
            logger.info(
                f"    Got: {result.predicted_defect} (confidence: {result.confidence:.2f})"
                if result.confidence
                else f"    Got: {result.predicted_defect}"
            )

        except Exception as e:
            logger.error(f"  Error: {e}")

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)

    correct = sum(1 for r in results if r.correct)
    total = len(results)
    accuracy = (correct / total * 100) if total > 0 else 0

    logger.info(f"Tested: {total} images")
    logger.info(f"Correct: {correct}")
    logger.info(f"Accuracy: {accuracy:.1f}%")

    # Show failures
    failures = [r for r in results if not r.correct]
    if failures:
        logger.info(f"\nFailed predictions ({len(failures)}):")
        for r in failures[:5]:  # Show first 5
            logger.info(f"  - {Path(r.image_path).name}")
            logger.info(f"    Expected: {r.expected_defect}, Got: {r.predicted_defect}")

    return 0 if accuracy >= 70 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

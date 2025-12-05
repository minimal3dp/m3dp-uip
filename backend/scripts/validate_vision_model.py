#!/usr/bin/env python3
"""CLI script for running vision model validation.

Usage:
    python -m backend.scripts.validate_vision_model [OPTIONS]

Examples:
    # Validate all defects
    python -m backend.scripts.validate_vision_model

    # Validate specific defect type
    python -m backend.scripts.validate_vision_model --defect stringing

    # Save report to custom location
    python -m backend.scripts.validate_vision_model --output reports/validation.json
"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from backend.app.core.config import settings
from backend.app.services.validation import VisionValidator
from backend.app.services.vision_service import VisionService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> int:
    """Run vision model validation."""
    parser = argparse.ArgumentParser(
        description="Validate vision model accuracy against reference images"
    )
    parser.add_argument(
        "--defect",
        type=str,
        help="Specific defect type to validate (default: all)",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default="backend/validation_data",
        help="Path to defect image dataset",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="backend/reports/vision_validation_report.json",
        help="Output path for validation report",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Check if Gemini API is configured
    if not settings.GOOGLE_GENAI_API_KEY:
        logger.error("GOOGLE_GENAI_API_KEY not configured. Set in .env file.")
        return 1

    # Check if dataset exists
    dataset_path = Path(args.dataset)
    if not dataset_path.exists():
        logger.error(f"Dataset path not found: {dataset_path}")
        return 1

    # Count images in dataset
    image_count = len(list(dataset_path.glob("**/*.jpg"))) + len(
        list(dataset_path.glob("**/*.png"))
    )
    if image_count == 0:
        logger.warning(f"No images found in {dataset_path}")
        logger.info("Please add reference images with metadata. See README.md")
        return 1

    logger.info(f"Found {image_count} images in dataset")

    try:
        # Initialize services
        logger.info("Initializing vision service...")
        vision_service = VisionService()

        logger.info("Initializing validator...")
        validator = VisionValidator(
            vision_service=vision_service,
            dataset_path=dataset_path,
        )

        # Run validation
        logger.info(f"Starting validation for: {args.defect or 'all defects'}")
        report = await validator.validate_dataset(defect_type=args.defect)

        # Display results
        logger.info("\n" + "=" * 60)
        logger.info("VALIDATION RESULTS")
        logger.info("=" * 60)
        logger.info(f"Total Images: {report.total_images}")
        logger.info(f"Correct Predictions: {report.correct_predictions}")
        logger.info(f"Overall Accuracy: {report.accuracy:.2%}")
        logger.info("")

        # Per-defect breakdown
        logger.info("Accuracy by Defect Type:")
        for defect, stats in sorted(report.by_defect_type.items()):
            logger.info(
                f"  {defect}: {stats['correct']}/{stats['total']} ({stats['accuracy']:.2%})"
            )

        # Failed predictions
        if report.failed_predictions:
            logger.info("")
            logger.info(f"Failed Predictions ({len(report.failed_predictions)}):")
            for failed in report.failed_predictions[:10]:  # Show first 10
                logger.info(
                    f"  {Path(failed.image_path).name}: "
                    f"Expected '{failed.expected_defect}', "
                    f"Got '{failed.predicted_defect}'"
                )
            if len(report.failed_predictions) > 10:
                logger.info(f"  ... and {len(report.failed_predictions) - 10} more")

        logger.info("=" * 60)

        # Save report
        validator.save_report(report, args.output)
        logger.info(f"\nDetailed report saved to: {args.output}")

        # Return non-zero if accuracy below threshold
        if report.accuracy < 0.80:  # 80% threshold
            logger.warning(f"\n⚠️  Accuracy ({report.accuracy:.2%}) below 80% threshold")
            return 1

        logger.info(f"\n✅ Validation passed with {report.accuracy:.2%} accuracy")
        return 0

    except Exception as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

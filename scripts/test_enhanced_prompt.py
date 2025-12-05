"""
Test the enhanced prompt with decision tree on confused samples.
"""

import asyncio
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.app.services.vision_service import VisionService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_confused_samples():
    """Test on samples that were previously confused."""
    vision_service = VisionService()

    if not vision_service.is_configured():
        logger.error("Vision API not configured")
        return

    # Load validation report to find confused samples
    report_path = Path("backend/reports/vision_validation_report.json")
    with open(report_path) as f:
        report = json.load(f)

    # Get samples from top confusion patterns
    test_cases = {
        "Spaghetti → Stringing": [],
        "Spaghetti → Poor_Bridging": [],
        "Stringing → Poor_Bridging": [],
        "Stringing → Spaghetti": [],
        "Warping → Poor_Bridging": [],
    }

    for fail in report["failed_predictions"]:
        expected = fail["expected_defect"]
        predicted = fail["predicted_defect"]
        pattern = f"{expected} → {predicted}"

        if pattern in test_cases and len(test_cases[pattern]) < 2:
            test_cases[pattern].append(fail)

    logger.info("\n" + "=" * 80)
    logger.info("TESTING ENHANCED PROMPT WITH DECISION TREE")
    logger.info("=" * 80)

    results = {"improved": 0, "still_wrong": 0, "total": 0}

    for pattern, samples in test_cases.items():
        if not samples:
            continue

        logger.info(f"\n### Testing Pattern: {pattern} ###\n")

        for sample in samples:
            results["total"] += 1
            img_path = Path(sample["image_path"])
            expected = sample["expected_defect"]
            old_pred = sample["predicted_defect"]

            if not img_path.exists():
                logger.warning(f"Image not found: {img_path}")
                continue

            logger.info(f"📸 {img_path.name}")
            logger.info(f"   Expected: {expected}")
            logger.info(f"   Old prediction: {old_pred}")

            with open(img_path, "rb") as f:
                image_data = f.read()

            try:
                result = await vision_service.analyze_image(image_data)
                new_pred = result["classification"]
                confidence = result["confidence"]

                logger.info(f"   New prediction: {new_pred} (confidence: {confidence})")

                if new_pred == expected:
                    logger.info("   ✅ IMPROVED! Now correct")
                    results["improved"] += 1
                elif new_pred == old_pred:
                    logger.info(f"   ⚠️  Still predicts {old_pred}")
                    results["still_wrong"] += 1
                else:
                    logger.info(f"   ⚠️  Different wrong answer: {new_pred}")
                    results["still_wrong"] += 1

                # Show reasoning
                if result.get("observations"):
                    logger.info(f"   Observations: {result['observations'][0][:100]}...")

            except Exception as e:
                logger.error(f"   ❌ Error: {e}")
                results["still_wrong"] += 1

    logger.info("\n" + "=" * 80)
    logger.info("RESULTS SUMMARY")
    logger.info("=" * 80)
    logger.info(f"Total tested: {results['total']}")
    logger.info(f"Improved (now correct): {results['improved']}")
    logger.info(f"Still wrong: {results['still_wrong']}")
    if results["total"] > 0:
        improvement_rate = (results["improved"] / results["total"]) * 100
        logger.info(f"Improvement rate: {improvement_rate:.1f}%")


if __name__ == "__main__":
    asyncio.run(test_confused_samples())

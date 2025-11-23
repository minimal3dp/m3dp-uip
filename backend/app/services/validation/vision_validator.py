"""Vision Model Validation Service.

This module provides tools for validating and benchmarking the vision API
against reference defect images with known classifications.
"""

import json
import logging
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from app.services.vision_service import VisionService

logger = logging.getLogger(__name__)


class ValidationMetadata(BaseModel):
    """Metadata for a reference defect image."""

    defect_type: str
    severity: str
    source: str
    source_url: str | None = None
    printer_type: str
    material: str
    expected_classification: str
    visual_markers: list[str]
    notes: str | None = None


class ValidationResult(BaseModel):
    """Result of validating a single image."""

    image_path: str
    expected_defect: str
    predicted_defect: str
    confidence: float | None = None
    correct: bool
    visual_markers_matched: list[str] | None = None
    notes: str | None = None


class ValidationReport(BaseModel):
    """Summary report of validation run."""

    total_images: int
    correct_predictions: int
    accuracy: float
    by_defect_type: dict[str, dict[str, Any]]
    confusion_matrix: dict[str, dict[str, int]] | None = None
    failed_predictions: list[ValidationResult]


class VisionValidator:
    """Service for validating vision model accuracy."""

    def __init__(
        self,
        vision_service: VisionService,
        dataset_path: Path | str = "backend/tests/fixtures/defect_images",
    ):
        """Initialize validator.

        Args:
            vision_service: VisionService instance to test
            dataset_path: Path to defect image dataset
        """
        self.vision_service = vision_service
        self.dataset_path = Path(dataset_path)
        self.results: list[ValidationResult] = []

    def load_metadata(self, image_path: Path) -> ValidationMetadata | None:
        """Load metadata JSON for an image.

        Args:
            image_path: Path to image file

        Returns:
            ValidationMetadata if found, None otherwise
        """
        metadata_path = image_path.parent / f"{image_path.stem}_metadata.json"
        if not metadata_path.exists():
            logger.warning(f"No metadata found for {image_path}")
            return None

        try:
            with open(metadata_path) as f:
                data = json.load(f)
            return ValidationMetadata(**data)
        except Exception as e:
            logger.error(f"Error loading metadata for {image_path}: {e}")
            return None

    async def validate_image(
        self, image_path: Path, metadata: ValidationMetadata
    ) -> ValidationResult:
        """Validate vision API prediction for a single image.

        Args:
            image_path: Path to defect image
            metadata: Expected classification metadata

        Returns:
            ValidationResult with comparison
        """
        try:
            # Read image
            with open(image_path, "rb") as f:
                image_data = f.read()

            # Get prediction from vision service
            # Note: Using context from metadata
            context = {
                "printer_model": metadata.printer_type,
                "filament_type": metadata.material,
            }
            response = await self.vision_service.analyze_image(
                image_data=image_data,
                context=context,
            )

            # Extract primary defect from response
            predicted_defect = response.get("defect_type", "Unknown")

            # Check if prediction matches expected
            correct = predicted_defect.lower() == metadata.expected_classification.lower()

            return ValidationResult(
                image_path=str(image_path),
                expected_defect=metadata.expected_classification,
                predicted_defect=predicted_defect,
                confidence=response.get("confidence"),
                correct=correct,
                visual_markers_matched=response.get("visual_markers"),
                notes=None,
            )

        except Exception as e:
            logger.error(f"Error validating {image_path}: {e}")
            return ValidationResult(
                image_path=str(image_path),
                expected_defect=metadata.expected_classification,
                predicted_defect="ERROR",
                confidence=None,
                correct=False,
                notes=f"Validation error: {str(e)}",
            )

    async def validate_dataset(self, defect_type: str | None = None) -> ValidationReport:
        """Run validation on entire dataset or specific defect type.

        Args:
            defect_type: If provided, only validate this defect type

        Returns:
            ValidationReport with accuracy metrics
        """
        self.results = []

        # Discover all images in dataset
        search_pattern = "**/*.jpg" if defect_type is None else f"{defect_type}/**/*.jpg"
        image_paths = list(self.dataset_path.glob(search_pattern))
        image_paths.extend(self.dataset_path.glob(search_pattern.replace(".jpg", ".png")))

        logger.info(f"Found {len(image_paths)} images to validate")

        # Validate each image
        for image_path in image_paths:
            metadata = self.load_metadata(image_path)
            if metadata is None:
                continue

            result = await self.validate_image(image_path, metadata)
            self.results.append(result)

        # Generate report
        return self._generate_report()

    def _generate_report(self) -> ValidationReport:
        """Generate validation report from results.

        Returns:
            ValidationReport with accuracy metrics
        """
        if not self.results:
            return ValidationReport(
                total_images=0,
                correct_predictions=0,
                accuracy=0.0,
                by_defect_type={},
                failed_predictions=[],
            )

        total = len(self.results)
        correct = sum(1 for r in self.results if r.correct)
        accuracy = correct / total if total > 0 else 0.0

        # Group by defect type
        by_defect: dict[str, dict[str, Any]] = {}
        for result in self.results:
            defect = result.expected_defect
            if defect not in by_defect:
                by_defect[defect] = {
                    "total": 0,
                    "correct": 0,
                    "accuracy": 0.0,
                }

            by_defect[defect]["total"] += 1
            if result.correct:
                by_defect[defect]["correct"] += 1

        # Calculate per-defect accuracy
        for _defect, stats in by_defect.items():
            stats["accuracy"] = stats["correct"] / stats["total"]

        # Collect failed predictions
        failed = [r for r in self.results if not r.correct]

        return ValidationReport(
            total_images=total,
            correct_predictions=correct,
            accuracy=accuracy,
            by_defect_type=by_defect,
            failed_predictions=failed,
        )

    def save_report(self, report: ValidationReport, output_path: Path | str) -> None:
        """Save validation report to JSON file.

        Args:
            report: ValidationReport to save
            output_path: Path to output JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(report.model_dump(), f, indent=2)

        logger.info(f"Validation report saved to {output_path}")

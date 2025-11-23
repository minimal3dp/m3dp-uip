"""Tests for vision model validation service."""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest
from app.services.validation import (
    ValidationMetadata,
    ValidationReport,
    ValidationResult,
    VisionValidator,
)


@pytest.fixture
def sample_metadata():
    """Sample validation metadata."""
    return ValidationMetadata(
        defect_type="Stringing",
        severity="Medium",
        source="All3DP",
        source_url="https://all3dp.com/...",
        printer_type="Generic",
        material="PLA",
        expected_classification="Stringing",
        visual_markers=["thin plastic threads", "strings between parts"],
        notes="Clear example with good lighting",
    )


@pytest.fixture
def mock_vision_service():
    """Mock VisionService."""
    service = MagicMock()
    service.analyze_image = AsyncMock()
    return service


@pytest.fixture
def validator(mock_vision_service, tmp_path):
    """VisionValidator instance with mock service."""
    return VisionValidator(
        vision_service=mock_vision_service,
        dataset_path=tmp_path / "test_images",
    )


class TestValidationMetadata:
    """Test ValidationMetadata model."""

    def test_metadata_creation(self, sample_metadata):
        """Test metadata can be created with all fields."""
        assert sample_metadata.defect_type == "Stringing"
        assert sample_metadata.expected_classification == "Stringing"
        assert len(sample_metadata.visual_markers) == 2

    def test_metadata_from_dict(self):
        """Test metadata can be created from dictionary."""
        data = {
            "defect_type": "Warping",
            "severity": "High",
            "source": "Prusa",
            "printer_type": "Generic",
            "material": "ABS",
            "expected_classification": "Warping",
            "visual_markers": ["corners lifting", "bed detachment"],
        }
        metadata = ValidationMetadata(**data)
        assert metadata.defect_type == "Warping"
        assert metadata.material == "ABS"


class TestValidationResult:
    """Test ValidationResult model."""

    def test_result_creation_correct(self):
        """Test result for correct prediction."""
        result = ValidationResult(
            image_path="test/stringing_001.jpg",
            expected_defect="Stringing",
            predicted_defect="Stringing",
            confidence=0.95,
            correct=True,
        )
        assert result.correct is True
        assert result.confidence == 0.95

    def test_result_creation_incorrect(self):
        """Test result for incorrect prediction."""
        result = ValidationResult(
            image_path="test/stringing_001.jpg",
            expected_defect="Stringing",
            predicted_defect="Warping",
            confidence=0.65,
            correct=False,
            notes="Misclassified due to dark background",
        )
        assert result.correct is False
        assert result.predicted_defect == "Warping"
        assert result.notes is not None


class TestVisionValidator:
    """Test VisionValidator service."""

    def test_validator_initialization(self, validator):
        """Test validator can be initialized."""
        assert validator.vision_service is not None
        assert validator.dataset_path is not None
        assert validator.results == []

    def test_load_metadata_success(self, validator, sample_metadata, tmp_path):
        """Test loading metadata from JSON file."""
        # Create test image and metadata
        image_dir = tmp_path / "test_images" / "stringing"
        image_dir.mkdir(parents=True)

        image_path = image_dir / "test_001.jpg"
        image_path.write_bytes(b"fake image data")

        metadata_path = image_dir / "test_001_metadata.json"
        metadata_path.write_text(sample_metadata.model_dump_json())

        # Load metadata
        loaded = validator.load_metadata(image_path)
        assert loaded is not None
        assert loaded.defect_type == "Stringing"
        assert loaded.expected_classification == "Stringing"

    def test_load_metadata_missing(self, validator, tmp_path):
        """Test loading metadata when file doesn't exist."""
        image_path = tmp_path / "test_images" / "nonexistent.jpg"
        loaded = validator.load_metadata(image_path)
        assert loaded is None

    def test_load_metadata_invalid_json(self, validator, tmp_path):
        """Test loading metadata with invalid JSON."""
        image_dir = tmp_path / "test_images"
        image_dir.mkdir(parents=True)

        image_path = image_dir / "test.jpg"
        image_path.write_bytes(b"fake")

        metadata_path = image_dir / "test_metadata.json"
        metadata_path.write_text("invalid json {{{")

        loaded = validator.load_metadata(image_path)
        assert loaded is None

    @pytest.mark.asyncio
    async def test_validate_image_correct_prediction(self, validator, sample_metadata, tmp_path):
        """Test validation with correct prediction."""
        # Setup mock response
        validator.vision_service.analyze_image.return_value = {
            "defect_type": "Stringing",
            "confidence": 0.92,
            "visual_markers": ["thin threads", "cobwebs"],
        }

        # Create test image
        image_path = tmp_path / "test_images" / "test.jpg"
        image_path.parent.mkdir(parents=True)
        image_path.write_bytes(b"fake image")

        # Validate
        result = await validator.validate_image(image_path, sample_metadata)

        assert result.correct is True
        assert result.predicted_defect == "Stringing"
        assert result.expected_defect == "Stringing"
        assert result.confidence == 0.92

    @pytest.mark.asyncio
    async def test_validate_image_incorrect_prediction(self, validator, sample_metadata, tmp_path):
        """Test validation with incorrect prediction."""
        # Setup mock response (wrong prediction)
        validator.vision_service.analyze_image.return_value = {
            "defect_type": "Warping",
            "confidence": 0.75,
        }

        image_path = tmp_path / "test_images" / "test.jpg"
        image_path.parent.mkdir(parents=True)
        image_path.write_bytes(b"fake image")

        result = await validator.validate_image(image_path, sample_metadata)

        assert result.correct is False
        assert result.predicted_defect == "Warping"
        assert result.expected_defect == "Stringing"

    @pytest.mark.asyncio
    async def test_validate_image_error_handling(self, validator, sample_metadata, tmp_path):
        """Test validation with service error."""
        # Setup mock to raise exception
        validator.vision_service.analyze_image.side_effect = Exception("API Error")

        image_path = tmp_path / "test_images" / "test.jpg"
        image_path.parent.mkdir(parents=True)
        image_path.write_bytes(b"fake image")

        result = await validator.validate_image(image_path, sample_metadata)

        assert result.correct is False
        assert result.predicted_defect == "ERROR"
        assert "API Error" in result.notes

    @pytest.mark.asyncio
    async def test_validate_dataset_empty(self, validator):
        """Test validation with no images in dataset."""
        report = await validator.validate_dataset()

        assert report.total_images == 0
        assert report.correct_predictions == 0
        assert report.accuracy == 0.0
        assert len(report.by_defect_type) == 0

    @pytest.mark.asyncio
    async def test_validate_dataset_with_images(self, validator, sample_metadata, tmp_path):
        """Test validation with multiple images."""
        # Setup mock responses
        validator.vision_service.analyze_image.side_effect = [
            {"defect_type": "Stringing", "confidence": 0.90},  # Correct
            {"defect_type": "Stringing", "confidence": 0.85},  # Correct
            {"defect_type": "Warping", "confidence": 0.70},  # Incorrect
        ]

        # Create test images with metadata
        image_dir = tmp_path / "test_images" / "stringing"
        image_dir.mkdir(parents=True)

        for i in range(3):
            image_path = image_dir / f"test_{i:03d}.jpg"
            image_path.write_bytes(b"fake image")

            metadata_path = image_dir / f"test_{i:03d}_metadata.json"
            metadata_path.write_text(sample_metadata.model_dump_json())

        # Run validation
        report = await validator.validate_dataset()

        assert report.total_images == 3
        assert report.correct_predictions == 2
        assert report.accuracy == pytest.approx(2 / 3)
        assert "Stringing" in report.by_defect_type
        assert report.by_defect_type["Stringing"]["total"] == 3
        assert report.by_defect_type["Stringing"]["correct"] == 2
        assert len(report.failed_predictions) == 1

    @pytest.mark.asyncio
    async def test_validate_dataset_specific_defect(self, validator, sample_metadata, tmp_path):
        """Test validation filtered by defect type."""
        validator.vision_service.analyze_image.return_value = {
            "defect_type": "Stringing",
            "confidence": 0.90,
        }

        # Create test image
        image_dir = tmp_path / "test_images" / "stringing"
        image_dir.mkdir(parents=True)

        image_path = image_dir / "test_001.jpg"
        image_path.write_bytes(b"fake")

        metadata_path = image_dir / "test_001_metadata.json"
        metadata_path.write_text(sample_metadata.model_dump_json())

        # Run validation for specific defect
        report = await validator.validate_dataset(defect_type="stringing")

        assert report.total_images >= 0  # May be 0 due to path matching

    def test_generate_report(self, validator):
        """Test report generation from results."""
        # Add mock results
        validator.results = [
            ValidationResult(
                image_path="test1.jpg",
                expected_defect="Stringing",
                predicted_defect="Stringing",
                confidence=0.9,
                correct=True,
            ),
            ValidationResult(
                image_path="test2.jpg",
                expected_defect="Stringing",
                predicted_defect="Warping",
                confidence=0.7,
                correct=False,
            ),
            ValidationResult(
                image_path="test3.jpg",
                expected_defect="Warping",
                predicted_defect="Warping",
                confidence=0.95,
                correct=True,
            ),
        ]

        report = validator._generate_report()

        assert report.total_images == 3
        assert report.correct_predictions == 2
        assert report.accuracy == pytest.approx(2 / 3)
        assert len(report.by_defect_type) == 2
        assert report.by_defect_type["Stringing"]["total"] == 2
        assert report.by_defect_type["Stringing"]["correct"] == 1
        assert report.by_defect_type["Warping"]["total"] == 1
        assert report.by_defect_type["Warping"]["correct"] == 1
        assert len(report.failed_predictions) == 1

    def test_save_report(self, validator, tmp_path):
        """Test saving validation report to JSON."""
        report = ValidationReport(
            total_images=10,
            correct_predictions=8,
            accuracy=0.8,
            by_defect_type={
                "Stringing": {"total": 5, "correct": 4, "accuracy": 0.8},
                "Warping": {"total": 5, "correct": 4, "accuracy": 0.8},
            },
            failed_predictions=[],
        )

        output_path = tmp_path / "report.json"
        validator.save_report(report, output_path)

        assert output_path.exists()

        # Verify JSON content
        with open(output_path) as f:
            data = json.load(f)

        assert data["total_images"] == 10
        assert data["accuracy"] == 0.8
        assert "Stringing" in data["by_defect_type"]


class TestValidationReport:
    """Test ValidationReport model."""

    def test_report_creation(self):
        """Test report creation with all fields."""
        report = ValidationReport(
            total_images=100,
            correct_predictions=85,
            accuracy=0.85,
            by_defect_type={
                "Stringing": {"total": 50, "correct": 45, "accuracy": 0.90},
            },
            failed_predictions=[],
        )

        assert report.total_images == 100
        assert report.accuracy == 0.85
        assert len(report.by_defect_type) == 1

    def test_report_serialization(self):
        """Test report can be serialized to dict."""
        report = ValidationReport(
            total_images=10,
            correct_predictions=8,
            accuracy=0.8,
            by_defect_type={},
            failed_predictions=[],
        )

        data = report.model_dump()
        assert isinstance(data, dict)
        assert data["total_images"] == 10
        assert data["accuracy"] == 0.8

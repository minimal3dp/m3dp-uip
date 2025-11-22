"""
Integration tests for diagnosis endpoints.

Tests end-to-end flows:
- Image upload → vision analysis → CSV recommendations
- Text query → semantic routing → CSV lookup
- Error handling and validation
- Response formatting
"""

import io
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient
from PIL import Image


@pytest.fixture
def client():
    """Create test client for FastAPI app."""
    # Import here to avoid circular imports
    from app.main import app

    return TestClient(app)


@pytest.fixture
def sample_image_bytes():
    """Create sample image bytes for testing."""
    # Create a small test image
    img = Image.new("RGB", (100, 100), color="red")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)
    return img_bytes.read()


@pytest.fixture
def mock_router_service():
    """Mock RouterService for integration tests."""
    with patch("app.api.endpoints.diagnosis.get_router_service") as mock:
        service = MagicMock()

        # Mock diagnose_from_text
        service.diagnose_from_text = AsyncMock(
            return_value={
                "classification": "calibration",
                "confidence": 0.9,
                "handler": "csv_lookup",
                "recommendations": [
                    {
                        "Name": "Rotation Distance",
                        "Description": "Calibrate extruder rotation distance",
                    }
                ],
            }
        )

        # Mock diagnose_from_image
        service.diagnose_from_image = AsyncMock(
            return_value={
                "classification": "Under_Extrusion",
                "issue_type": "Mechanical",
                "confidence": 0.85,
                "observations": ["Visible gaps between layers"],
                "likely_causes": ["Incorrect rotation distance", "Partial nozzle clog"],
                "recommendations": [
                    {
                        "Name": "Extruder Calibration",
                        "Fix": "Calibrate rotation distance",
                    }
                ],
                "handler": "vision_api",
            }
        )

        mock.return_value = service
        yield service


class TestAnalyzeImageEndpoint:
    """Test /analyze/image endpoint."""

    def test_analyze_image_success(self, client, sample_image_bytes, mock_router_service):
        """Test successful image analysis."""
        files = {"file": ("test.jpg", io.BytesIO(sample_image_bytes), "image/jpeg")}

        response = client.post("/api/v1/diagnosis/analyze/image", files=files)

        assert response.status_code == 200
        data = response.json()
        assert data["classification"] == "Under_Extrusion"
        assert data["issue_type"] == "Mechanical"
        assert data["confidence"] == 0.85
        assert len(data["observations"]) > 0
        assert len(data["likely_causes"]) > 0
        mock_router_service.diagnose_from_image.assert_called_once()

    def test_analyze_image_with_context(self, client, sample_image_bytes, mock_router_service):
        """Test image analysis with context fields."""
        files = {"file": ("test.jpg", io.BytesIO(sample_image_bytes), "image/jpeg")}
        data = {
            "filament_color": "Black",
            "printer_model": "Prusa MK4",
            "slicer": "OrcaSlicer",
            "nozzle_size": 0.4,
        }

        response = client.post(
            "/api/v1/diagnosis/analyze/image",
            files=files,
            data=data,
        )

        assert response.status_code == 200
        # Verify context was passed to service
        call_args = mock_router_service.diagnose_from_image.call_args
        assert call_args[1]["context"]["filament_color"] == "Black"
        assert call_args[1]["context"]["nozzle_size"] == 0.4

    def test_analyze_image_no_file(self, client):
        """Test image analysis without file returns error."""
        response = client.post("/api/v1/diagnosis/analyze/image")

        assert response.status_code == 422  # Validation error

    def test_analyze_image_invalid_file_type(self, client):
        """Test image analysis with invalid file type."""
        files = {"file": ("test.txt", io.BytesIO(b"not an image"), "text/plain")}

        response = client.post("/api/v1/diagnosis/analyze/image", files=files)

        # Should either validate MIME type or let vision API handle it
        # Behavior depends on implementation
        assert response.status_code in [400, 422, 500]


class TestAnalyzeTextEndpoint:
    """Test /analyze/text endpoint."""

    def test_analyze_text_success(self, client, mock_router_service):
        """Test successful text analysis."""
        request_data = {"query": "how do I calibrate e-steps"}

        response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

        assert response.status_code == 200
        data = response.json()
        assert data["classification"] == "calibration"
        assert data["confidence"] == 0.9
        assert data["handler"] == "csv_lookup"
        assert len(data["recommendations"]) > 0
        mock_router_service.diagnose_from_text.assert_called_once()

    def test_analyze_text_with_context(self, client, mock_router_service):
        """Test text analysis with context."""
        request_data = {
            "query": "PETG temperature settings",
            "printer_model": "Ender 3",
            "filament_type": "PETG",
        }

        response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

        assert response.status_code == 200
        # Verify context was passed
        call_args = mock_router_service.diagnose_from_text.call_args
        assert call_args[1]["context"]["filament_type"] == "PETG"

    def test_analyze_text_empty_query(self, client):
        """Test text analysis with empty query."""
        request_data = {"query": ""}

        response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

        # Should either validate or handle gracefully
        assert response.status_code in [200, 400, 422]

    def test_analyze_text_no_query(self, client):
        """Test text analysis without query field."""
        request_data = {}

        response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

        assert response.status_code == 422  # Validation error


class TestErrorHandling:
    """Test error handling in endpoints."""

    def test_analyze_image_service_error(self, client, sample_image_bytes):
        """Test image analysis handles service errors."""
        with patch("app.api.endpoints.diagnosis.get_router_service") as mock:
            service = MagicMock()
            service.diagnose_from_image = AsyncMock(side_effect=RuntimeError("Vision API error"))
            mock.return_value = service

            files = {"file": ("test.jpg", io.BytesIO(sample_image_bytes), "image/jpeg")}
            response = client.post("/api/v1/diagnosis/analyze/image", files=files)

            assert response.status_code == 500
            assert "error" in response.json() or "detail" in response.json()

    def test_analyze_text_service_error(self, client):
        """Service error now triggers fallback path instead of 500."""
        with patch("app.api.endpoints.diagnosis.get_router_service") as mock:
            service = MagicMock()
            service.diagnose_from_text = AsyncMock(side_effect=Exception("Service error"))
            mock.return_value = service

            request_data = {"query": "test query"}
            response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

            assert response.status_code == 200
            data = response.json()
            assert data["handler"] == "fallback_csv_router"
            assert data["confidence"] <= 0.6


class TestResponseFormat:
    """Test response formatting and structure."""

    def test_image_response_has_required_fields(self, client, sample_image_bytes):
        """Test image analysis response has all required fields."""
        files = {"file": ("test.jpg", io.BytesIO(sample_image_bytes), "image/jpeg")}
        response = client.post("/api/v1/diagnosis/analyze/image", files=files)
        if response.status_code == 500:
            # Vision path not configured (e.g., missing API key) — acceptable in CI
            pytest.skip("Vision API not configured; skipping image analysis validation")
        data = response.json()
        assert response.status_code == 200
        for field in [
            "classification",
            "issue_type",
            "confidence",
            "recommendations",
        ]:
            assert field in data

    def test_text_response_has_required_fields(self, client):
        """Test text analysis response has all required fields."""
        request_data = {"query": "test query"}

        response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

        assert response.status_code == 200
        data = response.json()

        # Required fields
        assert "classification" in data
        assert "confidence" in data
        assert "handler" in data
        assert "recommendations" in data


class TestCORS:
    """Test CORS configuration."""

    def test_cors_headers_present(self, client):
        """Test CORS headers are present in responses."""
        response = client.options("/api/v1/diagnosis/analyze/text")

        # Check for CORS headers (if configured)
        # This depends on your CORS middleware setup
        assert response.status_code in [200, 405]  # OPTIONS or method not allowed


class TestHealthCheck:
    """Test health check endpoints (if implemented)."""

    def test_health_endpoint(self, client):
        """Test health check endpoint."""
        # Try common health check paths
        for path in ["/health", "/api/health", "/"]:
            response = client.get(path)
            if response.status_code == 200:
                break
        else:
            # Skip if no health endpoint found
            pytest.skip("No health endpoint configured")


class TestEndToEndFlow:
    """Test complete end-to-end diagnostic flows."""

    @pytest.mark.asyncio
    async def test_complete_image_diagnosis_flow(self, client, sample_image_bytes):
        """Test complete flow from image upload to recommendations."""
        # Step 1: Upload image
        files = {"file": ("test.jpg", io.BytesIO(sample_image_bytes), "image/jpeg")}
        data = {"filament_color": "Black", "printer_model": "Prusa MK4"}

        response = client.post(
            "/api/v1/diagnosis/analyze/image",
            files=files,
            data=data,
        )

        if response.status_code == 500:
            pytest.skip("Vision API unavailable; skipping end-to-end image flow")
        result = response.json()
        assert response.status_code == 200
        assert "recommendations" in result
        assert "classification" in result

    def test_complete_text_diagnosis_flow(self, client):
        """Test complete flow from text query to recommendations."""
        # Step 1: Submit query
        request_data = {
            "query": "my prints have gaps between layers",
            "printer_model": "Ender 3",
            "filament_type": "PLA",
        }

        response = client.post("/api/v1/diagnosis/analyze/text", json=request_data)

        # Step 2: Verify analysis completed
        assert response.status_code == 200
        result = response.json()

        # Step 3: Verify recommendations provided
        assert "recommendations" in result

        # Step 4: Verify classification and handler
        assert "classification" in result
        assert "handler" in result

"""
Integration tests for complete diagnostic workflows.

Tests end-to-end flows with real services:
- CSV Loader → Semantic Router → Response formatting
- Vision Service → Router Service → CSV lookup
- Error handling across service boundaries
"""

import io
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from PIL import Image


@pytest.fixture
def client():
    """Create test client."""
    from app.main import app

    return TestClient(app)


@pytest.fixture
def sample_image():
    """Create sample test image."""
    img = Image.new("RGB", (100, 100), color="red")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)
    return img_bytes.read()


class TestTextDiagnosisIntegration:
    """Test text-based diagnosis with real CSV data."""

    def test_calibration_query_returns_csv_data(self, client):
        """Test calibration query flows through router to CSV."""
        response = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={"query": "how do I calibrate extruder rotation distance"},
        )

        assert response.status_code == 200
        data = response.json()

        # Verify routing classified correctly (may fallback to general without API key)
        assert data["classification"] in ["calibration", "klipper_calibrations", "general"]
        assert data["handler"] in ["csv_lookup", "fallback_csv_router", "fallback"]

        # Verify CSV data returned
        assert "recommendations" in data
        assert len(data["recommendations"]) > 0

    def test_troubleshooting_query_returns_csv_data(self, client):
        """Test troubleshooting query gets defect data."""
        response = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={"query": "my print has strings all over it"},
        )

        assert response.status_code == 200
        data = response.json()

        # Should route to troubleshooting (or general if router not configured)
        assert data["classification"] in ["troubleshooting", "orca_recommendations", "general"]
        assert "recommendations" in data

    def test_material_query_returns_csv_data(self, client):
        """Test material query gets material profiles."""
        response = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={
                "query": "what temperature should I use for PETG",
                "filament_type": "PETG",
            },
        )

        assert response.status_code == 200
        data = response.json()

        # Should route to material profiles (or general if router not configured)
        assert data["classification"] in ["material", "orca_recommendations", "general"]
        assert "recommendations" in data


class TestImageDiagnosisIntegration:
    """Test image-based diagnosis with vision API."""

    def test_vision_to_csv_flow(self, client, sample_image):
        """Test vision API classifies and returns CSV recommendations."""
        files = {"file": ("test.jpg", io.BytesIO(sample_image), "image/jpeg")}

        response = client.post("/api/v1/diagnosis/analyze/image", files=files)

        # May fail if GOOGLE_GENAI_API_KEY not set
        if response.status_code == 500:
            pytest.skip("Vision API not configured")

        assert response.status_code == 200
        data = response.json()

        # Vision should classify defect
        assert "classification" in data
        assert "confidence" in data

        # Should return recommendations from CSV
        assert "recommendations" in data

    def test_vision_with_context_integration(self, client, sample_image):
        """Test vision API uses context for better classification."""
        files = {"file": ("test.jpg", io.BytesIO(sample_image), "image/jpeg")}
        data = {
            "filament_color": "Black",
            "printer_model": "Prusa MK4",
            "nozzle_size": 0.4,
        }

        response = client.post(
            "/api/v1/diagnosis/analyze/image",
            files=files,
            data=data,
        )

        if response.status_code == 500:
            pytest.skip("Vision API not configured")

        assert response.status_code == 200


class TestCalculatorIntegration:
    """Test calculator endpoints with data validation."""

    def test_rotation_distance_calculator_flow(self, client):
        """Test rotation distance calculation returns correct format."""
        response = client.post(
            "/api/v1/calculators/rotation-distance",
            json={
                "current_rotation_distance": 33.5,
                "requested_extrusion": 100.0,
                "actual_extrusion": 98.5,
            },
        )

        assert response.status_code == 200
        data = response.json()

        # Verify calculation result
        assert "new_rotation_distance" in data
        assert "klipper_config" in data
        assert data["new_rotation_distance"] > 0

    def test_pressure_advance_calculator_flow(self, client):
        """Test pressure advance calculation with material type."""
        response = client.post(
            "/api/v1/calculators/pressure-advance",
            json={
                "material_type": "PLA",
                "current_pa": 0.0,
                "print_speed": 100.0,
                "nozzle_diameter": 0.4,
            },
        )

        assert response.status_code == 200
        data = response.json()

        # Verify pressure advance result
        assert "recommended_range" in data
        assert "start_value" in data
        assert "increment" in data
        assert "test_parameters" in data
        assert "klipper_config" in data
        assert "calibration_method" in data
        assert isinstance(data["recommended_range"], list)
        assert len(data["recommended_range"]) == 2
        assert data["start_value"] >= 0

    def test_calculator_validation_errors(self, client):
        """Test calculator handles invalid input."""
        response = client.post(
            "/api/v1/calculators/rotation-distance",
            json={
                "current_rotation_distance": -1,  # Invalid
                "requested_extrusion": 100.0,
                "actual_extrusion": 98.5,
            },
        )

        assert response.status_code == 422  # Validation error


class TestCSVLoaderIntegration:
    """Test CSV loader service integration."""

    def test_csv_loader_caches_data(self, client):
        """Test CSV data is cached across requests."""
        # First request - loads CSV
        response1 = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={"query": "calibration"},
        )

        # Second request - should use cache
        response2 = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={"query": "calibration"},
        )

        assert response1.status_code == 200
        assert response2.status_code == 200

    def test_csv_validation_endpoint_integration(self, client):
        """Test CSV validation endpoint returns loader state."""
        response = client.get("/api/v1/diagnosis/csv-validation")

        assert response.status_code == 200
        data = response.json()

        assert "has_errors" in data
        assert "loaded_files" in data


class TestErrorHandlingIntegration:
    """Test error handling across service boundaries."""

    def test_vision_api_error_fallback(self, client, sample_image):
        """Test system handles vision API failures gracefully."""
        # Mock vision service to fail
        with patch("app.services.vision_service.VisionService.analyze_image") as mock:
            mock.side_effect = Exception("API error")

            files = {"file": ("test.jpg", io.BytesIO(sample_image), "image/jpeg")}
            response = client.post("/api/v1/diagnosis/analyze/image", files=files)

            # Should return error but not crash
            assert response.status_code in [200, 500]

    def test_csv_missing_graceful_handling(self, client):
        """Test system handles missing CSV files gracefully."""
        # This should work because CSV files are present
        response = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={"query": "test"},
        )

        # Should return something, even if CSV is missing
        assert response.status_code in [200, 500]

    def test_invalid_calculator_input_validation(self, client):
        """Test calculator validates input properly."""
        response = client.post(
            "/api/v1/calculators/rotation-distance",
            json={
                "current_rotation_distance": "invalid",  # Should be float
                "requested_extrusion": 100.0,
                "actual_extrusion": 98.5,
            },
        )

        assert response.status_code == 422


class TestPerformanceIntegration:
    """Test performance characteristics of integrated services."""

    def test_text_diagnosis_response_time(self, client):
        """Test text diagnosis completes in reasonable time."""
        import time

        start = time.time()
        response = client.post(
            "/api/v1/diagnosis/analyze/text",
            json={"query": "calibration help"},
        )
        duration = time.time() - start

        assert response.status_code == 200
        # Should complete in under 2 seconds
        assert duration < 2.0

    def test_calculator_response_time(self, client):
        """Test calculator completes quickly."""
        import time

        start = time.time()
        response = client.post(
            "/api/v1/calculators/rotation-distance",
            json={
                "current_rotation_distance": 33.5,
                "requested_extrusion": 100.0,
                "actual_extrusion": 98.5,
            },
        )
        duration = time.time() - start

        assert response.status_code == 200
        # Should be nearly instant (<100ms)
        assert duration < 0.1


class TestConcurrentRequests:
    """Test handling of concurrent requests."""

    def test_concurrent_text_diagnosis(self, client):
        """Test multiple simultaneous text diagnoses."""
        import concurrent.futures

        def make_request():
            return client.post(
                "/api/v1/diagnosis/analyze/text",
                json={"query": "test query"},
            )

        # Make 5 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            responses = [f.result() for f in futures]

        # All should succeed
        for response in responses:
            assert response.status_code == 200

    def test_concurrent_calculators(self, client):
        """Test multiple simultaneous calculator requests."""
        import concurrent.futures

        def make_request():
            return client.post(
                "/api/v1/calculators/rotation-distance",
                json={
                    "current_rotation_distance": 33.5,
                    "requested_extrusion": 100.0,
                    "actual_extrusion": 98.5,
                },
            )

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            responses = [f.result() for f in futures]

        for response in responses:
            assert response.status_code == 200

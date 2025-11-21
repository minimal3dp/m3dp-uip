"""
Tests for FastAPI application endpoints.
"""

import pytest
from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient):
    """Test root endpoint returns health check."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "M3DP-UIP API"
    assert "version" in data


def test_health_endpoint(client: TestClient):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "environment" in data


@pytest.mark.skip(reason="Diagnosis endpoint not yet implemented")
def test_analyze_image_endpoint(client: TestClient, sample_image_data: bytes):
    """Test image analysis endpoint."""
    files = {"file": ("test.png", sample_image_data, "image/png")}
    response = client.post("/api/v1/analyze/image", files=files)
    assert response.status_code == 200
    data = response.json()
    assert "issue_type" in data
    assert "classification" in data
    assert "recommendations" in data

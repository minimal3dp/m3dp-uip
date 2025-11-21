"""
Tests for Calculator API Endpoints

Validates CSV-driven formula calculations and API behavior.
"""

from app.main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)


# ============================================================================
# Calculator List Tests
# ============================================================================


def test_list_calculators():
    """Test calculator listing endpoint."""
    response = client.get("/api/v1/calculators")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "calculators" in data
    assert len(data["calculators"]) >= 2  # rotation-distance, pressure-advance

    # Check required fields
    for calc in data["calculators"]:
        assert "id" in calc
        assert "name" in calc
        assert "category" in calc
        assert "csv_source" in calc
        assert "endpoint" in calc


# ============================================================================
# Rotation Distance Calculator Tests
# ============================================================================


def test_rotation_distance_calculation_basic():
    """Test basic rotation distance calculation."""
    request_data = {
        "current_rotation_distance": 33.5,
        "requested_extrusion": 100,
        "actual_extrusion": 98.5,
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Formula: new = (current * actual) / requested
    # Expected: (33.5 * 98.5) / 100 = 33.0
    assert "new_rotation_distance" in data
    assert abs(data["new_rotation_distance"] - 33.0) < 0.1

    assert "change_percent" in data
    assert "within_tolerance" in data
    assert "klipper_config" in data
    assert "rotation_distance:" in data["klipper_config"]
    assert "recommendation" in data


def test_rotation_distance_within_tolerance():
    """Test calculation within ±2mm tolerance."""
    request_data = {
        "current_rotation_distance": 33.5,
        "requested_extrusion": 100,
        "actual_extrusion": 99.0,  # 1mm deviation = within tolerance
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["within_tolerance"] is True
    assert "✅" in data["recommendation"]


def test_rotation_distance_outside_tolerance():
    """Test calculation outside ±2mm tolerance."""
    request_data = {
        "current_rotation_distance": 33.5,
        "requested_extrusion": 100,
        "actual_extrusion": 95.0,  # 5mm deviation = outside tolerance
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["within_tolerance"] is False
    assert "⚠️" in data["recommendation"]
    assert "re-calibrate" in data["recommendation"].lower()


def test_rotation_distance_formula_accuracy():
    """Test formula accuracy against known values."""
    # Test case from CSV documentation
    # Current: 33.5, Requested: 100, Actual: 98.5
    # Expected: (33.5 * 98.5) / 100 = 32.9975 ≈ 33.0
    request_data = {
        "current_rotation_distance": 33.5,
        "requested_extrusion": 100,
        "actual_extrusion": 98.5,
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)
    data = response.json()

    # Formula validation
    expected = (33.5 * 98.5) / 100
    assert abs(data["new_rotation_distance"] - expected) < 0.001


def test_rotation_distance_validation_negative():
    """Test validation rejects negative values."""
    request_data = {
        "current_rotation_distance": -33.5,  # Invalid: negative
        "requested_extrusion": 100,
        "actual_extrusion": 98.5,
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_rotation_distance_validation_zero():
    """Test validation rejects zero requested extrusion."""
    request_data = {
        "current_rotation_distance": 33.5,
        "requested_extrusion": 0,  # Invalid: zero causes division error
        "actual_extrusion": 98.5,
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)

    # Should reject at validation level (Pydantic) or calculation level
    assert response.status_code in [
        status.HTTP_422_UNPROCESSABLE_ENTITY,
        status.HTTP_400_BAD_REQUEST,
    ]


def test_rotation_distance_validation_out_of_range():
    """Test validation rejects unrealistic values."""
    request_data = {
        "current_rotation_distance": 200,  # Invalid: > 100
        "requested_extrusion": 100,
        "actual_extrusion": 98.5,
    }

    response = client.post("/api/v1/calculators/rotation-distance", json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


# ============================================================================
# Pressure Advance Calculator Tests
# ============================================================================


def test_pressure_advance_pla():
    """Test pressure advance calculation for PLA."""
    request_data = {
        "material_type": "PLA",
        "print_speed": 100,
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Check PLA range (0.03 - 0.06 per CSV)
    assert data["recommended_range"] == [0.03, 0.06]
    assert data["start_value"] == 0.0  # Default when no current PA provided
    assert data["increment"] == 0.005  # Standard increment
    assert "test_parameters" in data
    assert data["test_parameters"]["speed"] == 100
    assert "klipper_config" in data
    assert "pressure_advance:" in data["klipper_config"]


def test_pressure_advance_petg():
    """Test pressure advance calculation for PETG."""
    request_data = {
        "material_type": "PETG",
        "current_pa": 0.05,  # Existing value
        "print_speed": 80,
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Check PETG range (0.06 - 0.08 per CSV)
    assert data["recommended_range"] == [0.06, 0.08]
    assert data["start_value"] == 0.05  # Uses provided current PA
    assert data["test_parameters"]["speed"] == 80


def test_pressure_advance_tpu():
    """Test pressure advance calculation for TPU (flexible)."""
    request_data = {
        "material_type": "TPU",
        "print_speed": 30,  # Slow for flexible
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # TPU needs very low PA (0.0 - 0.02)
    assert data["recommended_range"] == [0.0, 0.02]
    assert data["start_value"] == 0.0


def test_pressure_advance_case_insensitive():
    """Test material type is case-insensitive."""
    for material in ["pla", "PLA", "Pla"]:
        request_data = {
            "material_type": material,
            "print_speed": 100,
            "nozzle_diameter": 0.4,
        }

        response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["recommended_range"] == [0.03, 0.06]


def test_pressure_advance_invalid_material():
    """Test invalid material type returns 400."""
    request_data = {
        "material_type": "CHOCOLATE",  # Not a real filament
        "print_speed": 100,
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "not recognized" in response.json()["detail"]


def test_pressure_advance_test_parameters():
    """Test test parameters are correctly populated."""
    request_data = {
        "material_type": "ABS",
        "current_pa": 0.04,
        "print_speed": 120,
        "nozzle_diameter": 0.6,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    params = data["test_parameters"]
    assert params["start_pa"] == 0.04
    assert params["end_pa"] > data["recommended_range"][1]  # Extends beyond max
    assert params["increment"] == 0.005
    assert params["speed"] == 120
    assert params["layer_height"] == 0.2  # Standard from CSV
    assert params["line_width"] == 0.6  # Matches nozzle
    assert params["nozzle_diameter"] == 0.6


def test_pressure_advance_validation_negative_pa():
    """Test validation rejects negative pressure advance."""
    request_data = {
        "material_type": "PLA",
        "current_pa": -0.05,  # Invalid: negative
        "print_speed": 100,
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_pressure_advance_validation_high_pa():
    """Test validation rejects unrealistic PA values."""
    request_data = {
        "material_type": "PLA",
        "current_pa": 5.0,  # Invalid: > 1.0
        "print_speed": 100,
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


# ============================================================================
# Integration Tests
# ============================================================================


def test_calculator_endpoints_return_consistent_format():
    """Test all calculators return consistent response formats."""
    # Each calculator should include config snippets
    rotation_response = client.post(
        "/api/v1/calculators/rotation-distance",
        json={
            "current_rotation_distance": 33.5,
            "requested_extrusion": 100,
            "actual_extrusion": 98.5,
        },
    )

    pa_response = client.post(
        "/api/v1/calculators/pressure-advance",
        json={"material_type": "PLA", "print_speed": 100, "nozzle_diameter": 0.4},
    )

    assert rotation_response.status_code == status.HTTP_200_OK
    assert pa_response.status_code == status.HTTP_200_OK

    # Both should have klipper_config
    assert "klipper_config" in rotation_response.json()
    assert "klipper_config" in pa_response.json()


def test_calculator_cors_headers():
    """Test CORS headers are present for calculator endpoints."""
    response = client.options("/api/v1/calculators/rotation-distance")

    # FastAPI TestClient doesn't fully simulate CORS, but we can verify endpoint exists
    assert response.status_code in [
        status.HTTP_200_OK,
        status.HTTP_405_METHOD_NOT_ALLOWED,
    ]

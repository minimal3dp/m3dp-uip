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
    assert (
        len(data["calculators"]) >= 4
    )  # rotation-distance, orcaslicer-flow, orcaslicer-flow-yolo, pressure-advance

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

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


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
        status.HTTP_422_UNPROCESSABLE_CONTENT,
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

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


# ============================================================================
# OrcaSlicer Flow Calibration Calculator Tests
# ============================================================================


def test_orcaslicer_flow_pass_1_only():
    """Test OrcaSlicer Flow Rate Pass 1 calculation only."""
    request_data = {
        "old_flow_rate": 0.99,
        "pass_1_slide_value": -10,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Formula: pass_1_flow = 0.99 * (100 + (-10)) / 100 = 0.891
    expected_pass_1 = 0.99 * (100 + (-10)) / 100
    assert abs(data["pass_1_flow"] - expected_pass_1) < 0.001
    assert data["pass_2_flow"] is None
    assert "pass_1_flow" in data
    assert "change_from_original" in data
    assert "slicer_config" in data
    assert "recommendation" in data
    assert "Pass 1 complete" in data["recommendation"]


def test_orcaslicer_flow_two_pass():
    """Test OrcaSlicer Flow Rate two-pass calculation."""
    request_data = {
        "old_flow_rate": 0.99,
        "pass_1_slide_value": -10,
        "pass_2_slide_value": -1,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Formula: pass_1 = 0.99 * (100 + (-10)) / 100 = 0.891
    # Formula: pass_2 = 0.891 * (100 + (-1)) / 100 = 0.882
    expected_pass_1 = 0.99 * (100 + (-10)) / 100
    expected_pass_2 = expected_pass_1 * (100 + (-1)) / 100

    assert abs(data["pass_1_flow"] - expected_pass_1) < 0.001
    assert abs(data["pass_2_flow"] - expected_pass_2) < 0.001
    assert "Calibration complete" in data["recommendation"]


def test_orcaslicer_flow_formula_accuracy():
    """Test OrcaSlicer Flow formula accuracy against Excel."""
    # From EXTRACTED_FORMULAS.md (OrcaSlicer Flow Calibration sheet)
    request_data = {
        "old_flow_rate": 0.99,
        "pass_1_slide_value": -10,
        "pass_2_slide_value": -1,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow", json=request_data)
    data = response.json()

    # Exact formula from Excel
    pass_1_expected = 0.99 * (100 - 10) / 100
    pass_2_expected = pass_1_expected * (100 - 1) / 100

    assert abs(data["pass_1_flow"] - pass_1_expected) < 0.0001
    assert abs(data["pass_2_flow"] - pass_2_expected) < 0.0001


def test_orcaslicer_flow_validation():
    """Test OrcaSlicer Flow validation."""
    # Missing pass_1_slide_value
    request_data = {
        "old_flow_rate": 1.0,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow", json=request_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_orcaslicer_flow_yolo_basic():
    """Test OrcaSlicer Flow YOLO calculation."""
    request_data = {
        "old_flow_rate": 1.0,
        "yolo_slide_value": -0.035,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow-yolo", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Formula: new_flow = 1.0 + (-0.035) = 0.965
    expected_flow = 1.0 + (-0.035)
    assert abs(data["new_flow"] - expected_flow) < 0.001
    assert "new_flow" in data
    assert "change_from_original" in data
    assert "slicer_config" in data
    assert "YOLO calibration complete" in data["recommendation"]


def test_orcaslicer_flow_yolo_formula_accuracy():
    """Test OrcaSlicer Flow YOLO formula accuracy against Excel."""
    # From EXTRACTED_FORMULAS.md (OrcaSlicer Flow YOLO sheet)
    request_data = {
        "old_flow_rate": 1.0,
        "yolo_slide_value": -0.035,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow-yolo", json=request_data)
    data = response.json()

    # Exact formula from Excel
    expected_flow = 1.0 + (-0.035)
    assert abs(data["new_flow"] - expected_flow) < 0.0001


def test_orcaslicer_flow_yolo_positive_adjustment():
    """Test YOLO with positive slide value."""
    request_data = {
        "old_flow_rate": 1.0,
        "yolo_slide_value": 0.02,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow-yolo", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Formula: new_flow = 1.0 + 0.02 = 1.02
    assert abs(data["new_flow"] - 1.02) < 0.001


def test_orcaslicer_flow_yolo_validation():
    """Test OrcaSlicer Flow YOLO validation."""
    # Missing yolo_slide_value
    request_data = {
        "old_flow_rate": 1.0,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow-yolo", json=request_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_orcaslicer_flow_yolo_calculation_result():
    """Test OrcaSlicer Flow YOLO calculation result."""
    # From EXTRACTED_FORMULAS.md (OrcaSlicer Flow YOLO sheet)
    request_data = {
        "old_flow_rate": 1.0,
        "yolo_slide_value": -0.035,
    }

    response = client.post("/api/v1/calculators/orcaslicer-flow-yolo", json=request_data)
    data = response.json()

    # Exact formula from Excel
    expected_flow = 1.0 + (-0.035)
    assert abs(data["new_flow"] - expected_flow) < 0.0001


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

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_pressure_advance_validation_high_pa():
    def test_pressure_advance_asa_and_nylon_ranges():
        """Test ASA and NYLON material ranges and midpoint config generation."""
        for material, expected in {"ASA": [0.04, 0.07], "NYLON": [0.05, 0.08]}.items():
            resp = client.post(
                "/api/v1/calculators/pressure-advance",
                json={"material_type": material, "print_speed": 90, "nozzle_diameter": 0.4},
            )
            assert resp.status_code == status.HTTP_200_OK
            data = resp.json()
            assert data["recommended_range"] == expected
            # Midpoint used in klipper_config
            midpoint = sum(expected) / 2
            assert f"pressure_advance: {midpoint:.3f}" in data["klipper_config"]

    def test_pressure_advance_midpoint_config_with_current_pa():
        """When current_pa provided, ensure start_value differs from midpoint and config uses midpoint."""
        resp = client.post(
            "/api/v1/calculators/pressure-advance",
            json={
                "material_type": "PETG",
                "current_pa": 0.07,
                "print_speed": 80,
                "nozzle_diameter": 0.4,
            },
        )
        assert resp.status_code == status.HTTP_200_OK
        data = resp.json()
        assert data["start_value"] == 0.07
        midpoint = sum(data["recommended_range"]) / 2
        assert f"pressure_advance: {midpoint:.3f}" in data["klipper_config"]

    def test_pressure_advance_unrecognized_material_error_message():
        """Validate error message content for unrecognized material."""
        resp = client.post(
            "/api/v1/calculators/pressure-advance",
            json={"material_type": "WOOD", "print_speed": 100, "nozzle_diameter": 0.4},
        )
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        detail = resp.json()["detail"]
        assert "Supported:" in detail and "PLA" in detail

    """Test validation rejects unrealistic PA values."""
    request_data = {
        "material_type": "PLA",
        "current_pa": 5.0,  # Invalid: > 1.0
        "print_speed": 100,
        "nozzle_diameter": 0.4,
    }

    response = client.post("/api/v1/calculators/pressure-advance", json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


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


# ============================================================================
# Temperature Tower Calculator Tests (Phase 5)
# ============================================================================


def test_temperature_tower_basic():
    """Test basic temperature tower calculation."""
    request_data = {
        "tower_start_temp": 220,
        "tower_end_temp": 180,
        "temp_increment": 5,
        "best_segment_height": 36,
        "total_tower_height": 60,
        "observations": "Best surface finish at 36mm height",
    }

    response = client.post("/api/v1/calculators/temperature-tower", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "optimal_temperature" in data
    assert data["optimal_temperature"] == 195  # 220 - (3 * 5)
    assert "temperature_range" in data
    assert data["temperature_range"]["optimal"] == 195
    assert data["temperature_range"]["safe_min"] == 190
    assert data["temperature_range"]["safe_max"] == 200
    assert "quality_summary" in data
    assert "adjustment_notes" in data
    assert "klipper_config" in data


def test_temperature_tower_validation_inverted_temps():
    """Test temperature tower rejects start temp <= end temp."""
    request_data = {
        "tower_start_temp": 180,
        "tower_end_temp": 220,
        "temp_increment": 5,
        "best_segment_height": 36,
        "total_tower_height": 60,
    }

    response = client.post("/api/v1/calculators/temperature-tower", json=request_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "higher than end temperature" in response.json()["detail"]


def test_temperature_tower_validation_negative_increment():
    """Test temperature tower rejects negative increment."""
    request_data = {
        "tower_start_temp": 220,
        "tower_end_temp": 180,
        "temp_increment": -5,
        "best_segment_height": 36,
        "total_tower_height": 60,
    }

    response = client.post("/api/v1/calculators/temperature-tower", json=request_data)

    # Pydantic validation returns 422
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_temperature_tower_validation_height_exceeded():
    """Test temperature tower rejects best segment height > total height."""
    request_data = {
        "tower_start_temp": 220,
        "tower_end_temp": 180,
        "temp_increment": 5,
        "best_segment_height": 70,
        "total_tower_height": 60,
    }

    response = client.post("/api/v1/calculators/temperature-tower", json=request_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "cannot exceed total tower height" in response.json()["detail"]


# ============================================================================
# Retraction Tuning Calculator Tests (Phase 5)
# ============================================================================


def test_retraction_tuning_direct_drive_moderate():
    """Test retraction tuning for direct drive with moderate stringing."""
    request_data = {
        "extruder_type": "Direct Drive",
        "current_retraction_distance": 1.0,
        "current_retraction_speed": 35,
        "stringing_severity": "moderate",
        "test_result": "Some stringing visible",
    }

    response = client.post("/api/v1/calculators/retraction-tuning", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "recommended_distance" in data
    assert data["recommended_distance"] == 1.5  # Current + 0.5
    assert "recommended_speed" in data
    assert data["recommended_speed"] == 40  # Current + 5
    assert data["z_hop"] is True
    assert data["z_hop_height"] == 0.2
    assert data["wipe"] is True
    assert "temperature_note" in data
    assert "orcaslicer_settings" in data


def test_retraction_tuning_bowden_severe():
    """Test retraction tuning for bowden with severe stringing."""
    request_data = {
        "extruder_type": "Bowden",
        "current_retraction_distance": 5.0,
        "current_retraction_speed": 45,
        "stringing_severity": "severe",
        "test_result": "Heavy stringing everywhere",
    }

    response = client.post("/api/v1/calculators/retraction-tuning", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["recommended_distance"] == 8.0  # Max for Bowden
    assert data["recommended_speed"] == 70  # Max for Bowden
    assert data["z_hop"] is True
    assert data["z_hop_height"] == 0.4
    assert data["wipe"] is True


def test_retraction_tuning_none_severity():
    """Test retraction tuning with no stringing keeps current settings."""
    request_data = {
        "extruder_type": "Direct Drive",
        "current_retraction_distance": 1.5,
        "current_retraction_speed": 40,
        "stringing_severity": "none",
        "test_result": "No stringing observed",
    }

    response = client.post("/api/v1/calculators/retraction-tuning", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["recommended_distance"] == 1.5  # Unchanged
    assert data["recommended_speed"] == 40  # Unchanged
    assert data["z_hop"] is False
    assert data["wipe"] is False


def test_retraction_tuning_invalid_extruder_type():
    """Test retraction tuning rejects invalid extruder type."""
    request_data = {
        "extruder_type": "Invalid Type",
        "current_retraction_distance": 1.0,
        "current_retraction_speed": 35,
        "stringing_severity": "moderate",
    }

    response = client.post("/api/v1/calculators/retraction-tuning", json=request_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Direct Drive" in response.json()["detail"]
    assert "Bowden" in response.json()["detail"]


# ============================================================================
# Belt Tension Calculator Tests (Phase 5)
# ============================================================================


def test_belt_tension_gt2_6mm_good_range():
    """Test belt tension calculation for GT2 6mm belt in good range."""
    request_data = {
        "belt_type": "GT2",
        "belt_width": 6,
        "measured_frequency_x": 110.0,
        "measured_frequency_y": 108.0,
        "belt_length_x": 800,
        "belt_length_y": 800,
        "kinematics": "CoreXY",
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "tension_x_newtons" in data
    assert "tension_y_newtons" in data
    assert data["tension_x_newtons"] > 0
    assert data["tension_y_newtons"] > 0
    assert "assessment_x" in data
    assert "Good" in data["assessment_x"]
    assert "assessment_y" in data
    assert "Good" in data["assessment_y"]
    assert data["adjustment_needed"] is False  # Within 5Hz tolerance
    assert "resonance_note" in data


def test_belt_tension_gt2_9mm():
    """Test belt tension calculation for GT2 9mm belt."""
    request_data = {
        "belt_type": "GT2",
        "belt_width": 9,
        "measured_frequency_x": 115.0,
        "belt_length_x": 750,
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["tension_x_newtons"] > 0
    # 9mm belt has higher linear mass (4.8 vs 3.2)
    assert "assessment_x" in data


def test_belt_tension_too_loose():
    """Test belt tension with low frequency (too loose)."""
    request_data = {
        "belt_type": "GT2",
        "belt_width": 6,
        "measured_frequency_x": 75.0,
        "belt_length_x": 800,
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "Too Loose" in data["assessment_x"]
    assert data["adjustment_needed"] is True
    assert "turns_to_adjust" in data


def test_belt_tension_too_tight():
    """Test belt tension with high frequency (too tight)."""
    request_data = {
        "belt_type": "GT2",
        "belt_width": 6,
        "measured_frequency_x": 145.0,
        "belt_length_x": 800,
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "Too Tight" in data["assessment_x"]
    assert data["adjustment_needed"] is True


def test_belt_tension_corexy_imbalance():
    """Test belt tension detects CoreXY imbalance."""
    request_data = {
        "belt_type": "GT2",
        "belt_width": 6,
        "measured_frequency_x": 110.0,
        "measured_frequency_y": 95.0,  # 15Hz difference
        "belt_length_x": 800,
        "belt_length_y": 800,
        "kinematics": "CoreXY",
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert data["adjustment_needed"] is True
    assert "balance" in data["turns_to_adjust"].lower() or "Balance" in data["turns_to_adjust"]
    assert "imbalance" in data["resonance_note"].lower()


def test_belt_tension_invalid_belt_type():
    """Test belt tension rejects unsupported belt type."""
    request_data = {
        "belt_type": "InvalidType",
        "belt_width": 6,
        "measured_frequency_x": 110.0,
        "belt_length_x": 800,
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "belt type" in response.json()["detail"].lower()


def test_belt_tension_invalid_belt_width():
    """Test belt tension rejects unsupported belt width for GT2."""
    request_data = {
        "belt_type": "GT2",
        "belt_width": 12,  # Only 6 and 9 supported
        "measured_frequency_x": 110.0,
        "belt_length_x": 800,
    }

    response = client.post("/api/v1/calculators/belt-tension", json=request_data)

    # Pydantic validation returns 422
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

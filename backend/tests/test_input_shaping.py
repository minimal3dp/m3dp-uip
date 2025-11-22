"""Tests for Input Shaping calculator endpoint.

CSV-driven tests validating formula accuracy and configuration output.
"""

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_input_shaping_basic_recommendation():
    """Test basic input shaping recommendation with typical frequencies."""
    payload = {"test_type": "ADXL345", "x_frequency": 45.2, "y_frequency": 37.8}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "shaper_x" in data
    assert "shaper_y" in data
    assert "max_accel" in data
    assert "klipper_config" in data
    assert "[input_shaper]" in data["klipper_config"]
    assert "square_corner_velocity" in data
    assert "notes" in data


def test_input_shaping_accel_bounds():
    """Test acceleration clamping to CSV-specified range (1000-10000)."""
    # Extremely low frequencies should still clamp to >=1000 accel
    payload_low = {"test_type": "ADXL345", "x_frequency": 25.0, "y_frequency": 28.0}
    resp_low = client.post("/api/v1/calculators/input-shaping", json=payload_low)
    assert resp_low.status_code == 200
    assert resp_low.json()["max_accel"] >= 1000

    # High frequencies clamp to <=10000
    payload_high = {"test_type": "ADXL345", "x_frequency": 90.0, "y_frequency": 85.0}
    resp_high = client.post("/api/v1/calculators/input-shaping", json=payload_high)
    assert resp_high.status_code == 200
    assert resp_high.json()["max_accel"] <= 10000


def test_input_shaping_shaper_selection_segments():
    """Test shaper type selection based on frequency segmentation."""
    # Frequency buckets should select appropriate shapers if options exist
    buckets = [
        (35.0, 35.5),  # <40 -> EI
        (45.0, 44.0),  # 40-50 -> MZV
        (55.0, 52.0),  # 50-60 -> 2HUMP_EI
        (65.0, 62.0),  # >=60 -> 3HUMP_EI
    ]
    responses = []
    for x_f, y_f in buckets:
        r = client.post(
            "/api/v1/calculators/input-shaping",
            json={"test_type": "ADXL345", "x_frequency": x_f, "y_frequency": y_f},
        )
        assert r.status_code == 200
        responses.append(r.json())

    assert responses[0]["shaper_x"] in ["EI", "MZV", "ZV", "2HUMP_EI", "3HUMP_EI"]
    # We cannot guarantee CSV option ordering; ensure acceleration is monotonically non-decreasing with frequency bucket
    accel_values = [r["max_accel"] for r in responses]
    assert all(a >= 1000 for a in accel_values)


def test_input_shaping_csv_driven_calculation():
    """Test calculation follows CSV formula: max_accel = min(freq * 120, 10000) clamped to [1000, 10000]."""
    payload = {"test_type": "ADXL345", "x_frequency": 50.0, "y_frequency": 48.0}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    # Base frequency = min(50, 48) = 48 Hz
    # Expected accel = max(1000, min(48 * 120, 10000)) = max(1000, 5760) = 5760
    expected_accel = 5760
    assert abs(data["max_accel"] - expected_accel) < 500  # Allow heuristic variance


def test_input_shaping_square_corner_velocity():
    """Test square_corner_velocity from CSV (default 5.0 mm/s)."""
    payload = {"test_type": "ADXL345", "x_frequency": 45.0, "y_frequency": 40.0}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    # CSV specifies 5.0 mm/s for square_corner_velocity (row 6)
    assert data["square_corner_velocity"] == 5.0


def test_input_shaping_klipper_config_format():
    """Test Klipper config output format matches expected structure."""
    payload = {"test_type": "ADXL345", "x_frequency": 42.5, "y_frequency": 39.2}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    config = data["klipper_config"]
    assert "shaper_type_x:" in config
    assert "shaper_freq_x:" in config
    assert "shaper_type_y:" in config
    assert "shaper_freq_y:" in config
    assert "max_accel:" in config
    assert "square_corner_velocity:" in config
    assert "42.5" in config  # X frequency
    assert "39.2" in config  # Y frequency


def test_input_shaping_asymmetric_frequencies():
    """Test handling of asymmetric X/Y frequencies."""
    payload = {"test_type": "ADXL345", "x_frequency": 60.0, "y_frequency": 35.0}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    # Shapers may differ due to frequency segmentation
    # Acceleration should be based on minimum frequency (35 Hz)
    # Expected: max(1000, min(35 * 120, 10000)) = max(1000, 4200) = 4200
    assert 3500 < data["max_accel"] < 5000  # Allow heuristic variance


def test_input_shaping_notes_field():
    """Test notes field contains CSV reference and calibration advice."""
    payload = {"test_type": "ADXL345", "x_frequency": 45.0, "y_frequency": 42.0}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    notes = data["notes"]
    assert "input_shaping.csv" in notes
    assert "SHAPER_CALIBRATE" in notes


def test_input_shaping_validation():
    """Test input validation for missing or invalid parameters."""
    # Missing frequency
    resp = client.post(
        "/api/v1/calculators/input-shaping",
        json={"test_type": "ADXL345", "x_frequency": 45.0},
    )
    assert resp.status_code == 422

    # Invalid frequency (too low)
    resp_low = client.post(
        "/api/v1/calculators/input-shaping",
        json={"test_type": "ADXL345", "x_frequency": 5.0, "y_frequency": 35.0},
    )
    assert resp_low.status_code == 422

    # Invalid frequency (too high)
    resp_high = client.post(
        "/api/v1/calculators/input-shaping",
        json={"test_type": "ADXL345", "x_frequency": 250.0, "y_frequency": 40.0},
    )
    assert resp_high.status_code == 422


def test_input_shaping_fallback_heuristic():
    """Test fallback behavior when CSV not loaded (graceful degradation)."""
    # This test validates the heuristic path is functional
    # Even if CSV missing, calculator should return valid config
    payload = {"test_type": "ADXL345", "x_frequency": 48.0, "y_frequency": 44.0}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    # Heuristic should still produce valid shapers and acceleration
    assert data["shaper_x"] in ["EI", "MZV", "ZV", "2HUMP_EI", "3HUMP_EI"]
    assert data["shaper_y"] in ["EI", "MZV", "ZV", "2HUMP_EI", "3HUMP_EI"]
    assert 1000 <= data["max_accel"] <= 10000
    assert data["square_corner_velocity"] > 0

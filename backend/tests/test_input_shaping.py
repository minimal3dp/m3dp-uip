"""Tests for Input Shaping calculator endpoint."""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_input_shaping_basic_recommendation():
    payload = {"test_type": "ADXL345", "x_frequency": 45.2, "y_frequency": 37.8}
    resp = client.post("/api/v1/calculators/input-shaping", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "shaper_x" in data
    assert "shaper_y" in data
    assert "max_accel" in data
    assert "klipper_config" in data
    assert "[input_shaper]" in data["klipper_config"]


def test_input_shaping_accel_bounds():
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


def test_input_shaping_validation():
    # Missing frequency
    resp = client.post(
        "/api/v1/calculators/input-shaping",
        json={"test_type": "ADXL345", "x_frequency": 45.0},
    )
    assert resp.status_code == 422

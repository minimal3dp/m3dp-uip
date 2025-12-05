"""Additional tests to improve coverage for calculator endpoints.

Focus:
- Input Shaping fallback path when CSV missing (df is None)
- Input Shaping default option parsing when Notes absent
- Malformed input_shaping.csv handling (insufficient rows)
"""

from unittest.mock import patch

import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.mark.parametrize("x,y", [(35.0, 42.0), (55.0, 65.0)])
def test_input_shaping_fallback(x, y):
    """Test heuristic fallback when CSV loader returns None."""
    with patch("app.services.csv_loader.CSVLoader.get_input_shaping_data", return_value=None):
        resp = client.post(
            "/api/v1/calculators/input-shaping",
            json={"test_type": "ADXL345", "x_frequency": x, "y_frequency": y},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "klipper_config" in data
        # Ensure shaper types selected from heuristic set
        assert data["shaper_x"] in {"EI", "MZV", "2HUMP_EI", "3HUMP_EI"}
        assert data["shaper_y"] in {"EI", "MZV", "2HUMP_EI", "3HUMP_EI"}


def test_input_shaping_missing_notes_defaults():
    """Test default shaper options applied when Notes column missing/invalid."""
    # Build minimal DataFrame with required row indexes but no Notes content
    import pandas as pd

    rows = []
    # Indices 0-6 expected; fill with empty dicts except formula row
    for i in range(7):
        rows.append({"Parameter": f"Row{i}", "Notes": None, "Formula": 5.0 if i == 6 else None})
    df = pd.DataFrame(rows)

    with patch("app.services.csv_loader.CSVLoader.get_input_shaping_data", return_value=df):
        resp = client.post(
            "/api/v1/calculators/input-shaping",
            json={"test_type": "ADXL345", "x_frequency": 52.3, "y_frequency": 47.8},
        )
        assert resp.status_code == 200
        data = resp.json()
        # Should fall back to default list first element 'MZV'
        assert data["shaper_x"] in {"MZV", "ZV", "EI", "2HUMP_EI", "3HUMP_EI"}
        assert data["square_corner_velocity"] == 5.0


def test_input_shaping_malformed_csv_raises():
    """Test that malformed CSV (insufficient rows) raises during processing."""
    import pandas as pd

    # Provide only two rows so iloc[3] triggers exception
    df = pd.DataFrame(
        [
            {"Parameter": "Test Type", "Notes": "Options: MZV"},
            {"Parameter": "X Freq", "Notes": "Options: EI"},
        ]
    )

    with patch("app.services.csv_loader.CSVLoader.get_input_shaping_data", return_value=df):
        resp = client.post(
            "/api/v1/calculators/input-shaping",
            json={"test_type": "ADXL345", "x_frequency": 42.0, "y_frequency": 38.0},
        )
        assert resp.status_code == 500
        detail = resp.json().get("detail", "")
        assert detail == "Malformed input_shaping.csv"

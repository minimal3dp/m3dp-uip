import httpx
import pytest
from app.main import app


def _client():
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_rotation_distance_basic():
    async with _client() as client:
        payload = {
            "current_rotation_distance": 33.5,
            "requested_extrusion": 100.0,
            "actual_extrusion": 98.5,
        }
        resp = await client.post("/api/v1/calculators/rotation-distance", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "new_rotation_distance" in data
    assert "klipper_config" in data
    assert data["klipper_config"].startswith("rotation_distance:")
    assert round(data["new_rotation_distance"], 3) == round((33.5 * 98.5) / 100, 3)


@pytest.mark.asyncio
async def test_rotation_distance_tolerance_flag():
    async with _client() as client:
        payload = {
            "current_rotation_distance": 33.5,
            "requested_extrusion": 100.0,
            "actual_extrusion": 90.0,
        }
        resp = await client.post("/api/v1/calculators/rotation-distance", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["within_tolerance"] is False
    assert "⚠️" in data["recommendation"]

import httpx
import pytest
from app.main import app


def _client():
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_root():
    async with _client() as client:
        resp = await client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"
    assert "calculators" in data
    assert "csv_loaded" in data
    assert isinstance(data["calculators"], list)


@pytest.mark.asyncio
async def test_health():
    async with _client() as client:
        resp = await client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"
    assert "csv_loaded" in data
    assert "csv_count" in data

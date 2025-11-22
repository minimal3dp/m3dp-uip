import httpx
import pytest
from app.main import app


def _client():
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_quick_classify_endpoint():
    async with _client() as client:
        payload = {"query": "Stringing on PLA due to humidity", "printer_model": "Ender 3"}
        resp = await client.post("/api/v1/diagnosis/classify", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["issue_type"] in {"material", "slicer", "mechanical"}
    assert "matches" in data
    assert data["match_count"] == len(data["matches"])  # consistency


@pytest.mark.asyncio
async def test_analyze_text_primary_path():
    async with _client() as client:
        payload = {"query": "Retraction causing blobs", "slicer": "OrcaSlicer"}
        resp = await client.post("/api/v1/diagnosis/analyze/text", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "issue_type" in data
    assert "classification" in data
    assert "recommendations" in data
    assert "handler" in data


@pytest.mark.asyncio
async def test_analyze_text_fallback_path(monkeypatch):
    """Force router service failure to exercise fallback classification."""
    from app.services import router_service

    async def failing(*_ignore, **_ignore_kw):  # noqa: D401
        raise RuntimeError("Forced failure for test")

    monkeypatch.setattr(
        router_service.get_router_service().__class__, "diagnose_from_text", failing
    )

    async with _client() as client:
        payload = {"query": "Belt slipping causing layer shift"}
        resp = await client.post("/api/v1/diagnosis/analyze/text", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["handler"] == "fallback_csv_router"
    assert data["confidence"] <= 0.6
    assert data["classification"] == data["issue_type"]

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_csv_validation_endpoint():
    resp = client.get("/api/v1/diagnosis/csv-validation")
    assert resp.status_code == 200
    data = resp.json()
    assert "csv_loaded" in data
    assert "loaded_files" in data
    assert isinstance(data["loaded_files"], list)
    assert "validation_errors" in data
    assert "has_errors" in data
    # Even if there are errors, structure should be dict
    assert isinstance(data["validation_errors"], dict)

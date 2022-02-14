from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"API": "BAS", "version": "0.1"}

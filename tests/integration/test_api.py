from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_hello_returns_200():
    response = client.get("/api/hello")
    assert response.status_code == 200

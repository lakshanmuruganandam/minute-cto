
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Minute CTO is ready to architect your startup."}

def test_generate_architecture():
    response = client.post("/api/v1/architecture/generate", json={"product_description": "A social network for dogs", "target_users": 1000})
    assert response.status_code == 200
    assert "architecture" in response.json()

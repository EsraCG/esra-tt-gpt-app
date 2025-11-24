from fastapi.testclient import TestClient
from src.api.main import app 

client = TestClient(app)

def test_ask_endpoint():
    response = client.posts("/ask", json={"prompt":"What is FastAPI?"})
    assert response.status_code == 200
    assert "FastAPI" in response.json()["response"]
    
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_obtener_pokemones():
    response = client.get("/")
    assert response.status_code == 200
    assert len(response.json()) == 5

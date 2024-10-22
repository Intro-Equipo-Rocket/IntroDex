from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_team_id_existe():
    response = client.get("/equipos/id/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["nombre"] == "Equipo 1"
    
    
def test_team_id_inexistente():
    response = client.get("/equipos/id/111")
    assert response.status_code == 404

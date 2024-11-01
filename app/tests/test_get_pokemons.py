from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_obtener_pokemones():
    response = client.get("/pokemons")
    pokemones_json = response.json()
    
    assert response.status_code == 200
    assert pokemones_json

    for pokemon in pokemones_json:
        assert "id" in pokemon
        assert "nombre" in pokemon


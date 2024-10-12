from fastapi.testclient import TestClient
from app.main import app
from app.model_pokemon_id import pokemones

client = TestClient(app)


def test_borrar_pokemon_existente() -> None:
    response = client.delete("/pokemon/delete/25")
    assert response.status_code == 200
    assert len(pokemones) == 6


def test_borrar_pokemon_no_existente() -> None:
    response = client.delete("/pokemon/delete/0")
    assert response.status_code == 404

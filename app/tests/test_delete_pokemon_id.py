from fastapi.testclient import TestClient
from app.main import app
from app.db.pokemons_db import pokemones

client = TestClient(app)


def test_borrar_pokemon_existente() -> None:
    response = client.delete("/pokemons/delete/25")
    assert response.status_code == 200
    assert len(pokemones) == 1


def test_borrar_pokemon_no_existente() -> None:
    response = client.delete("/pokemons/delete/0")
    assert response.status_code == 404

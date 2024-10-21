from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_pokemon_id_existente() -> None:
    response = client.get("/pokemons/id/25")
    assert response.status_code == 200
    assert response.json()["id"] == 25


def test_obtener_pokemon_nombre_existente() -> None:
    response = client.get("/pokemons/nombre/greninja")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Greninja"


def test_pokemon_id_no_existe() -> None:
    response = client.get(
        "/pokemons/id/7777777",
    )
    assert response.status_code == 404


def test_pokemon_nombre_no_existe() -> None:
    response = client.get(
        "/pokemons/nombre/zzz",
    )
    assert response.status_code == 404


def test_detalles_pokemon_id_existente() -> None:
    response = client.get("/pokemons/id/658")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Greninja"
    assert response.json()["tipos"][0] == 11
    assert response.json()["habilidades"][0] == 67
    assert (
        response.json()["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png"
    )


def test_detalles_pokemon_nombre_existente() -> None:
    response = client.get("/pokemons/nombre/greninja")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Greninja"
    assert response.json()["tipos"][0] == 11
    assert response.json()["habilidades"][0] == 67
    assert (
        response.json()["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png"
    )
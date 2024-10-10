from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_pokemon_id() -> None:
    response = client.get("/pokemon_id/25")
    assert response.status_code == 200
    assert response.json()["id"] == 25


def test_pokemon_no_existe() -> None:
    response = client.get(
        "/pokemon_id/7777777",
    )
    assert response.status_code == 404


def test_detalles_pokemon() -> None:
    response = client.get("/pokemon_id/658")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Greninja"
    assert response.json()["tipo_principal"] == "Agua"
    assert response.json()["habilidad_1"] == "Torrente"
    assert (
        response.json()["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png"
    )

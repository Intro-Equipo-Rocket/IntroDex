from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_movimiento_id_existente() -> None:
    response = client.get("/moves/id/813")
    assert response.status_code == 200
    assert response.json()["id"] == 813


def test_obtener_movimiento_nombre_existente() -> None:
    response = client.get("/moves/name/triple-axel")
    assert response.status_code == 200
    assert response.json()["nombre"] == "triple-axel"


def test_movimiento_id_no_existe() -> None:
    response = client.get(
        "/moves/id/7777777",
    )
    assert response.status_code == 404


def test_movimiento_nombre_no_existe() -> None:
    response = client.get(
        "/moves/name/andkjadkjah",
    )
    assert response.status_code == 404


def test_detalles_movimiento_id() -> None:
    response = client.get("/moves/id/813")
    assert response.status_code == 200
    assert response.json()["nombre"] == "triple-axel"
    assert response.json()["tipo"] == "Ice"
    assert response.json()["categoria"] == "Physical"
    assert (
        response.json()["efecto"]
        == "Inflicts regular damage with no additional effect."
    )
    assert (
        response.json()["pokemones_aprenden_tms"][0]["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"
    )


def test_detalles_movimiento_nombre() -> None:
    response = client.get("/moves/name/triple-axel")
    assert response.status_code == 200
    assert response.json()["nombre"] == "triple-axel"
    assert response.json()["tipo"] == "Ice"
    assert response.json()["categoria"] == "Physical"
    assert (
        response.json()["efecto"]
        == "Inflicts regular damage with no additional effect."
    )
    assert (
        response.json()["pokemones_aprenden_tms"][0]["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"
    )

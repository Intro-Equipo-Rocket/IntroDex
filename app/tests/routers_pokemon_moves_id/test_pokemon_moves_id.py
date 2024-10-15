from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_movimiento_id_existente() -> None:
    response = client.get("/movimientos/id/813")
    assert response.status_code == 200
    assert response.json()["id"] == 813


def test_obtener_movimiento_nombre_existente() -> None:
    response = client.get("/movimientos/nombre/triple-axel")
    assert response.status_code == 200
    assert response.json()["nombre"] == "triple-axel"


def test_movimiento_id_no_existe() -> None:
    response = client.get(
        "/movimientos/id/7777777",
    )
    assert response.status_code == 404


def test_movimiento_nombre_no_existe() -> None:
    response = client.get(
        "/movimientos/nombre/andkjadkjah",
    )
    assert response.status_code == 404


def test_detalles_movimiento_id() -> None:
    response = client.get("/movimientos/id/813")
    assert response.status_code == 200
    assert response.json()["nombre"] == "triple-axel"
    assert response.json()["tipo"] == 15
    assert response.json()["categoria"] == 2
    assert response.json()["efecto"] == 1
    assert (
        response.json()["pokemones_aprenden_tms"][0]["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"
    )


def test_detalles_movimiento_nombre() -> None:
    response = client.get("/movimientos/nombre/triple-axel")
    assert response.status_code == 200
    assert response.json()["nombre"] == "triple-axel"
    assert response.json()["tipo"] == 15
    assert response.json()["categoria"] == 2
    assert response.json()["efecto"] == 1
    assert (
        response.json()["pokemones_aprenden_tms"][0]["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"
    )

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_movimiento_id_pokemons_existente() -> None:
    response = client.get("/movimientos/813/pokemon")
    assert response.status_code == 200
    assert response.json()["id"] == 813


def test_movimiento_id_pokemons_no_existe() -> None:
    response = client.get("/movimientos/8888888888/pokemon")
    assert response.status_code == 404


def test_detalles_nulos_movimiento_id_pokemons() -> None:
    response = client.get("/movimientos/813/pokemon")
    assert response.status_code == 200
    assert response.json()["nombre"] == None
    assert response.json()["tipo"] == None
    assert response.json()["categoria"] == None
    assert response.json()["potencia"] == None
    assert response.json()["precision"] == None
    assert response.json()["usos"] == None
    assert response.json()["generacion"] == None
    assert response.json()["efecto"] == None

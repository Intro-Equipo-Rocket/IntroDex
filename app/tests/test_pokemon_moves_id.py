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
    response = client.get("/movimientos/id/7777777")
    assert response.status_code == 404


def test_movimiento_nombre_no_existe() -> None:
    response = client.get("/movimientos/nombre/andkjadkjah")
    assert response.status_code == 404

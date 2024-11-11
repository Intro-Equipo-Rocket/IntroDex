from fastapi.testclient import TestClient
from app.main import app

from app.modelos import *

client = TestClient(app)


def test_obtener_movimiento_id_existente() -> None:
    response = client.get("/movimientos/id/144")
    assert response.status_code == 200


def test_obtener_movimiento_nombre_existente() -> None:
    response = client.get("/movimientos/nombre/Transformación")
    assert response.status_code == 200


def test_no_existe_movimiento() -> None:
    response = client.get("/movimientos/id/9999999999999999")
    assert response.status_code == 404

    response = client.get("/movimientos/nombre/dadafgadasdafasd")
    assert response.status_code == 404


def test_verificar_datos_por_movimiento_id_existente() -> None:
    response = client.get("/movimientos/id/144")
    assert response.json()["nombre"] == "Transformación"


def test_verificar_datos_por_nombre_existente() -> None:
    response = client.get("/movimientos/nombre/Transformación")
    assert response.json()["id"] == 144

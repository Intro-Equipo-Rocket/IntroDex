from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_movimiento_id_existente() -> None:
    response = client.get("/movimientos/id/813")
    assert response.status_code == 200
    assert response.json()["id"] == 813


def test_obtener_movimiento_nombre_existente() -> None:
    response = client.get("/movimientos/nombre/thunderbolt")
    assert response.status_code == 200
    assert response.json()["nombre"] == "thunderbolt"


def test_movimiento_id_no_existe() -> None:
    response = client.get("/movimientos/id/7777777")
    assert response.status_code == 404


def test_movimiento_nombre_no_existe() -> None:
    response = client.get("/movimientos/nombre/andkjadkjah")
    assert response.status_code == 404


def test_detalles_movimiento_id() -> None:
    response = client.get("/movimientos/id/85")
    assert response.status_code == 200
    assert response.json()["pokemones_aprenden_evolucionar"] == None
    ["pokemones_aprenden_subir_nivel"] == None
    ["pokemones_aprenden_grupo_huevo"] == None
    ["pokemones_aprenden_tms"] == None


def test_detalles_movimiento_nombre() -> None:
    response = client.get("/movimientos/nombre/thunderbolt")
    assert response.status_code == 200
    assert response.json()["pokemones_aprenden_evolucionar"] == None
    ["pokemones_aprenden_subir_nivel"] == None
    ["pokemones_aprenden_grupo_huevo"] == None
    ["pokemones_aprenden_tms"] == None

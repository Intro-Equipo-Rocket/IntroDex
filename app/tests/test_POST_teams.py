from fastapi.testclient import TestClient
from app.main import app
from app.db.equipos_db import equipos

client = TestClient(app)

def test_crear_equipo_sin_pokemones() -> None:
    response = client.post("/equipos/?id_equipo=997&nombre_equipo=equipo_prueba&generacion_equipo=8")
    assert response.status_code == 201
    assert response.json()["id"] == 997
    assert response.json()["nombre"] == "equipo_prueba"

def test_crear_equipo_con_id_existente() -> None:
    response = client.post("/equipos/?id_equipo=997&nombre_equipo=nuevo_equipo_prueba&generacion_equipo=8")
    assert response.status_code == 400
    assert response.json() == {"detail": "Ese equipo ya existe"}
    equipos.pop()

def test_crear_equipo_con_generacion_erronea() -> None:
    response = client.post("/equipos/?id_equipo=2&nombre_equipo=equipo_prueba&generacion_equipo=9")
    assert response.status_code == 400
    assert response.json() == {"detail": "La generación del equipo no es válida"}

def test_crear_equipo_con_pokemones_movimientos_naturaleza_y_evs() -> None:
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&id_naturaleza_1=1",
                           json={"movimientos_pkm_1": [84,85,25,87], "evs_pkm_1": {"vida": 10, "ataque": 10, "defensa": 10, "ataque_especial": 10, "defensa_especial": 10, "velocidad": 10}})
    assert response.status_code == 201
    assert response.json()["id"] == 1111
    assert response.json()["nombre"] == "equipo_prueba"
    assert response.json()["pokemones"][0]["naturaleza"]["id"] == 1
    assert response.json()["pokemones"][0]["movimientos"] == [84,85,25,87]
    assert response.json()["pokemones"][0]["evs"] == {"vida": 10, "ataque": 10, "defensa": 10, "ataque_especial": 10, "defensa_especial": 10, "velocidad": 10}
    equipos.pop()

def test_crear_equipo_con_pokemon_no_existente() -> None:
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=7777&id_naturaleza_1=1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokemon no encontrado o ya eliminado."}

def test_crear_equipo_con_pokemon_fuera_de_generacion() -> None:
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=1&id_pkm_1=658&id_naturaleza_1=1") # Greninja no es de la generacion 1
    assert response.status_code == 400
    assert response.json() == {"detail": "El pokemon de id 658 no pertenece a la generacion del equipo"}

def test_crear_equipo_con_movimientos_inexistentes_no_aprendidos_o_fuera_de_rango() -> None:
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&&id_naturaleza_1=1&movimientos_pkm_1=[7777]") # Movimiento no existente
    assert response.status_code == 400
    assert response.json() == {"detail": "Algun movimiento del pokemon de id 25 no son validos o no tiene movimientos"}
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&id_naturaleza_1=1",
                           json={"movimientos_pkm_1":[813]}) # Pikachu no aprende Triple Axel
    assert response.status_code == 400
    assert response.json() == {"detail": "Algun movimiento del pokemon de id 25 no son validos o no tiene movimientos"}
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&id_naturaleza_1=1",
                           json={"movimientos_pkm_1":[84,85,25,87,113]}) # Todos los movimientos son validos pero son mas de 4
    assert response.status_code == 400
    assert response.json() == {"detail": "Algun movimiento del pokemon de id 25 no son validos o no tiene movimientos"}

def test_crear_equipo_con_naturaleza_inexistente_o_sin_naturaleza() -> None:
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&id_naturaleza_1=7777")
    print(response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "Naturaleza no encontrada."}
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25")
    assert response.status_code == 404
    assert response.json() == {"detail": "Naturaleza no encontrada."}

def test_crear_equipo_con_evs_incorrectos() -> None:
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&id_naturaleza_1=1",
                           json={"movimientos_pkm_1": [84,85,25,87], "evs_pkm_1": {"vida": -1, "ataque": 10, "defensa": 10, "ataque_especial": 10, "defensa_especial": 10, "velocidad": 10}})
    assert response.status_code == 400
    assert response.json() == {"detail":"Los EVs no son validos, asegurarse de que la suma de los EVs no sea mayor a 510 y que cada EV no sea mayor a 255"}
    response = client.post("/equipos/?id_equipo=1111&nombre_equipo=equipo_prueba&generacion_equipo=8&id_pkm_1=25&id_naturaleza_1=1",
                           json={"movimientos_pkm_1": [84,85,25,87], "evs_pkm_1": {"vida": 100, "ataque": 100, "defensa": 100, "ataque_especial": 100, "defensa_especial": 100, "velocidad": 100}}) # Suma de EVs mayor a 510
    assert response.status_code == 400
    assert response.json() == {"detail":"Los EVs no son validos, asegurarse de que la suma de los EVs no sea mayor a 510 y que cada EV no sea mayor a 255"}
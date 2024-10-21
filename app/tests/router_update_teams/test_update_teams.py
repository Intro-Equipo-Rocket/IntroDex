from fastapi.testclient import TestClient
from app.main import app

test = TestClient(app)

def test_editar_equipo_exitoso():
    nuevo_equipo = {
        "id": 1,
        "nombre": 'Equipo nuevo',
        "pokemones": [{
            "pokemon": {
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
                "id": 1,
                "nombre": "Ivysaur",
                "tipos": [12, 4],
                "habilidades": [65],
                "habilidad_oculta": 34,
                "vida": 45,
                "ataque": 49,
                "defensa": 49,
                "ataque_especial": 65,
                "defensa_especial": 65,
                "velocidad": 45,
                "total": 318,
                "movimientos_aprendibles_evolucion": [],
                "movimientos_aprendibles_nivel": [],
                "movimientos_aprendibles_tms": [],
                "movimientos_aprendibles_huevo": [],
                "debilidades_tipo": [],
                "generacion": 1,
                "altura": 10,  # Altura en decímetros
                "peso": 130,  # Peso en hectogramos
                "grupo_huevo": ["Monster", "Grass"]
            },
            "movimientos": [],
            "naturaleza": {
                "id": 1,
                "nombre": "Fuerte",
                "stat_perjudicada_id": 2,
                "stat_mejorada_id": 2
            },
            "evs": {
                "vida": 255,
                "ataque": 255,
                "defensa": 0,
                "ataque_especial": 0,
                "defensa_especial": 0,
                "velocidad": 0
            }
        }],
        "generacion": 1
    }

    test_1 = test.put("/equipos/1", json=nuevo_equipo)
    
    assert test_1.status_code == 200
    assert test_1.json()["nombre"] == "Equipo nuevo"
    assert test_1.json()["pokemones"][0]["pokemon"]["nombre"] == "ivasaur"

def test_editar_equipo_no_encontrado():
    nuevo_equipo = {
        "id": 2,
        "nombre": 'Equipo no existente',
        "pokemones": [],  
        "generacion": 1
    }

    test_2 = test.put("/equipos/2", json=nuevo_equipo)
    
    assert test_2.status_code == 404
    assert test_2.json()["detail"] == "El equipo a cambiar no fue encontrado"
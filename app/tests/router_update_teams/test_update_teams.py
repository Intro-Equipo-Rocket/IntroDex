from fastapi.testclient import TestClient
from app.main import app

test = TestClient(app)

def test_editar_equipo_exitoso():
    nuevo_equipo = {
  "id": 1,
  "nombre": "equipo prueba",
  "pokemones": [
    {
      "pokemon": {
        "imagen": "string",
        "id": 27,
        "nombre": "pruebamon",
        "tipos": [
          0
        ],
        "altura": 0,
        "peso": 0,
        "habilidades": [
          0
        ],
        "habilidad_oculta": 0,
        "grupo_huevo": [
          0
        ],
        "vida": 0,
        "ataque": 0,
        "defensa": 0,
        "ataque_especial": 0,
        "defensa_especial": 0,
        "velocidad": 0,
        "total": 0,
        "evoluciones": [
          0
        ],
        "imagenes_evoluciones": [
          "string"
        ],
        "movimientos_aprendibles_nivel": [
          0
        ],
        "movimientos_aprendibles_evolucion": [
          0
        ],
        "movimientos_aprendibles_tms": [
          0
        ],
        "movimientos_aprendibles_huevo": [
          0
        ],
        "debilidades_tipo": [
          0
        ],
        "generacion": 0
      },
      "movimientos": [
        0
      ],
      "naturaleza": {
        "id": 0,
        "nombre": "string",
        "stat_perjudicada_id": 0,
        "stat_mejorada_id": 0
      },
      "evs": {
        "vida": 0,
        "ataque": 0,
        "defensa": 0,
        "ataque_especial": 0,
        "defensa_especial": 0,
        "velocidad": 0
      }
    }
  ],
  "generacion": 0
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
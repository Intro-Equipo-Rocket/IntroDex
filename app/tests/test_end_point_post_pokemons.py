from app.main import app
from fastapi.testclient import TestClient
from app.routers.pokemon import *

client = TestClient(app)

pokemon_prueba = Pokemon(
        imagen="string",
        id=26,
        nombre="string",
        tipos=[0],
        altura=0,
        peso=0,
        habilidades=[0],
        habilidad_oculta=0,
        grupo_huevo=[0],
        vida=0,
        ataque=0,
        defensa=0,
        ataque_especial=0,
        defensa_especial=0,
        velocidad=0,
        total=0,
        evoluciones=[0],
        imagenes_evoluciones=[],
        movimientos_aprendibles_nivel=[0],
        movimientos_aprendibles_evolucion=[0],
        movimientos_aprendibles_tms=[0],
        movimientos_aprendibles_huevo=[0],
        debilidades_tipo=[0],      
    )
   
def test_crear_pokemon_existente():
    response = client.post("/pokemons", json=pokemones[0].dict())
    assert response.status_code == 400
    assert len(pokemones) == 2
    
def test_crear_pokemon_nuevo():
    response = client.post("/pokemons", json=pokemon_prueba.dict())
    assert response.status_code == 201
    assert len(pokemones) == 3
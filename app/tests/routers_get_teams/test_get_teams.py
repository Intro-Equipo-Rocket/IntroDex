from fastapi.testclient import TestClient
from app.main import app

test = TestClient(app)

def test_obtener_equipos_pagina_1():
    pagina = 1
    test_1 = test.get(f"/equipos/pagina/{pagina}?pagina={pagina}&cantidad_pokemons=10")
    assert test_1.status_code == 200
    assert len(test_1.json()) == 10

def test_obtener_equipos_pagina_sin_equipos():
    pagina = 4
    test_2 = test.get(f"/equipos/pagina/{pagina}?pagina={pagina}&cantidad_pokemons=10")
    assert test_2.status_code == 404
    assert test_2.json() == {'detail': 'No se encontraron equipos para esta página'} 

def test_pagina_invalida():
    pagina = 0
    test_3 = test.get(f"/equipos/pagina/{pagina}?pagina={pagina}&cantidad_pokemons=10")
    assert test_3.status_code == 404
    assert test_3.json() == {'detail': 'Algunos de los parámetros están siendo mal introducidas'}

def test_cantidad_olvidada():
    cantidad = 0
    test_4 = test.get(f"/equipos/pagina/{pagina}?pagina=1&cantidad_pokemons={cantidad}")
    assert test_4.status_code == 404
    assert test_4.json() == {'detail': 'Algunos de los parámetros están siendo mal introducidas'}

from fastapi.testclient import TestClient
from app.main import app
from app.db.pokemons_db import pokemones

client = TestClient(app)

def test_obtener_movimientos_del_pkm() -> None:
    pokemon = pokemones[0]
    response = client.get(f"/pokemons/{pokemon.id}/movimientos")
    assert response.status_code == 200
    assert response.json() != []

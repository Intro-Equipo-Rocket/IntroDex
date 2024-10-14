from fastapi import FastAPI

from app.routers.main import api_router_get_pokemon_moves_id


app = FastAPI()
app.include_router(api_router_get_pokemon_moves_id)

<<<<<<< HEAD
=======
app.include_router(pokemon.router, preffix='/pokemons', tags=['Pokemons'])
app.include_router(movimientos.router, preffix='/movimientos', tags=['Movimientos'])
app.include_router(equipos.router, prefix='/equipos', tags=['Equipos'])
>>>>>>> parte_1

@app.get("/")
def root():
<<<<<<< HEAD
    return {"mensaje": "Bienvenido a la API de pokemon del Equipo Rocket!"}
=======
    return {'mensaje': 'Bienvenido a la API de pokemon del Equipo Rocket!'}
>>>>>>> parte_1

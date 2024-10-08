from fastapi import FastAPI
from .routers import pokemon, movimientos, equipos

app = FastAPI()

app.include_router(pokemon.router, preffix='/pokemons', tags=['Pokemons'])
app.include_router(movimientos.router, preffix='/movimientos', tags=['Movimienos'])
app.include_router(equipos.router, prefix='/equipos', tags=['Equipos'])

@app.get('/')
def root():
    return {'message': 'Bienvenido a la API de pokemon del Equipo Rocket!'}
from fastapi import FastAPI

from app.routers import pokemon, movimientos, equipos


app = FastAPI()


app.include_router(pokemon.router, prefix='/pokemons', tags=['Pokemons'])
app.include_router(movimientos.router, prefix='/movimientos', tags=['Movimientos'])
app.include_router(equipos.router, prefix='/equipos', tags=['Equipos'])

@app.get("/")
def root():
    return {'mensaje': 'Bienvenido a la API de pokemon del Equipo Rocket!'}

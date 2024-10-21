from fastapi import FastAPI
from .routers import pokemon, movimientos, equipos, naturalezas

app = FastAPI()


app.include_router(pokemon.router, prefix='/pokemons', tags=['Pokemons'])
app.include_router(movimientos.router, prefix='/movimientos', tags=['Movimientos'])
app.include_router(equipos.router, prefix='/equipos', tags=['Equipos'])
app.include_router(naturalezas.router, prefix="/naturalezas", tags=["Naturaleza"])


@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de pokemon del Equipo Rocket!"}

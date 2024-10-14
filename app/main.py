from fastapi import FastAPI

from app.routers.main import api_router_get_pokemon_moves_id


app = FastAPI()
app.include_router(api_router_get_pokemon_moves_id)


@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de pokemon del Equipo Rocket!"}

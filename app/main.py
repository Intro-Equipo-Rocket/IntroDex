from fastapi import FastAPI
from app.routers.main import api_router_post_pokemon

app = FastAPI()
app.include_router(api_router_post_pokemon)


@app.get("/")
def root():
    return {"message": "Bienvenido a la API de pokemon del Equipo Rocket!"}

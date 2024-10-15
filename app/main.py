from fastapi import FastAPI
from app.routers.main import get_naturalezas_router

app = FastAPI()

app.include_router(get_naturalezas_router)

@app.get('/')
def root():
    return {'mensaje': 'Bienvenido a la API de pokemon del Equipo Rocket!'}
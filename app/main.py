from fastapi import FastAPI

from app.routers.main import api_router


app = FastAPI()
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Bienvenido a la API de pokemon del Equipo Rocket!"}

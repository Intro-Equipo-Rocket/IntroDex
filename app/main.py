from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Bienvenido a la API de pokemon del Equipo Rocket!"}

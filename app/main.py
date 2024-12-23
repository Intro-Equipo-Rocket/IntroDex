import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Engine
from sqlmodel import Session, select
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from .routers import pokemon, movimientos, equipos, naturalezas
from .database import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


# Make sure that the connection to the DB can be made. If not, exit gracefully.
@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init(db_engine: Engine) -> None:
    try:
        with Session(db_engine) as session:
            # Try to create session to check if DB is awake
            session.exec(select(1))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init(engine)
    logger.info("Service finished initializing")


app = FastAPI()

# Lista de orígenes permitidos
origins = [
    "http://localhost:5173",
     "http://localhost",
]

# Agregar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(pokemon.router, prefix="/pokemons", tags=["Pokemons"])
app.include_router(movimientos.router, prefix="/movimientos", tags=["Movimientos"])
app.include_router(equipos.router, prefix="/equipos", tags=["Equipos"])
app.include_router(naturalezas.router, prefix="/naturalezas", tags=["Naturaleza"])


@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de pokemon del Equipo Rocket!"}

main()

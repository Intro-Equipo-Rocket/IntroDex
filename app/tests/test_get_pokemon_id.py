import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from typing import Generator

from app.modelos import (
    Pokemon,
    Tipos,
    TiposPokemon,
    Habilidades,
    HabilidadesPokemon,
    GrupoHuevo,
    GrupoHuevoPokemon,
    StatsDelPokemon,
    Movimientos,
    MovimientosPokemon,
    PokemonPublic,
)
from app.main import app
from app.database import get_session


@pytest.fixture(name="engine")
def engine_fixture():
    return create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )


@pytest.fixture(name="session")
def session_fixture(engine: create_engine) -> Generator[Session, None, None]:
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session) -> Generator[TestClient, None, None]:
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


def test_get_pokemon_por_id(session: Session, client: TestClient) -> None:
    # Crear tipos de ejemplo
    tipo_agua = Tipos(id=11, nombre="Agua")
    tipo_siniestro = Tipos(id=17, nombre="Siniestro")
    session.add(tipo_agua)
    session.add(tipo_siniestro)
    session.commit()

    # Asociaciones de tipos con el Pokémon
    tipos_pokemon = [
        TiposPokemon(type_id=11, pokemon_id=1),
        TiposPokemon(type_id=17, pokemon_id=1),
    ]
    session.add_all(tipos_pokemon)
    session.commit()

    # Crear el Pokémon de prueba
    pokemon_test = Pokemon(
        id=0,
        nombre="pruebamon",
        imagen="https://example.com/pruebamon.png",
        altura=999,
        peso=1,
        especie=25,
        generacion=99,
        id_evolucion=None,
        imagen_evolucion="https://example.com/pruebamon_evolucion.png",
        tipos=tipos_pokemon,
        habilidades=[],
        grupo_huevo=[],
        stats=[],
        movimientos=[],
    )
    session.add(pokemon_test)
    session.commit()

    # Realizar la solicitud GET al endpoint
    response = client.get("/nombre/pruebamon")
    assert response.status_code == 200
    data = response.json()

    # Validar la estructura de la respuesta
    assert data["nombre"] == "pruebamon"
    assert data["imagen"] == "https://example.com/pruebamon.png"
    assert data["altura"] == 999
    assert data["peso"] == 1
    assert data["generacion"] == 99
    assert data["id_evolucion"] is None
    assert data["imagen_evolucion"] == "https://example.com/pruebamon_evolucion.png"
    assert len(data["tipos"]) == 2
    assert data["tipos"][0]["id"] == 11
    assert data["tipos"][0]["nombre"] == "Agua"
    assert data["tipos"][1]["id"] == 17
    assert data["tipos"][1]["nombre"] == "Siniestro"
    # Puedes añadir más aserciones para otras relaciones si es necesario

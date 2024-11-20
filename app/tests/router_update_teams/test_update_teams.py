from fastapi.testclient import TestClient
from app.modelos import Equipo
from app.main import app
from app.database import get_session
from sqlmodel import SQLModel, Session, create_engine
import pytest

DATABASE_URL = "sqlite:///./test_1.db"
engine = create_engine(DATABASE_URL, echo=True)

@pytest.fixture(scope="module")
def setup_db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add_all([
            Equipo(id=1, nombre="Equipo Rocket", generacion=1),
            Equipo(id=2, nombre="Equipo Aqua", generacion=3),
        ])
        session.commit()
    yield
    SQLModel.metadata.drop_all(engine)

@pytest.fixture
def client():
    def override_get_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session
    yield TestClient(app)
    app.dependency_overrides.clear()

def test_editar_equipo_exitoso(client, setup_db):
    equipo_nuevo = Equipo(id=1, nombre="Equipo Plasma", generacion=4)
    response = client.put(f'/equipos/{equipo_nuevo.id}', json=equipo_nuevo.model_dump())

    assert response.status_code == 200
    assert response.json()["nombre"] == "Equipo Plasma"

def test_editar_equipo_no_encontrado(client, setup_db):
    equipo_nuevo = Equipo(id=7, nombre="Equipo Plasma", generacion=4)
    response = client.put(f'/equipos/{equipo_nuevo.id}', json=equipo_nuevo.model_dump())

    assert response.status_code == 404
    assert response.json() == {"detail": "El equipo a cambiar no existe"}
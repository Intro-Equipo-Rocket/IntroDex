from fastapi.testclient import TestClient
from app.modelos import Equipo
from app.main import app
from app.database import get_session
from sqlmodel import SQLModel, Session, create_engine
import pytest

DATABASE_URL = "sqlite:///./test_2.db"
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

def test_eliminar_equipo_existente(client, setup_db):
    equipo_id = 1
    pagina = client.delete(f'/equipos/{equipo_id}')

    assert pagina.status_code == 200
    assert pagina.json() == {'mensaje': f'El equipo con id {equipo_id} ha sido eliminado'}

def test_eliminar_equipo_inexistente(client, setup_db):
    equipo_id = 55
    pagina = client.delete(f'/equipos/{equipo_id}')

    assert pagina.status_code == 404
    assert pagina.json() == {'detail': f'El equipo con id {equipo_id} no ha sido encontrado'}

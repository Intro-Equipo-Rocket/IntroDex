from fastapi.testclient import TestClient
from app.main import app
from app.db.equipos_db import equipos

client_test = TestClient(app)

def test_eliminar_equipo_existente():
    equipo_id = 1
    pagina = client_test.delete(f'/equipos/{equipo_id}')

    assert pagina.status_code == 200
    assert pagina.json() == {'mensaje': f'El equipo (Equipo 1) con id ({equipo_id}) ha sido eliminado.'}
    assert not any(equipo['id'] == equipo_id for equipo in equipos)

def test_eliminar_equipo_inexistente():
    equipo_id = 55
    pagina = client_test.delete(f'/equipos/{equipo_id}')

    assert pagina.status_code == 404
    assert pagina.json() == {'detail': f'No se ha encontrado al equipo con id ({equipo_id}).'}

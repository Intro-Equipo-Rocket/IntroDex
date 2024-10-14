from fastapi import APIRouter
from app.modelos import *
<<<<<<< HEAD
from app.db import *
=======
from app.db.equipos_db import *
>>>>>>> parte_1

router = APIRouter()

@router.get('/naturalezas')
def obtener_naruralezas():
    pass

@router.get('/')
def obtener_equipos():
    pass

@router.post('/')
def crear_equipo(equipo: Equipo):
    pass

@router.put('/{equipo_id}')
def editar_equipo(equipo_id: int, equipo_nuevo: Equipo):
    pass

@router.get('/{equipo_id}')
def obtener_equipo_por_id(equipo_id: int):
    pass

@router.delete('/{equipo_id}')
def eliminar_equipo(equipo_id: int):
    pass
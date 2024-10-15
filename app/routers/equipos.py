from fastapi import APIRouter, HTTPException
from app.modelos import *
from app.db.equipos_db import *

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
    for i, equipo in enumerate(equipos_db):
        if equipo.id == equipo_id:
            equipo_eliminado = equipos_db.pop(i)
            return {'mensaje': f"El equipo ({equipo_eliminado.nombre}) con id ({equipo_id}) ha sido eliminado."}
        
    raise HTTPException(status_code=404, detail=f'No se ha encontrado al equipo con id ({equipo_id}).')
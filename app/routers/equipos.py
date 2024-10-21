from fastapi import APIRouter, HTTPException
from app.modelos import *
from app.db.equipos_db import *

router = APIRouter()


@router.get("/naturalezas")
def obtener_naruralezas():
    pass


@router.get("/")
def obtener_equipos():
    pass


@router.post("/")
def crear_equipo(equipo: Equipo):
    pass


@router.put("/{equipo_id}")
def editar_equipo(equipo_id: int, equipo_nuevo: Equipo):
    for equipo in equipos_db:
        if equipo.id == equipo_id:
            equipo.nombre = equipo_nuevo.nombre
            equipo.pokemones = equipo_nuevo.pokemones
            equipo.generacion = equipo_nuevo.generacion

            return equipo
            
    raise HTTPException(status_code=404, detail="El equipo a cambiar no fue encontrado")


@router.get("/{equipo_id}")
def obtener_equipo_por_id(equipo_id: int):
    pass


@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int):
    pass

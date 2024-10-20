from fastapi import APIRouter, HTTPException
from app.modelos import *
from app.db.equipos_db import *
from typing import List

router = APIRouter()


@router.get("/naturalezas")
def obtener_naruralezas():
    pass


@router.get("/", response_model=List[Equipo])
def obtener_equipos(pagina: int, cantidad_pokemons: int = 10):
    if not pagina >= 1 or not cantidad_pokemons >= 1:
        raise HTTPException(status_code=404, detail="Algunos de los parámetros están siendo mal introducidas")
    
    skip = (pagina - 1) * 10
    equipos_pagina = equipos_db[skip:skip + cantidad_pokemons]

    if not equipos_pagina:
        raise HTTPException(status_code=404, detail="No se encontraron equipos para esta página")
    
    return equipos_pagina


@router.post("/")
def crear_equipo(equipo: Equipo):
    pass


@router.put("/{equipo_id}")
def editar_equipo(equipo_id: int, equipo_nuevo: Equipo):
    pass


@router.get("/{equipo_id}")
def obtener_equipo_por_id(equipo_id: int):
    pass


@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int):
    pass

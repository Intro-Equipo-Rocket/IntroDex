from fastapi import APIRouter, HTTPException, status
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
    equipos_pagina = equipos[skip:skip + cantidad_pokemons]

    if not equipos_pagina:
        raise HTTPException(status_code=404, detail="No se encontraron equipos para esta página")
    
    return equipos_pagina


@router.post("/")
def crear_equipo(equipo: Equipo):
    pass


@router.put("/{equipo_id}")
def editar_equipo(equipo_id: int, equipo_nuevo: Equipo):
    pass


@router.get("/id/{equipo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def obtener_equipo_por_id(equipo_id: int) -> Equipo:
    for equipo in equipos:
        if equipo.id == equipo_id:
            return equipo
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND, detail="Id de equipo inexistente"
    )

            
    
@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int):
    for i, equipo in enumerate(equipos):
        if equipo.id == equipo_id:
            equipo_eliminado = equipos.pop(i)
            return {'mensaje': f"El equipo ({equipo_eliminado.nombre}) con id ({equipo_id}) ha sido eliminado."}
        
    raise HTTPException(status_code=404, detail=f'No se ha encontrado al equipo con id ({equipo_id}).')

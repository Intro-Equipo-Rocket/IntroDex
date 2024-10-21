from fastapi import APIRouter, HTTPException, status
from app.modelos import Movimiento, Error
from app.db.movimientos_db import *

router = APIRouter()


@router.get("/{id}/pokemon", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Movimientos:
    for move in Moves:
        if move.id == id:
            move.nombre = None
            move.tipo = None
            move.categoria = None
            move.potencia = None
            move.precision = None
            move.usos = None
            move.generacion = None
            move.efecto = None
            return move

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )


@router.get("/id/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_movimiento(id: int) -> Movimiento:
    for move in Moves:
        if move.id == id:
            move.pokemones_aprenden_evolucionar = None
            move.pokemones_aprenden_subir_nivel = None
            move.pokemones_aprenden_grupo_huevo = None
            move.pokemones_aprenden_tms = None
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )


@router.get("/nombre/{nombre}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_movimiento(nombre: str) -> Movimiento:
    for move in Moves:
        if move.nombre.lower() == nombre.lower():
            move.pokemones_aprenden_evolucionar = None
            move.pokemones_aprenden_subir_nivel = None
            move.pokemones_aprenden_grupo_huevo = None
            move.pokemones_aprenden_tms = None
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )
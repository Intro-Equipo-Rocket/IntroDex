from fastapi import APIRouter, HTTPException, status
from app.modelos import Movimiento, Error
from app.db.movimientos_db import *

router = APIRouter()


@router.get("/id/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Movimiento:
    for move in Moves:
        if move.id == id:
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )


@router.get("/nombre/{nombre}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(nombre: str) -> Movimiento:
    for move in Moves:
        if move.nombre.lower() == nombre.lower():
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )


@router.get("/{movimiento_id}/pokemons")
def obtener_pokemons_por_movimiento(movimiento_id: int):
    pass

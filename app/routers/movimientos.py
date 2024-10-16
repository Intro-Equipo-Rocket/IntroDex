from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from app.db.movimientos_db import *

router = APIRouter()


@router.get("/{movimiento_id}")
def obtener_movimiento_por_id(movimiento_id: int):
    pass


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

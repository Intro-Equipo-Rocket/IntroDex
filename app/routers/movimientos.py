from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from sqlmodel import select
from app.database import SessionDep

router = APIRouter()


@router.get("/{id}/pokemon", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Movimiento:
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


@router.get(
    "/id/{move_id}",
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    response_model=MovimientosPublic,
)
def show_por_id(session: SessionDep, move_id: int) -> MovimientosPublic:
    movimiento = session.exec(
        select(Movimientos).where(Movimientos.id == move_id)
    ).first()

    if not movimiento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
        )

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )


@router.get(
    "/nombre/{nombre}",
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    response_model=MovimientosPublic,
)
def show_por_id(session: SessionDep, nombre: str) -> MovimientosPublic:
    movimiento = session.exec(
        select(Movimientos).where(Movimientos.nombre == nombre)
    ).first()

    if not movimiento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
        )

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from app.modelos import Movimiento, Error
from app.db.movimientos_db import *
from app.database import SessionDep

router = APIRouter()


@router.get("/{id}/pokemon", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(session: SessionDep, id: int):
    # query = select(Movimiento).where(Movimiento.id == id)
    # movimiento = session.exec(query).first()
    # if not movimiento:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    #     )
    # return {"nombre": move.nombre, "pokemones": move.pokemones_aprenden_evolucionar + move.pokemones_aprenden_subir_nivel + move.pokemones_aprenden_grupo_huevo + move.pokemones_aprenden_tms}
    for move in Moves:
        if move.id == id:
            return {"nombre": move.nombre, "pokemones": move.pokemones_aprenden_evolucionar + move.pokemones_aprenden_subir_nivel + move.pokemones_aprenden_grupo_huevo + move.pokemones_aprenden_tms}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )


@router.get("/id/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_movimiento(session: SessionDep, id: int) -> Movimiento:
    # query = select(Movimiento).where(Movimiento.id == id)
    # movimiento = session.exec(query).first()
    # if not movimiento:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    #     )
    # return movimiento
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
def get_movimiento(session: SessionDep, nombre: str) -> Movimiento:
    # query = select(Movimiento).where(Movimiento.nombre == nombre)
    # movimiento = session.exec(query).first()
    # if not movimiento:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    #     )
    # return movimiento
    for move in Moves:
        if move.nombre == nombre:
            move.pokemones_aprenden_evolucionar = None
            move.pokemones_aprenden_subir_nivel = None
            move.pokemones_aprenden_grupo_huevo = None
            move.pokemones_aprenden_tms = None
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )

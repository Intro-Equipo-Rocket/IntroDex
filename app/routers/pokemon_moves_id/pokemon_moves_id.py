from fastapi import HTTPException, status, APIRouter
from app.model_pokemon_moves_id import Move, Error, Moves


router = APIRouter()


@router.get("/id/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Move:
    for move in Moves:
        if move.id == id:
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )


@router.get("/name/{nombre}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(nombre: str) -> Move:
    for move in Moves:
        if move.nombre.lower() == nombre.lower():
            return move
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
    )

from fastapi import APIRouter, HTTPException, status
from app.modelos import Naturaleza
from app.db.naturalezas_db import naturalezas

router = APIRouter()

@router.get("/", response_model=list[Naturaleza])
def obtener_naturalezas() -> list[Naturaleza]:
    if not naturalezas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Naturalezas no encontradas"
        )
    return naturalezas
from fastapi import APIRouter, HTTPException, status
from app.modelos import Naturaleza
from app.db.naturaleza_db import naturalezas
# from sqlmodel import Session, select
# from app.database import SessionDep

router = APIRouter()

@router.get("/", response_model=list[Naturaleza])
def obtener_naturalezas() -> list[Naturaleza]:  # def obtener_naturalezas(session: SessionDep):
    # query = select(Naturaleza)
    # naturalezas = session.exec(query).all()
    # if not naturalezas:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="Naturalezas no encontradas"
    #     )
    # return naturalezas
    if not naturalezas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Naturalezas no encontradas"
        )
    return naturalezas
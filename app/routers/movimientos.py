from fastapi import APIRouter
from app.modelos import *
<<<<<<< HEAD
from app.db import *
=======
from app.db.movimientos_db import *
>>>>>>> parte_1

router = APIRouter()

@router.get('/{movimiento_id}')
def obtener_movimiento_por_id(movimiento_id: int):
    pass

@router.get('/{movimiento_id}/pokemons')
def obtener_pokemons_por_movimiento(movimiento_id: int):
    pass
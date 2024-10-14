from fastapi import APIRouter
from app.modelos import *
<<<<<<< HEAD
from app.db import *
=======
from app.db.pokemons_db import *
>>>>>>> parte_1

router = APIRouter()

@router.get('/', response_model=list[Pokemon])
def obtener_pokemons():
    pass

@router.get('/{pokemon_id}')
def obtener_pokemon_por_id(pokemon_id: int):
    pass

@router.post('/')
def crear_pokemon(nuevo_pokemon: Pokemon):
    pass

@router.delete('/{pokemon_id}')
def eliminar_pokemon_por_id(pokemon_id: int):
    pass

@router.get('/{pokemon_id}/movimientos')
def obtener_movimientos_del_pokemon(pokemon_id: int):
    pass
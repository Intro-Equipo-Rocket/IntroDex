from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from app.db.pokemons_db import *

router = APIRouter()


@router.get("/", response_model=list[Pokemon])
def obtener_pokemons():
    pass


@router.get("/{pokemon_id}")
def obtener_pokemon_por_id(pokemon_id: int):
    pass


@router.post("/")
def crear_pokemon(nuevo_pokemon: Pokemon):
    pass


@router.delete("/delete/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Pokemon:
    pokemon = buscar_pokemon(id)
    pokemones.remove(pokemon)
    return pokemon


def buscar_pokemon(id: int) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pokemon no encontrado o ya eliminado.",
    )


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_del_pokemon(pokemon_id: int):
    pass

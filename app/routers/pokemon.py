from fastapi import APIRouter, HTTPException, status
from app.modelos import Pokemon, Error
from app.db.pokemons_db import *

router = APIRouter()


@router.get("/", response_model=list[Pokemon])
def obtener_pokemons():
    pass


@router.get("/id/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    )


@router.get("/nombre/{nombre}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(nombre: str) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    )


@router.post("/")
def crear_pokemon(nuevo_pokemon: Pokemon):
    pass


@router.delete("/{pokemon_id}")
def eliminar_pokemon_por_id(pokemon_id: int):
    pass


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_del_pokemon(pokemon_id: int):
    pass

from fastapi import HTTPException, status, APIRouter
from app.modelos import *
from app.db.pokemons_db import *

router = APIRouter()


@router.get("/", response_model=list[Pokemon])
def obtener_pokemones() -> list[Pokemon]:
    if not pokemones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay pokemones disponibles",
        )
    return pokemones



@router.get("/{pokemon_id}")
def obtener_pokemon_por_id(pokemon_id: int):
    pass


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(nuevo_pokemon: Pokemon):
    for pokemon in pokemones:
        if nuevo_pokemon.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Ese pokemon ya existe"
            )
    pokemones.append(nuevo_pokemon)
    return nuevo_pokemon


@router.delete("/{pokemon_id}")
def eliminar_pokemon_por_id(pokemon_id: int):
    pass


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_del_pokemon(pokemon_id: int):
    pass

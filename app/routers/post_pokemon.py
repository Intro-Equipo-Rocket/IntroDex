from fastapi import APIRouter, HTTPException, status
from app.pokemon import Pokemon
from app.db import pokemones

router = APIRouter()


@router.post("/create/{nuevo_pokemon}", status_code=status.HTTP_201_CREATED)
def crear_pokemon(nuevo_pokemon: Pokemon):
    for pokemon in pokemones:
        if nuevo_pokemon.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Ese pokemon ya existe"
            )
        else:
            pokemones.append(nuevo_pokemon)
    return pokemon

from fastapi import HTTPException, status, APIRouter
from model_pokemon_id import Pokemon, Error, pokemones

router = APIRouter()


@router.get("/")
def list() -> list[Pokemon]:
    return pokemones


@router.get("/{id}", responses={404: {"model": Error}})
def get_pokemon(id: int) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(status_code=404, detail="Pokemon not found")

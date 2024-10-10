from fastapi import HTTPException, status, APIRouter
from app.model_pokemon_id import Pokemon, Error, pokemones

router = APIRouter()


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    )

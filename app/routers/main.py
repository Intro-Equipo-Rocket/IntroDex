from fastapi import APIRouter

from app.routers.pokemon_moves_id import pokemon_moves_id

api_router_get_pokemon_moves_id = APIRouter()
api_router_get_pokemon_moves_id.include_router(
    pokemon_moves_id.router, prefix="/moves", tags=["Moves"]
)

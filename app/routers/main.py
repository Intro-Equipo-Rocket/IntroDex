from fastapi import APIRouter

from app.routers.pokemon_id import pokemon_id

api_router_get_pokemon_id = APIRouter()
api_router_get_pokemon_id.include_router(
    pokemon_id.router, prefix="/pokemon", tags=["Pokemon"]
)

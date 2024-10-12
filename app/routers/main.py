from fastapi import APIRouter

from app.routers.delete_pokemon_id import delete_pokemon_id

api_router_delete_pokemon_id = APIRouter()
api_router_delete_pokemon_id.include_router(
    delete_pokemon_id.router, prefix="/pokemon/delete", tags=["Pokemon"]
)

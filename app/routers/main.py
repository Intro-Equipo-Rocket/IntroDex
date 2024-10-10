from fastapi import APIRouter

from routers.pokemon_id import pokemon_id

api_router = APIRouter()
api_router.include_router(pokemon_id.router, prefix="/pokemon_id", tags=["Pokemon"])

from fastapi import APIRouter

from app.routers import pokemones

api_router_get_pokemones = APIRouter()
api_router_get_pokemones.include_router(
    pokemones.router, prefix="/pokemon", tags=["Pokemon"]
)

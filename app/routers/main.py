from fastapi import APIRouter
from app.routers import post_pokemon

api_router_post_pokemon = APIRouter()
api_router_post_pokemon.include_router(
    post_pokemon.router, prefix="/pokemon", tags=["Pokemon"]
)

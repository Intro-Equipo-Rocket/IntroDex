from fastapi import APIRouter
from app.routers import naturalezas

get_naturalezas_router = APIRouter()

get_naturalezas_router.include_router(
    naturalezas.router,
    prefix="/naturalezas",
    tags=["Naturaleza"]
)
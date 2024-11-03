from fastapi import APIRouter, HTTPException, status
from app.modelos import Pokemon, Error, Movimiento
from app.db.pokemons_db import *
from app.db.movimientos_db import *
from sqlmodel import Session, select
from app.database import SessionDep

router = APIRouter()


@router.get("/", response_model=list[Pokemon])
def obtener_pokemones(session: SessionDep) -> list[Pokemon]:
    # query = select(Pokemon)
    # pokemones = session.exec(query)
    if not pokemones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay pokemones disponibles",
        )
    return pokemones


@router.get("/id/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(session: SessionDep, id: int) -> Pokemon:
    # query = select(Pokemon).where(Pokemon.id == id)
    # pokemon = session.exec(query).first()
    # if not pokemon:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    #     )
    # return pokemon
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    )


@router.get("/nombre/{nombre}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(session: SessionDep, nombre: str) -> Pokemon:
    # query = select(Pokemon).where(Pokemon.nombre.lower() == nombre.lower())
    # pokemon = session.exec(query).first()
    # if not pokemon:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    #     )
    # return pokemon
    for pokemon in pokemones:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(session: SessionDep, nuevo_pokemon: Pokemon):
    # query = select(Pokemon).where(Pokemon.id == nuevo_pokemon.id)
    # pokemon = session.exec(query).first()
    # if pokemon:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail="Ese pokemon ya existe"
    #     )
    # session.add(nuevo_pokemon)
    # session.commit()
    # session.refresh(nuevo_pokemon)
    for pokemon in pokemones:
        if nuevo_pokemon.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Ese pokemon ya existe"
            )
    pokemones.append(nuevo_pokemon)
    return nuevo_pokemon


@router.delete("/delete/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(session: SessionDep, id: int) -> Pokemon:
    # query = select(Pokemon).where(Pokemon.id == id)
    # pokemon = session.exec(query).first()
    # if not pokemon:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    #     )
    # session.delete(pokemon)
    # session.commit()
    # return pokemon
    pokemon = buscar_pokemon(id)
    pokemones.remove(pokemon)
    return pokemon

def buscar_pokemon(session: SessionDep, id: int) -> Pokemon:
    # query = select(Pokemon).where(Pokemon.id == id)
    # pokemon = session.exec(query).first()
    # if not pokemon:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    #     )
    # return pokemon
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pokemon no encontrado o ya eliminado.",
    )

@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_del_pokemon(session: SessionDep, pokemon_id: int) -> list[Movimiento]:
    # query = select(Pokemon).where(Pokemon.id == pokemon_id)
    # pokemon = session.exec(query).first()
    # if not pokemon:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    #     )
    # movim_pkm = []
    # for id_movim_del_pkm in (pokemon.movimientos_aprendibles_evolucion
    #                         + pokemon.movimientos_aprendibles_huevo
    #                         + pokemon.movimientos_aprendibles_nivel
    #                         + pokemon.movimientos_aprendibles_tms):
    #     query = select(Movimiento).where(Movimiento.id == id_movim_del_pkm)
    #     movim = session.exec(query).first()
    #     movim_pkm.append(movim)
    # return movim_pkm
    pokemon = buscar_pokemon(pokemon_id)
    movim_pkm = []
    for id_movim_del_pkm in (pokemon.movimientos_aprendibles_evolucion 
                            + pokemon.movimientos_aprendibles_huevo
                            + pokemon.movimientos_aprendibles_nivel
                            + pokemon.movimientos_aprendibles_tms):
        for movimientos in Moves:
            if id_movim_del_pkm == movimientos.id:
                movim_pkm.append(movimientos)
    return movim_pkm
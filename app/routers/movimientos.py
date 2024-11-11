from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from sqlmodel import select
from app.database import SessionDep
from typing import List

router = APIRouter()


@router.get(
    "/{id}/pokemon",
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    response_model=List[PokemonPublic],
)
def show_por_id(session: SessionDep, move_id: int) -> List[PokemonPublic]:
    verificar_move_id(move_id, session)
    movimientos_pokemon = session.exec(
        select(MovimientosPokemon).where(MovimientosPokemon.move_id == move_id)
    ).all()

    pokemones = []

    for movimiento_pokemon in movimientos_pokemon:
        pokemon = session.exec(
            select(Pokemon).where(Pokemon.id == movimiento_pokemon.pokemon_id)
        ).first()

        if pokemon:
            tipos = session.exec(
                select(Tipos)
                .join(TiposPokemon)
                .where(TiposPokemon.pokemon_id == pokemon.id)
            ).all()

            habilidades = session.exec(
                select(Habilidades)
                .join(HabilidadesPokemon)
                .where(HabilidadesPokemon.pokemon_id == pokemon.id)
            ).all()

            grupo_huevo = session.exec(
                select(GrupoHuevo)
                .join(GrupoHuevoPokemon)
                .where(GrupoHuevoPokemon.species_id == pokemon.especie)
            ).all()

            stats = session.exec(
                select(StatsDelPokemon).where(StatsDelPokemon.pokemon_id == pokemon.id)
            ).all()

            movimientos = None  # movimientos == None porque solo nos interesa los datos del pokemon.

            pokemon_public = PokemonPublic(
                nombre=pokemon.nombre,
                imagen=pokemon.imagen,
                altura=pokemon.altura,
                peso=pokemon.peso,
                generacion=pokemon.generacion,
                id_evolucion=pokemon.id_evolucion,
                imagen_evolucion=pokemon.imagen_evolucion,
                tipos=tipos,
                habilidades=habilidades,
                grupo_huevo=grupo_huevo,
                stats=stats,
                movimientos=movimientos,
            )

            pokemones.append(pokemon_public)

    if not pokemones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Pokémon were found that learn that movement through pre-established methods",
        )

    return pokemones


def verificar_move_id(move_id: int, session: SessionDep) -> bool:
    movimiento = session.exec(
        select(Movimientos).where(Movimientos.id == move_id)
    ).first()
    if not movimiento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimiento no encontrado.",
        )
    return True

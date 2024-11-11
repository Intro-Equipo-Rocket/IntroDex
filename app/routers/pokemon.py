from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from sqlmodel import select
from app.database import SessionDep

router = APIRouter()


@router.get("/", response_model=list[PokemonPublic])
def get_pokemons(session: SessionDep) -> list[PokemonPublic]:
    pokemons = session.exec(select(Pokemon)).all()

    if not pokemons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Pokémon found"
        )

    pokemons_public = []
    for pokemon in pokemons:
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

        movimientos = session.exec(
            select(Movimientos)
            .join(MovimientosPokemon)
            .where(MovimientosPokemon.pokemon_id == pokemon.id)
        ).all()

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
        pokemons_public.append(pokemon_public)

    return pokemons_public


@router.get("/nombre/{nombre}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(nombre: str) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
    )


@router.get(
    "/id/{pokemon_id}",
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    response_model=PokemonPublic,
)
def show_por_id(session: SessionDep, pokemon_id: int) -> PokemonPublic:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == pokemon_id)).first()

    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found"
        )

    tipos = session.exec(
        select(Tipos).join(TiposPokemon).where(TiposPokemon.pokemon_id == pokemon.id)
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

    grupo_huevo = session.exec(
        select(GrupoHuevo)
        .join(GrupoHuevoPokemon)
        .where(GrupoHuevoPokemon.species_id == pokemon.especie)
    ).all()

    stats = session.exec(
        select(StatsDelPokemon).where(StatsDelPokemon.pokemon_id == pokemon.id)
    ).all()

    movimientos = session.exec(
        select(Movimientos)
        .join(MovimientosPokemon)
        .where(MovimientosPokemon.pokemon_id == pokemon.id)
    ).all()

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

    if pokemon_public:
        return pokemon_public
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found"
    )


@router.get(
    "/nombre/{nombre}",
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    response_model=PokemonPublic,
)
def show_por_name(session: SessionDep, nombre: str) -> PokemonPublic:
    pokemon = session.exec(
        select(Pokemon).where(Pokemon.nombre == nombre.lower())
    ).first()

    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Pokemon not exist"
        )

    tipos = session.exec(
        select(Tipos).join(TiposPokemon).where(TiposPokemon.pokemon_id == pokemon.id)
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

    grupo_huevo = session.exec(
        select(GrupoHuevo)
        .join(GrupoHuevoPokemon)
        .where(GrupoHuevoPokemon.species_id == pokemon.especie)
    ).all()

    stats = session.exec(
        select(StatsDelPokemon).where(StatsDelPokemon.pokemon_id == pokemon.id)
    ).all()

    movimientos = session.exec(
        select(Movimientos)
        .join(MovimientosPokemon)
        .where(MovimientosPokemon.pokemon_id == pokemon.id)
    ).all()

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

    if pokemon_public:
        return pokemon_public
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found"
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(nuevo_pokemon: Pokemon):
    for pokemon in pokemones:
        if nuevo_pokemon.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Ese pokemon ya existe"
            )
    pokemones.append(nuevo_pokemon)
    return nuevo_pokemon


@router.delete("/delete/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def get_pokemon(id: int) -> Pokemon:
    pokemon = buscar_pokemon(id)
    pokemones.remove(pokemon)
    return pokemon


def buscar_pokemon(id: int) -> Pokemon:
    for pokemon in pokemones:
        if pokemon.id == id:
            return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pokemon no encontrado o ya eliminado.",
    )


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_del_pokemon(pokemon_id: int) -> list[Movimiento]:
    pokemon = buscar_pokemon(pokemon_id)
    movim_pkm = []
    for id_movim_del_pkm in (
        pokemon.movimientos_aprendibles_evolucion
        + pokemon.movimientos_aprendibles_huevo
        + pokemon.movimientos_aprendibles_nivel
        + pokemon.movimientos_aprendibles_tms
    ):
        for movimientos in Moves:
            if id_movim_del_pkm == movimientos.id:
                movim_pkm.append(movimientos)
    return movim_pkm

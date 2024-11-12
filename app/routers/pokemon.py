from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from sqlmodel import select
from app.database import SessionDep

router = APIRouter()


@router.get("/", response_model=list[Pokemon])
def obtener_pokemones() -> list[Pokemon]:
    if not pokemones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay pokemones disponibles",
        )
    return pokemones


@router.get("/", response_model=list[Pokemon])
def obtener_pokemones() -> list[Pokemon]:
    if not pokemones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay pokemones disponibles",
        )
    return pokemones


@router.get(
    "/id/{pokemon_id}",
    responses={status.HTTP_404_NOT_FOUND: {"model": Error}},
    response_model=PokemonPublic,
)
def show_pokemon_por_id(session: SessionDep, pokemon_id: int) -> PokemonPublic:
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
def show_pokemon_por_name(session: SessionDep, nombre: str) -> PokemonPublic:
    pokemon = session.exec(
        select(Pokemon).where(Pokemon.nombre == nombre.lower())
    ).first()

    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not exist"
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


@router.get("/{pokemon_id}/movimientos", response_model=list[MovimientosPokemonPublic])
def obtener_movimientos_del_pokemon(
    pokemon_id: int, session: SessionDep
) -> list[MovimientosPokemon]:
    verificar_pkm(pokemon_id, session)
    pokemon_movimientos = session.exec(
        select(MovimientosPokemon).where(MovimientosPokemon.pokemon_id == pokemon_id)
    ).all()
    if not pokemon_movimientos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El pokemon no tiene movimientos.",
        )
    for pokemon_movimiento in pokemon_movimientos:
        pokemon_movimiento.movimientos = session.exec(
            select(Movimientos).where(Movimientos.id == pokemon_movimiento.move_id)
        ).first()
        pokemon_movimiento.movimientos.class_tipo = session.exec(
            select(Tipos).where(Tipos.id == pokemon_movimiento.movimientos.tipo)
        ).first()
        pokemon_movimiento.movimientos.class_categoria = session.exec(
            select(CategoriaMovimiento)
            .join(Movimientos)
            .where(CategoriaMovimiento.id == pokemon_movimiento.movimientos.categoria)
        ).first()
        pokemon_movimiento.movimientos.class_efecto = session.exec(
            select(EfectoMovimiento)
            .join(Movimientos)
            .where(EfectoMovimiento.id == pokemon_movimiento.movimientos.efecto)
        ).first()
        pokemon_movimiento.metodo = session.exec(
            select(MetodoAprenderMovimiento).where(
                MetodoAprenderMovimiento.pokemon_move_method_id
                == pokemon_movimiento.id_metodo
            )
        ).first()
    return pokemon_movimientos


def verificar_pkm(pokemon_id: int, session: SessionDep) -> bool:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == pokemon_id)).first()
    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pokemon no encontrado.",
        )
    return True

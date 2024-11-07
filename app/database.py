from collections.abc import Generator
import logging
from typing import Annotated
import csv

from fastapi import Depends
from sqlmodel import create_engine, select, Session

from app.modelos import Pokemon, Movimiento, PreViewPokemon, Naturaleza


SQLITE_FILE_PATH = "data/database.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

logger = logging.getLogger(__name__)


def seed():
    with Session(engine) as session:
        # Do no seed if there's data present in the DB
        if session.exec(select(pokemones)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(pokemones)

        session.commit()

        logger.info("Seeds loaded on Db")


def organizar_datos_por_id(data, id_key):
    data_por_id = {}
    for fila in data:
        key = int(fila[id_key])
        if key not in data_por_id:
            data_por_id[key] = []
        data_por_id[key].append(fila)
    return data_por_id


def cargar_pokemones(
    pokemon,
    pokemon_types,
    pokemon_abilities,
    pokemon_egg_groups,
    pokemon_stats,
    pokemon_evolutions,
    pokemon_moves,
    type_efficacy,
    pokemon_species,
):
    with open(pokemon, encoding="utf-8") as pokemon_file, open(
        pokemon_types, encoding="utf-8"
    ) as pokemon_types_file, open(
        pokemon_abilities, encoding="utf-8"
    ) as pokemon_abilities_file, open(
        pokemon_egg_groups, encoding="utf-8"
    ) as pokemon_egg_groups_file, open(
        pokemon_stats, encoding="utf-8"
    ) as pokemon_stats_file, open(
        pokemon_evolutions, encoding="utf-8"
    ) as pokemon_evolutions_file, open(
        pokemon_moves, encoding="utf-8"
    ) as pokemon_moves_file, open(
        type_efficacy, encoding="utf-8"
    ) as type_efficacy_file, open(
        pokemon_species, encoding="utf-8"
    ) as pokemon_species_file:

        pokemones = []

        pokemon_data = list(csv.DictReader(pokemon_file))
        pokemon_types_data = list(csv.DictReader(pokemon_types_file))
        pokemon_abilities_data = list(csv.DictReader(pokemon_abilities_file))
        pokemon_egg_groups_data = list(csv.DictReader(pokemon_egg_groups_file))
        pokemon_stats_data = list(csv.DictReader(pokemon_stats_file))
        pokemon_evolutions_data = list(csv.DictReader(pokemon_evolutions_file))
        pokemon_moves_data = list(csv.DictReader(pokemon_moves_file))
        pokemon_species_data = list(csv.DictReader(pokemon_species_file))
        type_efficacy_data = list(csv.DictReader(type_efficacy_file))

        pokemon_types_data_por_pokemon_id = organizar_datos_por_id(
            pokemon_types_data, "pokemon_id"
        )
        pokemon_abilities_data_por_pokemon_id = organizar_datos_por_id(
            pokemon_abilities_data, "pokemon_id"
        )
        pokemon_egg_groups_data_por_species_id = organizar_datos_por_id(
            pokemon_egg_groups_data, "species_id"
        )
        pokemon_stats_data_por_pokemon_id = organizar_datos_por_id(
            pokemon_stats_data, "pokemon_id"
        )
        pokemon_evolutions_data_por_pokemon_id = organizar_datos_por_id(
            pokemon_evolutions_data, "id"
        )
        pokemon_moves_data_por_pokemon_id = organizar_datos_por_id(
            pokemon_moves_data, "pokemon_id"
        )
        pokemon_species_data_por_id = organizar_datos_por_id(pokemon_species_data, "id")
        type_efficacy_data_por_target_type_id = organizar_datos_por_id(
            type_efficacy_data, "target_type_id"
        )

        for pokemon_line in pokemon_data:

            # id == pokemon_id (esencial para relacionar la mayoria de elementos).
            id = int(pokemon_line["id"])

            # id de relacion con el grupo huevo del pokemon.
            species_id = int(pokemon_line["species_id"])

            # datos generales + nombre del pokemon.
            nombre = str(pokemon_line["identifier"])
            altura = float(pokemon_line["height"])
            peso = float(pokemon_line["weight"])

            # tipos del pokemon.
            tipos = buscar_tipos_por_pokemon_id(pokemon_types_data_por_pokemon_id, id)

            # habilidades del pokemon.
            habilidades = buscar_habilidades_por_pokemon_id(
                pokemon_abilities_data_por_pokemon_id, id
            )
            habilidad_oculta = buscar_habilidad_oculta_por_pokemon_id(
                pokemon_abilities_data_por_pokemon_id, id
            )

            # grupo huevo del pokemon.
            grupo_huevo = buscar_grupo_huevo_por_species_id(
                pokemon_egg_groups_data_por_species_id, species_id
            )

            # stats del pokemon.
            vida = int(
                buscar_stat_por_pokemon_id(pokemon_stats_data_por_pokemon_id, id, 1)
            )
            ataque = int(
                buscar_stat_por_pokemon_id(pokemon_stats_data_por_pokemon_id, id, 2)
            )
            defensa = int(
                buscar_stat_por_pokemon_id(pokemon_stats_data_por_pokemon_id, id, 3)
            )
            ataque_especial = int(
                buscar_stat_por_pokemon_id(pokemon_stats_data_por_pokemon_id, id, 4)
            )
            defensa_especial = int(
                buscar_stat_por_pokemon_id(pokemon_stats_data_por_pokemon_id, id, 5)
            )
            velocidad = int(
                buscar_stat_por_pokemon_id(pokemon_stats_data_por_pokemon_id, id, 6)
            )

            # evoluciones e imagenes del pokemon.
            imagen = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"

            evoluciones = buscar_evoluciones_por_pokemon_id(
                pokemon_evolutions_data_por_pokemon_id, id
            )
            imagenes_evoluciones = []
            for evolucion in evoluciones:
                imagenes_evoluciones.append(
                    f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{evolucion}.png"
                )

            # movimientos aprendibles del pokemon.
            movimientos_aprendibles_nivel = (
                buscar_movimientos_aprendibles_por_pokemon_id(
                    pokemon_moves_data_por_pokemon_id, id, 1
                )
            )
            movimientos_aprendibles_evolucion = []
            movimientos_aprendibles_tms = buscar_movimientos_aprendibles_por_pokemon_id(
                pokemon_moves_data_por_pokemon_id, id, 4
            )
            movimientos_aprendibles_huevo = (
                buscar_movimientos_aprendibles_por_pokemon_id(
                    pokemon_moves_data_por_pokemon_id, id, 2
                )
            )

            # debilidades del pokemon.
            debilidades_tipo = buscar_debilidades_tipo_por_type_id(
                type_efficacy_data_por_target_type_id, tipos
            )

            # generacion del pokemon.
            generacion = buscar_generacion_por_pokemon_id(
                pokemon_species_data_por_id, id
            )

            pokemon: list[Pokemon] = [
                Pokemon(
                    imagen=imagen,
                    id=id,
                    nombre=nombre,
                    tipos=tipos,
                    altura=altura,
                    peso=peso,
                    habilidades=habilidades,
                    habilidad_oculta=habilidad_oculta,
                    grupo_huevo=grupo_huevo,
                    vida=vida,
                    ataque=ataque,
                    defensa=defensa,
                    ataque_especial=ataque_especial,
                    defensa_especial=defensa_especial,
                    velocidad=velocidad,
                    total=int(
                        vida
                        + ataque
                        + defensa
                        + ataque_especial
                        + defensa_especial
                        + velocidad
                    ),
                    evoluciones=evoluciones,
                    imagenes_evoluciones=imagenes_evoluciones,
                    movimientos_aprendibles_nivel=movimientos_aprendibles_nivel,
                    movimientos_aprendibles_evolucion=movimientos_aprendibles_evolucion,
                    movimientos_aprendibles_tms=movimientos_aprendibles_tms,
                    movimientos_aprendibles_huevo=movimientos_aprendibles_huevo,
                    debilidades_tipo=debilidades_tipo,
                    generacion=generacion,
                )
            ]
            pokemones.append(pokemon)

        return pokemones


def buscar_tipos_por_pokemon_id(data_tipos, id_pokemon):
    if id_pokemon not in data_tipos:
        return []
    return [int(tipo["type_id"]) for tipo in data_tipos[id_pokemon]]


def buscar_habilidades_por_pokemon_id(data_habilidades, id_pokemon):
    if id_pokemon not in data_habilidades:
        return []
    return [
        int(habilidad["ability_id"])
        for habilidad in data_habilidades[id_pokemon]
        if int(habilidad["is_hidden"]) == 0
    ]


def buscar_habilidad_oculta_por_pokemon_id(data_habilidades, id_pokemon):
    if id_pokemon not in data_habilidades:
        return None
    for habilidad in data_habilidades[id_pokemon]:
        if int(habilidad["is_hidden"]) == 1:
            return int(habilidad["ability_id"])
    return None


def buscar_grupo_huevo_por_species_id(data_grupo_huevo, species_id):
    if species_id not in data_grupo_huevo:
        return []
    return [
        int(grupo_huevo["egg_group_id"]) for grupo_huevo in data_grupo_huevo[species_id]
    ]


def buscar_stat_por_pokemon_id(data_stat, id_pokemon, devolver_stat):
    if id_pokemon not in data_stat:
        return -1
    stats = [int(stat["base_stat"]) for stat in data_stat[id_pokemon]]

    # Devolver el estadístico correspondiente según el parámetro devolver_stat
    if devolver_stat < 1 or devolver_stat > len(stats):
        return -1
    return stats[devolver_stat - 1]


def buscar_evoluciones_por_pokemon_id(data_evoluciones, id_pokemon):
    if id_pokemon not in data_evoluciones:
        return []
    evoluciones = []
    for evolucion in data_evoluciones[id_pokemon]:
        evolucion_id = int(evolucion["evolution_id"])
        evoluciones.append(evolucion_id)
        evoluciones += buscar_evoluciones_por_pokemon_id(data_evoluciones, evolucion_id)
    return evoluciones


def buscar_movimientos_aprendibles_por_pokemon_id(data_movimientos, id_pokemon, metodo):
    if id_pokemon not in data_movimientos:
        return []

    movimientos_unicos = list(
        {
            int(movimiento["move_id"])
            for movimiento in data_movimientos[id_pokemon]
            if int(movimiento["pokemon_move_method_id"]) == metodo
        }
    )

    return movimientos_unicos


def buscar_debilidades_tipo_por_type_id(data_debilidades, type_id):
    debilidades = []
    for tipo in type_id:
        if tipo not in data_debilidades:
            continue
        for debilidad in data_debilidades[tipo]:
            if int(debilidad["damage_factor"]) > 100:
                debilidades.append(int(debilidad["damage_type_id"]))
    return debilidades


def buscar_generacion_por_pokemon_id(data_generaciones, id_pokemon):
    if id_pokemon not in data_generaciones:
        return 0
    return int(data_generaciones[id_pokemon][0]["generation_id"])


def cargar_movimientos(moves, pokemon_moves):
    with open(moves, encoding="utf-8") as moves_file, open(
        pokemon_moves, encoding="utf-8"
    ) as pokemon_moves_file:

        movimientos = []

        moves_data = list(csv.DictReader(moves_file))
        pokemon_moves_data = list(csv.DictReader(pokemon_moves_file))

        pokemon_moves_data_por_move_id = organizar_datos_por_id(
            pokemon_moves_data, "move_id"
        )

        for move_line in moves_data:

            # id == move_id (esencial para relacionar la mayoria de elementos).
            id = int(move_line["id"])

            # datos de combate + nombre del movimiento.
            nombre = str(move_line["identifier"])
            tipo = int(move_line["type_id"])
            categoria = int(move_line["damage_class_id"])
            potencia = int(move_line["power"]) if move_line["power"] else 0
            precision = int(move_line["accuracy"]) if move_line["accuracy"] else 0
            usos = int(move_line["pp"]) if move_line["pp"] else 0
            generacion = int(move_line["generation_id"])
            efecto = int(move_line["effect_id"])

            # pokemones que aprenden el movimiento.
            pokemones_aprenden_subir_nivel = (
                buscar_pokemones_que_aprenden_el_movimiento(
                    pokemon_moves_data_por_move_id, id, 1
                )
            )
            pokemones_aprenden_evolucionar = (
                buscar_pokemones_que_aprenden_el_movimiento(
                    pokemon_moves_data_por_move_id, id, 2
                )
            )
            pokemones_aprenden_tms = buscar_pokemones_que_aprenden_el_movimiento(
                pokemon_moves_data_por_move_id, id, 4
            )
            pokemones_aprenden_grupo_huevo = (
                buscar_pokemones_que_aprenden_el_movimiento(
                    pokemon_moves_data_por_move_id, id, 3
                )
            )

            movimiento: list[Movimiento] = [
                Movimiento(
                    id=id,
                    nombre=nombre,
                    tipo=tipo,
                    categoria=categoria,
                    potencia=potencia,
                    precision=precision,
                    usos=usos,
                    generacion=generacion,
                    efecto=efecto,
                    pokemones_aprenden_subir_nivel=pokemones_aprenden_subir_nivel,
                    pokemones_aprenden_evolucionar=pokemones_aprenden_evolucionar,
                    pokemones_aprenden_tms=pokemones_aprenden_tms,
                    pokemones_aprenden_grupo_huevo=pokemones_aprenden_grupo_huevo,
                )
            ]
            movimientos.append(movimiento)

        return movimientos


def buscar_pokemones_que_aprenden_el_movimiento(data_movimientos, id_move, metodo):
    if id_move not in data_movimientos:
        return []

    pokemones_vistos = set()
    pokemones_unicos = []

    for movimiento in data_movimientos[id_move]:
        if int(movimiento["pokemon_move_method_id"]) == metodo:
            clave = (
                int(movimiento["pokemon_id"]),
                int(movimiento["level"]) if "level" in movimiento else None,
            )
            if clave not in pokemones_vistos:
                pokemones_vistos.add(clave)
                preview_pokemon = PreViewPokemon(
                    id_pokemon=clave[0],
                    imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{clave[0]}.png",
                    nivel=clave[1],
                )
                pokemones_unicos.append(preview_pokemon)

    return pokemones_unicos


def cargar_naturalezas(natures):
    with open(natures, encoding="utf-8") as natures_file:

        naturalezas = []

        natures_data = list(csv.DictReader(natures_file))

        for nature_line in natures_data:

            # id (esencial para relacionar la mayoria de elementos).
            id = int(nature_line["id"])

            # datos + nombre de la naturaleza.
            nombre = str(nature_line["identifier"])
            stat_perjudicada_id = int(nature_line["decreased_stat_id"])
            stat_mejorada_id = int(nature_line["increased_stat_id"])

            naturaleza: list[Naturaleza] = [
                Naturaleza(
                    id=id,
                    nombre=nombre,
                    stat_perjudicada_id=stat_perjudicada_id,
                    stat_mejorada_id=stat_mejorada_id,
                )
            ]
            naturalezas.append(naturaleza)

        return naturalezas


pokemones = cargar_pokemones(
    "pokemon.csv",
    "pokemon_types.csv",
    "pokemon_abilities.csv",
    "pokemon_egg_groups.csv",
    "pokemon_stats.csv",
    "pokemon_evolutions.csv",
    "pokemon_moves.csv",
    "type_efficacy.csv",
    "pokemon_species.csv",
)

movimientos = cargar_movimientos("moves.csv", "pokemon_moves.csv")

naturalezas = cargar_naturalezas("natures.csv")

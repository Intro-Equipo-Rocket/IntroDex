from app.modelos import Movimientos, PreViewPokemon


def crear_preview_pokemon(id_pokemon: int, nivel: int) -> PreViewPokemon:
    return PreViewPokemon(
        id_pokemon=id_pokemon,
        imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id_pokemon}.png",
        nivel=nivel,
    )


Moves: list[Movimientos] = [
    Movimientos(
        id=813,
        nombre="triple-axel",
        tipo=15,
        categoria=2,
        potencia=20,
        precision=90,
        usos=10,
        generacion=8,
        efecto=1,
        pokemones_aprenden_subir_nivel=[
            crear_preview_pokemon(1, 99),
        ],
        pokemones_aprenden_evolucionar=[
            crear_preview_pokemon(2, None),
        ],
        pokemones_aprenden_tms=[
            crear_preview_pokemon(3, None),
        ],
        pokemones_aprenden_grupo_huevo=[
            crear_preview_pokemon(658, None),
            crear_preview_pokemon(999, None),
        ],
    ),
    Movimientos(
        id=84,
        nombre="thunder-shock",
        tipo=13,
        categoria=3,
        potencia=40,
        precision=100,
        usos=30,
        generacion=1,
        efecto=7,
        pokemones_aprenden_subir_nivel=[
            crear_preview_pokemon(25, 1),
        ],
        pokemones_aprenden_evolucionar=[
            crear_preview_pokemon(2, None),
        ],
        pokemones_aprenden_tms=[
            crear_preview_pokemon(3, None),
        ],
        pokemones_aprenden_grupo_huevo=[
            crear_preview_pokemon(658, None),
            crear_preview_pokemon(999, None),
        ],
    ),
    Movimientos(
        id=85,
        nombre="thunderbolt",
        tipo=13,
        categoria=3,
        potencia=90,
        precision=100,
        usos=15,
        generacion=1,
        efecto=7,
        pokemones_aprenden_subir_nivel=[
            crear_preview_pokemon(1, None),
        ],
        pokemones_aprenden_evolucionar=[
            crear_preview_pokemon(2, None),
        ],
        pokemones_aprenden_tms=[
            crear_preview_pokemon(3, None),
        ],
        pokemones_aprenden_grupo_huevo=[
            crear_preview_pokemon(658, None),
            crear_preview_pokemon(999, None),
        ],
    ),
    Movimientos(
        id=113,
        nombre="light-screen",
        tipo=14,
        categoria=1,
        potencia=0,
        precision=0,
        usos=30,
        generacion=1,
        efecto=36,
        pokemones_aprenden_subir_nivel=[
            crear_preview_pokemon(25, 50),
        ],
        pokemones_aprenden_evolucionar=[
            crear_preview_pokemon(2, None),
        ],
        pokemones_aprenden_tms=[
            crear_preview_pokemon(3, None),
        ],
        pokemones_aprenden_grupo_huevo=[
            crear_preview_pokemon(658, None),
            crear_preview_pokemon(999, None),
        ],
    ),
    Movimientos(
        id=25,
        nombre="mega-kick",
        tipo=1,
        categoria=2,
        potencia=120,
        precision=75,
        usos=5,
        generacion=1,
        efecto=36,
        pokemones_aprenden_subir_nivel=[
            crear_preview_pokemon(1, None),
        ],
        pokemones_aprenden_evolucionar=[
            crear_preview_pokemon(2, None),
        ],
        pokemones_aprenden_tms=[
            crear_preview_pokemon(25, None),
        ],
        pokemones_aprenden_grupo_huevo=[
            crear_preview_pokemon(658, None),
            crear_preview_pokemon(999, None),
        ],
    )
]

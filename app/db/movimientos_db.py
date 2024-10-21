from app.modelos import Movimiento, PreViewPokemon


def crear_preview_pokemon(id_pokemon: int, nivel: int) -> PreViewPokemon:
    return PreViewPokemon(
        id_pokemon=id_pokemon,
        imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id_pokemon}.png",
        nivel=nivel,
    )


Moves: list[Movimiento] = [
    Movimiento(
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
    )
]

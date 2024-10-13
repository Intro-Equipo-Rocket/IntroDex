from pydantic import BaseModel


class PreViewPokemon(BaseModel):
    id_pokemon: int
    imagen: str
    nivel: int | None = None


class Move(BaseModel):
    id: int
    nombre: str
    tipo: str
    categoria: str
    potencia: int
    precision: int
    usos: int
    generacion: int
    efecto: str
    pokemones_aprenden_subir_nivel: list[PreViewPokemon]
    pokemones_aprenden_evolucionar: list[PreViewPokemon]
    pokemones_aprenden_tms: list[PreViewPokemon]
    pokemones_aprenden_grupo_huevo: list[PreViewPokemon]


class Error(BaseModel):
    detail: str


def crear_preview_pokemon(id_pokemon: int, nivel: int) -> PreViewPokemon:
    return PreViewPokemon(
        id_pokemon=id_pokemon,
        imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id_pokemon}.png",
        nivel=nivel,
    )


Moves: list[Move] = [
    Move(
        id=813,
        nombre="triple-axel",
        tipo="Ice",
        categoria="Physical",
        potencia=20,
        precision=90,
        usos=10,
        generacion=8,
        efecto="Inflicts regular damage with no additional effect.",
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
    )
]

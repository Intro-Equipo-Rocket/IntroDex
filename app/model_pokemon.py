from pydantic import BaseModel

class Pokemon(BaseModel):
    imagen: str
    id: int
    nombre: str
    tipos: list[str]
    altura: int
    peso: int
    habilidades: list[str]
    habilidad_oculta: str | None = None
    grupo_huevo: list[str]
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int
    total: int
    evoluciones: list[str] | None = None
    imagenes_evoluciones = list[str] | None = None


pokemones: list[Pokemon] = [
    Pokemon(
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        id=25,
        nombre="Pikachu",
        tipos=["Eléctrico"],
        altura=4,
        peso=60,
        habilidades=["Electricidad Estática", "Pararrayos"],
        habilidad_oculta=None,
        grupo_huevo=["Campo", "Hada"],
        vida=35,
        ataque=55,
        defensa=40,
        ataque_especial=50,
        defensa_especial=50,
        velocidad=90,
        total=320,
        evoluciones=["Raichu"],
        imagenes_evoluciones="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png",
    ),
    Pokemon(
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
        id=2,
        nombre="Ivysaur",
        tipos=["Planta", "Veneno"],
        altura=10,
        peso=130,
        habilidades=["Espesura"],
        habilidad_oculta="Clorofila",
        grupo_huevo=["PLanta", "Monstruo"],
        vida=60,
        ataque=62,
        defensa=63,
        ataque_especial=80,
        defensa_especial=80,
        velocidad=60,
        total=405,
        evoluciones=["Venusaur"],
        imagenes_evoluciones="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png",
    ),
    Pokemon(
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        id=9,
        nombre="Blastoise",
        tipos=["Agua"],
        altura=16,
        peso=855,
        habilidades=["Torrente"],
        habilidad_oculta="Cura Lluvia",
        grupo_huevo=["Agua", "Monstruo"],
        vida=79,
        ataque=83,
        defensa=100,
        ataque_especial=85,
        defensa_especial=105,
        velocidad=78,
        total=530,
        evoluciones= None,
        imagenes_evoluciones=None,
    ),
    Pokemon(
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/647.png",
        id=647,
        nombre="Keldeo",
        tipos=["Agua", "Lucha"],
        altura=14,
        peso=485,
        habilidades=["Justiciero"],
        habilidad_oculta=None,
        vida=91,
        ataque=72,
        defensa=90,
        ataque_especial=129,
        defensa_especial=90,
        velocidad=108,
        total=580,
        evoluciones=None,
        imagenes_evoluciones=None,
    ),
    Pokemon(
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/555.png",
        id=555,
        nombre="Darmanitan",
        tipos="Fuego",
        altura=13,
        peso=929,
        habilidades="Potencia Bruta",
        habilidad_oculta="Modo Daruma",
        vida=105,
        ataque=140,
        defensa=55,
        ataque_especial=30,
        defensa_especial=55,
        velocidad=95,
        total=480,
        evoluciones=None,
        imagenes_evoluciones=None,
    ),
]

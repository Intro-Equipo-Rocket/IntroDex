from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    nombre: str
    tipo_principal: str
    tipo_secundario: str | None = None
    altura: int
    peso: int
    habilidad_1: str
    habilidad_2: str | None = None
    habilidad_oculta: str | None = None
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int
    imagen: str


class Error(BaseModel):
    code: int
    detail: str


pokemones: list[Pokemon] = [
    Pokemon(
        id=25,
        nombre="Pikachu",
        tipo_principal="Eléctrico",
        tipo_secundario=None,
        altura=4,
        peso=60,
        habilidad_1="Electricidad Estática",
        habilidad_2="Pararrayos",
        habilidad_oculta=None,
        vida=35,
        ataque=55,
        defensa=40,
        ataque_especial=50,
        defensa_especial=50,
        velocidad=90,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    ),
    Pokemon(
        id=2,
        nombre="Ivysaur",
        tipo_principal="Planta",
        tipo_secundario="Veneno",
        altura=10,
        peso=130,
        habilidad_1="Espesura",
        habilidad_2=None,
        habilidad_oculta="Clorofila",
        vida=60,
        ataque=62,
        defensa=63,
        ataque_especial=80,
        defensa_especial=80,
        velocidad=60,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
    ),
    Pokemon(
        id=300,
        nombre="Skitty",
        tipo_principal="Normal",
        tipo_secundario=None,
        altura=6,
        peso=110,
        habilidad_1="Gran Encanto",
        habilidad_2="Normalidad",
        habilidad_oculta="Piel Milagro",
        vida=50,
        ataque=45,
        defensa=45,
        ataque_especial=35,
        defensa_especial=35,
        velocidad=50,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/300.png",
    ),
    Pokemon(
        id=9,
        nombre="Blastoise",
        tipo_principal="Agua",
        tipo_secundario=None,
        altura=16,
        peso=855,
        habilidad_1="Torrente",
        habilidad_2=None,
        habilidad_oculta="Cura Lluvia",
        vida=79,
        ataque=83,
        defensa=100,
        ataque_especial=85,
        defensa_especial=105,
        velocidad=78,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
    ),
    Pokemon(
        id=647,
        nombre="Keldeo",
        tipo_principal="Agua",
        tipo_secundario="Lucha",
        altura=14,
        peso=485,
        habilidad_1="Justiciero",
        habilidad_2=None,
        habilidad_oculta=None,
        vida=91,
        ataque=72,
        defensa=90,
        ataque_especial=129,
        defensa_especial=90,
        velocidad=108,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/647.png",
    ),
    Pokemon(
        id=555,
        nombre="Darmanitan",
        tipo_principal="Fuego",
        tipo_secundario=None,
        altura=13,
        peso=929,
        habilidad_1="Potencia Bruta",
        habilidad_2=None,
        habilidad_oculta="Modo Daruma",
        vida=105,
        ataque=140,
        defensa=55,
        ataque_especial=30,
        defensa_especial=55,
        velocidad=95,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/555.png",
    ),
    Pokemon(
        id=658,
        nombre="Greninja",
        tipo_principal="Agua",
        tipo_secundario="Siniestro",
        altura=15,
        peso=400,
        habilidad_1="Torrente",
        habilidad_2=None,
        habilidad_oculta="Mutatipo",
        vida=72,
        ataque=95,
        defensa=67,
        ataque_especial=103,
        defensa_especial=71,
        velocidad=122,
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png",
    ),
]

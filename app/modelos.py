from pydantic import BaseModel

class Pokemon(BaseModel):
    imagen: str
    id: int
    nombre: str
<<<<<<< HEAD
    tipos: list[str]
    altura: int
    peso: int
    habilidades: list[str]
    habilidad_oculta: str | None = None
=======
    tipos: list[int]
    altura: int
    peso: int
    habilidades: list[int]
    habilidad_oculta: int | None = None
    grupo_huevo:list[int]
>>>>>>> parte_1
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int
    total: int
<<<<<<< HEAD
    evoluciones: list[str] | None = None
    imagenes_evoluciones: list[str] | None = None
=======
    evoluciones: list[int] | None = None
    imagenes_evoluciones: list[str] | None = None
    movimientos_aprendibles_nivel: list[int]
    movimientos_aprendibles_evolucion: list[int]
    movimientos_aprendibles_tms: list[int]
    movimientos_aprendibles_huevo: list[int]
    debilidades_tipo: list[int]
>>>>>>> parte_1

class Error(BaseModel):
    detail: str

class Equipo(BaseModel):
    id: int
    nombre: str
    pokemones: list[int]  
<<<<<<< HEAD
    naturaleza: str | None = None
=======

class IntegranteEquipo(BaseModel):
    imagen: str
    id: int
    nombre: str
    tipos: list[int]
    habilidades: list[int]
    habilidad_oculta: int | None = None
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int
    total: int
    movimientos = list[int]

class PreViewPokemon(BaseModel):
    id_pokemon: int
    imagen: str
    nivel: int | None = None

class Movimientos(BaseModel):
    id: int
    nombre: str
    tipo: int
    categoria: int
    potencia: int
    precision: int
    usos: int
    generacion: int
    efecto: int
    pokemones_aprenden_subir_nivel: list[PreViewPokemon]
    pokemones_aprenden_evolucionar: list[PreViewPokemon]
    pokemones_aprenden_tms: list[PreViewPokemon]
    pokemones_aprenden_grupo_huevo: list[PreViewPokemon]
>>>>>>> parte_1

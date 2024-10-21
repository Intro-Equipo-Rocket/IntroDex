from pydantic import BaseModel


class Pokemon(BaseModel):
    imagen: str
    id: int
    nombre: str
    tipos: list[int]
    altura: int
    peso: int
    habilidades: list[int]
    habilidad_oculta: int | None = None
    grupo_huevo: list[int]
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int
    total: int
    evoluciones: list[int] | None = None
    imagenes_evoluciones: list[str] | None = None
    movimientos_aprendibles_nivel: list[int]
    movimientos_aprendibles_evolucion: list[int]
    movimientos_aprendibles_tms: list[int]
    movimientos_aprendibles_huevo: list[int]
    debilidades_tipo: list[int]
    generacion: int

class Error(BaseModel):
    detail: str

class Naturaleza(BaseModel):
    id: int
    nombre: str
    stat_perjudicada_id: int
    stat_mejorada_id: int

class Estadisticas(BaseModel):
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int

class IntegranteEquipo(BaseModel):
    pokemon:Pokemon
    movimientos: list[int]
    naturaleza: Naturaleza
    evs: Estadisticas

class Equipo(BaseModel):
    id: int
    nombre: str
    pokemones: list[IntegranteEquipo]

class PreViewPokemon(BaseModel):
    id_pokemon: int
    imagen: str
    nivel: int | None = None


class Movimiento(BaseModel):
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

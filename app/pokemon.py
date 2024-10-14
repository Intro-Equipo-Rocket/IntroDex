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
    imagenes_evoluciones: list[str] | None = None

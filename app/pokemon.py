from pydantic import BaseModel
from typing import Optional

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
    evoluciones: Optional[list[str]] = []
    imagenes_evoluciones: Optional[list[str]] = []
from pydantic import BaseModel

class Naturaleza(BaseModel):
    id: int
    nombre: str
    stat_perjudicada_id: int
    stat_mejorada_id: int
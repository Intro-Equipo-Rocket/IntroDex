from pydantic import BaseModel
from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    Column,
    ForeignKey,
    Table,
    Relationship,
    Integer,
    Text,
    String,
)


# class Pokemon(BaseModel):
#     imagen: str
#     id: int
#     nombre: str
#     tipos: list[int]
#     altura: int
#     peso: int
#     habilidades: list[int]
#     habilidad_oculta: int | None = None
#     grupo_huevo: list[int]
#     vida: int
#     ataque: int
#     defensa: int
#     ataque_especial: int
#     defensa_especial: int
#     velocidad: int
#     total: int
#     evoluciones: list[int] | None = None
#     imagenes_evoluciones: list[str] | None = None
#     movimientos_aprendibles_nivel: list[int]
#     movimientos_aprendibles_evolucion: list[int]
#     movimientos_aprendibles_tms: list[int]
#     movimientos_aprendibles_huevo: list[int]
#     debilidades_tipo: list[int]
#     generacion: int


class PokemonBase(SQLModel):
    imagen: str = Field(sa_column=Column("imagen", Text, nullable=False))
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    altura: int = Field(sa_column=Column("height", Integer, nullable=False))
    peso: int = Field(sa_column=Column("weight", Integer, nullable=False))
    generacion: int = Field(sa_column=Column("generation_id", Integer, nullable=False))
    id_evolucion: Optional[int] = Field(
        sa_column=Column("evolution_id", Integer, nullable=False)
    )
    imagen_evolucion: str = Field(
        sa_column=Column("imagen_evolucion", Text, nullable=False)
    )


class Pokemon(PokemonBase, table=True):
    __tablename__ = "pokemon"
    id: int = Field(sa_column=Column("pokemon_id", Integer, primary_key=True))
    tipos: List["TiposDelPokemon"] = Relationship(back_populates="pokemon")
    habilidades: List["HabilidadesDelPokemon"] = Relationship(back_populates="pokemon")
    grupo_huevo: List["GrupoHuevoDelPokemon"] = Relationship(back_populates="pokemon")
    stats: List["StatsDelPokemon"] = Relationship(back_populates="pokemon")
    movimientos_aprendibles: List["MovimientosAprendiblesDelPokemon"] = Relationship(
        back_populates="pokemon"
    )
    integrante: List["IntegrantesEquipo"] | None = Relationship(
        back_populates="pokemon"
    )


class PokemonCreate(PokemonBase):
    pass


class Tipos(SQLModel, table=True):
    __tablename__ = "tipo_pokemon"
    id: int = Field(sa_column=Column("type_id", Integer, primary_key=True))
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    pokemon_id: int = Field(
        sa_column=Column("pokemon_id", Integer, ForeignKey("pokemon.pokemon_id"))
    )
    pokemon: List["TiposDelPokemon"] = Relationship(back_populates="tipos")


class TiposCreate(SQLModel):
    pass


class TiposDelPokemon(SQLModel, table=True):
    pokemon_id: int = Field(
        sa_column=Column(Integer, ForeignKey("pokemon.pokemon_id"), primary_key=True)
    )
    type_id: int = Field(
        sa_column=Column(Integer, ForeignKey("tipo_pokemon.type_id"), primary_key=True)
    )
    pokemon: Pokemon = Relationship(back_populates="tipos")
    tipos: Tipos = Relationship(back_populates="pokemon")


class HabiliadesBase(SQLModel):
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    es_habilidad_oculta: bool = Field(
        sa_column=Column("is_hiden", Integer, nullable=False)
    )


class Habilidades(HabiliadesBase, table=True):
    __tablename__ = "habilidades"
    id: int = Field(sa_column=Column("ability_id", Integer, primary_key=True))
    pokemon_id: int = Field(
        sa_column=Column("pokemon_id", Integer, ForeignKey("pokemon.pokemon_id"))
    )
    pokemones: List["HabilidadesDelPokemon"] = Relationship(
        back_populates="habilidades"
    )


class HabilidadesCreate(HabiliadesBase):
    pass


class HabilidadesDelPokemon(SQLModel, table=True):
    pokemon_id: int = Field(
        sa_column=Column(Integer, ForeignKey("pokemon.pokemon_id"), primary_key=True)
    )
    ability_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("habilidades.ability_id"), primary_key=True
        )
    )
    pokemon: Pokemon = Relationship(back_populates="habilidades")
    habilidades: Habilidades = Relationship(back_populates="pokemon")


class GrupoHuevo(SQLModel, table=True):
    __tablename__ = "grupo_huevo"
    id: int = Field(sa_column=Column("egg_group_id", Integer, primary_key=True))
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    pokemon_id: int = Field(
        sa_column=Column("pokemon_id", Integer, ForeignKey("pokemon.pokemon_id"))
    )
    pokemon: List["GrupoHuevoDelPokemon"] = Relationship(back_populates="grupo_huevo")


class GrupoHuevoCreate(SQLModel):
    pass


class GrupoHuevoDelPokemon(SQLModel, table=True):
    pokemon_id: int = Field(
        sa_column=Column(Integer, ForeignKey("pokemon.pokemon_id"), primary_key=True)
    )
    egg_group_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("grupo_huevo.egg_group_id"), primary_key=True
        )
    )
    pokemon: Pokemon = Relationship(back_populates="grupo_huevo")
    grupo_huevo: GrupoHuevo = Relationship(back_populates="pokemon")


class Stats(SQLModel, table=True):
    __tablename__ = "stats"
    id: int = Field(sa_column=Column("stat_id", Integer, primary_key=True))
    base_stat: int = Field(sa_column=Column("base_stat", Integer, nullable=False))
    pokemon_id: int = Field(
        sa_column=Column("pokemon_id", Integer, ForeignKey("pokemon.pokemon_id"))
    )
    pokemon: List["StatsDelPokemon"] = Relationship(back_populates="stats")


class StatsCreate(SQLModel):
    pass


class StatsDelPokemon(SQLModel, table=True):
    pokemon_id: int = Field(
        sa_column=Column(Integer, ForeignKey("pokemon.pokemon_id"), primary_key=True)
    )
    stat_id: int = Field(
        sa_column=Column(Integer, ForeignKey("stats.stat_id"), primary_key=True)
    )
    pokemon: Pokemon = Relationship(back_populates="stats")
    stats: Stats = Relationship(back_populates="pokemon")


class MovimientosBase(SQLModel):
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    tipo: int = Field(sa_column=Column("type_id", Integer, nullable=False))
    categoria: int = Field(sa_column=Column("damage_class_id", Integer, nullable=False))
    potencia: int = Field(sa_column=Column("power", Integer, nullable=False))
    precision: int = Field(sa_column=Column("accuracy", Integer, nullable=False))
    usos: int = Field(sa_column=Column("pp", Integer, nullable=False))
    generacion: int = Field(sa_column=Column("generation_id", Integer, nullable=False))
    efecto: int = Field(sa_column=Column("effect_id", Integer, nullable=False))


class MetodoAprenderMovimiento(SQLModel, table=True):
    __tablename__ = "metodo_aprender_movimiento"
    pokemon_move_method_id: int = Field(
        sa_column=Column(
            "pokemon_move_method_id", Integer, nullable=False, primary_key=True
        )
    )
    movimientos: Optional["Movimientos"] = Relationship(
        back_populates="metodo_aprendizaje"
    )
    move_id: int = Field(
        sa_column=Column(
            "move_id", Integer, ForeignKey("movimientos.move_id"), primary_key=True
        )
    )


class Movimientos(SQLModel, table=True):
    __tablename__ = "movimientos"
    id: int = Field(sa_column=Column("move_id", Integer, primary_key=True))
    pokemon_id: int = Field(
        sa_column=Column("pokemon_id", Integer, ForeignKey("pokemon.pokemon_id"))
    )
    pokemon: List["MovimientosAprendiblesDelPokemon"] = Relationship(
        back_populates="movimientos"
    )
    metodo_aprendizaje: List["MetodoAprenderMovimiento"] = Relationship(
        back_populates="movimientos"
    )


class MovimientosCreate(MovimientosBase):
    pass


class MovimientosAprendiblesDelPokemon(SQLModel, table=True):
    __tablename__ = "movimientos_aprendibles"
    pokemon_id: int = Field(
        sa_column=Column(Integer, ForeignKey("pokemon.pokemon_id"), primary_key=True)
    )
    move_id: int = Field(
        sa_column=Column(Integer, ForeignKey("movimientos.move_id"), primary_key=True)
    )
    pokemon: Pokemon = Relationship(back_populates="movimientos")
    movimientos: Movimientos = Relationship(back_populates="pokemon")


class DebilidadesBase(SQLModel):
    damage_type: int = Field(
        sa_column=Column("damage_type_id", Integer, nullable=False)
    )
    target_type: int = Field(
        sa_column=Column("target_type_id", Integer, nullable=False)
    )
    damage_factor: int = Field(
        sa_column=Column("damage_factor", Integer, nullable=False)
    )


class Debilidades(SQLModel, table=True):
    __tablename__ = "debilidades"
    id: int = Field(
        sa_column=Column(
            "type_id", Integer, ForeignKey("tipo_pokemon.type_id"), primary_key=True
        )
    )


class DebilidadesCreate(DebilidadesBase):
    pass


class NaturalezaBase(SQLModel):
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    stat_perjudicada: int = Field(
        sa_column=Column("decreased_stat_id", Integer, nullable=False)
    )
    stat_mejorada: int = Field(
        sa_column=Column("increased_stat_id", Integer, nullable=False)
    )


class Naturaleza(NaturalezaBase, table=True):
    __tablename__ = "naturaleza"
    id: int = Field(sa_column=Column("id", Integer, primary_key=True))


# class Estadisticas(BaseModel):
#     vida: int
#     ataque: int
#     defensa: int
#     ataque_especial: int
#     defensa_especial: int
#     velocidad: int


class EstadisticasBase(SQLModel):
    vida: int = Field(sa_column=Column("hp", Integer, nullable=False))
    ataque: int = Field(sa_column=Column("attack", Integer, nullable=False))
    defensa: int = Field(sa_column=Column("defense", Integer, nullable=False))
    ataque_especial: int = Field(
        sa_column=Column("special-attack", Integer, nullable=False)
    )
    defensa_especial: int = Field(
        sa_column=Column("special-defense", Integer, nullable=False)
    )
    velocidad: int = Field(sa_column=Column("speed", Integer, nullable=False))


class EstadisticasTabla(SQLModel, table=True):
    __tablename__ = "estadisticas"
    member_id: int = Field(
        sa_column=Column(
            "member_id",
            Integer,
            ForeignKey("integrantes_equipo.member_id"),
            primary_key=True,
        )
    )


class IntegrantesEquipo(SQLModel, table=True):
    __tablename__ = "integrantes_equipo"
    id: int = Field(sa_column=Column("member_id", Integer, primary_key=True))
    pokemon_id: int = Field(
        sa_column=Column("pokemon_id", Integer, ForeignKey("pokemon.pokemon_id"))
    )
    pokemon: Optional[Pokemon] = Relationship(back_populates="integrante")
    equipo_id: int = Field(
        sa_column=Column("team_id", Integer, ForeignKey("equipo.id"))
    )
    equipo: Optional["Equipo"] = Relationship(back_populates="integrantes")
    movimientos: List["MovimientosDelIntegrante"] = Relationship(
        back_populates="integrante"
    )
    naturaleza_id: int = Field(
        sa_column=Column("nature_id", Integer, ForeignKey("naturaleza.id"))
    )
    evs: Estadisticas = Relationship(back_populates="integrantes_equipo")


class MovimientosDelIntegrante(SQLModel, table=True):
    member_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("integrantes_equipo.member_id"), primary_key=True
        )
    )
    move_id: int = Field(
        sa_column=Column(Integer, ForeignKey("movimientos.move_id"), primary_key=True)
    )
    integrante: Optional[IntegrantesEquipo] = Relationship(back_populates="movimientos")
    movimientos: Optional[Movimientos] = Relationship()


class Equipo(SQLModel, table=True):
    __tablename__ = "equipo"
    id: int = Field(sa_column=Column("id", Integer, primary_key=True))
    nombre: str = Field(sa_column=Column("identifier", Text, nullable=False))
    generacion: int = Field(sa_column=Column("generation_id", Integer, nullable=False))
    integrantes: List["IntegrantesEquipo"] = Relationship(back_populates="equipo")


class Error(BaseModel):
    detail: str


# class Naturaleza(BaseModel):
#     id: int
#     nombre: str
#     stat_perjudicada_id: int
#     stat_mejorada_id: int


# class IntegranteEquipo(BaseModel):
#     pokemon: Pokemon
#     movimientos: list[int]
#     naturaleza: Naturaleza
#     evs: Estadisticas


# class Equipo(BaseModel):
#     id: int
#     nombre: str
#     pokemones: list[IntegranteEquipo]
#     generacion: int


# class PreViewPokemon(BaseModel):
#     id_pokemon: int
#     imagen: str
#     nivel: int | None = None


# class Movimiento(BaseModel):
#     id: int
#     nombre: str
#     tipo: int
#     categoria: int
#     potencia: int
#     precision: int
#     usos: int
#     generacion: int
#     efecto: int
#     pokemones_aprenden_subir_nivel: Optional[List[PreViewPokemon]] = None
#     pokemones_aprenden_evolucionar: Optional[List[PreViewPokemon]] = None
#     pokemones_aprenden_tms: Optional[List[PreViewPokemon]] = None
#     pokemones_aprenden_grupo_huevo: Optional[List[PreViewPokemon]] = None

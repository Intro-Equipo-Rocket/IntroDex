from pydantic import BaseModel


class TiposPokemon(BaseModel):
    id_tipo_principal: int
    id_tipo_secundario: int | None = None


class HabilidadesPokemon(BaseModel):
    id_habilidad_1: int
    id_habilidad_2: int | None = None
    id_habilidad_oculta: int | None = None


class EstadisticasPokemon(BaseModel):
    vida: int
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    velocidad: int


class GrupoHuevoPokemon(BaseModel):
    id_especie: int
    id_grupo_huevo: int


class Debilidades_tipo_pokemon(BaseModel):
    normal: int
    lucha: int
    volador: int
    veneno: int
    tierra: int
    roca: int
    bicho: int
    fantasma: int
    acero: int
    fuego: int
    agua: int
    planta: int
    electrico: int
    psiquico: int
    hielo: int
    dragon: int
    siniestro: int
    hada: int


class EvolucionesPokemon(BaseModel):
    id_evolucion: int | None = None
    imagen_evolucion: str | None = None


class Pokemon(BaseModel):
    id: int
    nombre: str
    tipos: list[TiposPokemon]
    altura: int
    peso: int
    habilidades: list[HabilidadesPokemon]
    estadisticas: list[EstadisticasPokemon]
    grupo_huevo: list[GrupoHuevoPokemon]
    debilidades_tipo: tuple[Debilidades_tipo_pokemon]
    evoluciones: list[EvolucionesPokemon]
    imagen: str


class Error(BaseModel):
    detail: str


def crear_tipos_pokemon(
    id_tipo_principal: int, id_tipo_secundario: int
) -> TiposPokemon:
    return TiposPokemon(
        id_tipo_principal=id_tipo_principal, id_tipo_secundario=id_tipo_secundario
    )


def crear_habilidades_pokemon(
    id_habilidad_1: int, id_habilidad_2: int, id_habilidad_oculta: int
) -> HabilidadesPokemon:
    return HabilidadesPokemon(
        id_habilidad_1=id_habilidad_1,
        id_habilidad_2=id_habilidad_2,
        id_habilidad_oculta=id_habilidad_oculta,
    )


def crear_estadisticas_pokemon(
    vida: int,
    ataque: int,
    defensa: int,
    ataque_especial: int,
    defensa_especial: int,
    velocidad: int,
) -> EstadisticasPokemon:
    return EstadisticasPokemon(
        vida=vida,
        ataque=ataque,
        defensa=defensa,
        ataque_especial=ataque_especial,
        defensa_especial=defensa_especial,
        velocidad=velocidad,
    )


def crear_grupo_huevo_pokemon(
    id_especie: int, id_grupo_huevo: int
) -> GrupoHuevoPokemon:
    return GrupoHuevoPokemon(id_especie=id_especie, id_grupo_huevo=id_grupo_huevo)


def crear_debilidades_tipos_pokemon(
    normal: int,
    lucha: int,
    volador: int,
    veneno: int,
    tierra: int,
    roca: int,
    bicho: int,
    fantasma: int,
    acero: int,
    fuego: int,
    agua: int,
    planta: int,
    electrico: int,
    psiquico: int,
    hielo: int,
    dragon: int,
    siniestro: int,
    hada: int,
) -> Debilidades_tipo_pokemon:
    return Debilidades_tipo_pokemon(
        normal=normal,
        fuego=fuego,
        agua=agua,
        electrico=electrico,
        planta=planta,
        hielo=hielo,
        lucha=lucha,
        veneno=veneno,
        tierra=tierra,
        volador=volador,
        psiquico=psiquico,
        bicho=bicho,
        roca=roca,
        fantasma=fantasma,
        dragon=dragon,
        siniestro=siniestro,
        acero=acero,
        hada=hada,
    )


def crear_evoluciones_pokemon(id_evolucion: int) -> EvolucionesPokemon:
    if id_evolucion != None:
        return EvolucionesPokemon(
            id_evolucion=id_evolucion,
            imagen_evolucion=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id_evolucion}.png",
        )
    else:
        return EvolucionesPokemon(
            id_evolucion=None,
            imagen_evolucion=None,
        )


pokemones: list[Pokemon] = [
    Pokemon(
        id=25,
        nombre="Pikachu",
        tipos=[crear_tipos_pokemon(13, None)],
        altura=4,
        peso=60,
        habilidades=[crear_habilidades_pokemon(9, 31, None)],
        estadisticas=[crear_estadisticas_pokemon(35, 55, 40, 50, 50, 90)],
        grupo_huevo=[crear_grupo_huevo_pokemon(25, 5)],
        debilidades_tipo=[
            crear_debilidades_tipos_pokemon(
                100,
                100,
                200,
                100,
                0,
                100,
                100,
                100,
                100,
                100,
                200,
                50,
                50,
                100,
                100,
                50,
                100,
                100,
            )
        ],
        evoluciones=[crear_evoluciones_pokemon(26)],
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    ),
    Pokemon(
        id=658,
        nombre="Greninja",
        tipos=[crear_tipos_pokemon(11, 17)],
        altura=15,
        peso=400,
        habilidades=[crear_habilidades_pokemon(67, None, 168)],
        estadisticas=[crear_estadisticas_pokemon(72, 95, 67, 103, 71, 122)],
        grupo_huevo=[crear_grupo_huevo_pokemon(658, 2)],
        debilidades_tipo=[
            crear_debilidades_tipos_pokemon(
                100,
                200,
                100,
                100,
                100,
                100,
                200,
                50,
                50,
                50,
                50,
                200,
                200,
                0,
                50,
                100,
                50,
                200,
            )
        ],
        evoluciones=[crear_evoluciones_pokemon(None)],
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png",
    ),
]

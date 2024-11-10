from fastapi import APIRouter, HTTPException, status
from app.modelos import *
# from app.db.equipos_db import *
# from app.db.naturaleza_db import *
# from app.routers.pokemon import *
from typing import List
from sqlmodel import Session, select
from app.database import SessionDep

router = APIRouter()

# @router.get("/pagina/{pagina}", response_model=List[Equipo])
# def obtener_equipos(pagina: int, cantidad_equipos: int = 10):
#     if pagina < 1 or cantidad_equipos < 1:
#         raise HTTPException(status_code=404, detail="Algunos de los parámetros están siendo mal introducidas")
    
#     skip = (pagina - 1) * 10
#     equipos_pagina = equipos_db[skip:skip + cantidad_equipos]

#     if not equipos_pagina:
#         raise HTTPException(status_code=404, detail="No se encontraron equipos para esta página")
    
#     return equipos_pagina

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EquipoPublic)
def crear_equipo(id_equipo: int, nombre_equipo: str, generacion_equipo: int, session: SessionDep,
                 id_pkm_1: int=None, id_movimientos_pkm_1: list[int]=None, id_naturaleza_1: int=None, evs_pkm_1: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_2: int=None, id_movimientos_pkm_2: list[int]=None, id_naturaleza_2: int=None, evs_pkm_2: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_3: int=None, id_movimientos_pkm_3: list[int]=None, id_naturaleza_3: int=None, evs_pkm_3: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_4: int=None, id_movimientos_pkm_4: list[int]=None, id_naturaleza_4: int=None, evs_pkm_4: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_5: int=None, id_movimientos_pkm_5: list[int]=None, id_naturaleza_5: int=None, evs_pkm_5: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_6: int=None, id_movimientos_pkm_6: list[int]=None, id_naturaleza_6: int=None, evs_pkm_6: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),):
    
    query = select(Equipo).where(Equipo.id == id_equipo)
    equipo = session.exec(query).first()
    if equipo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Ese equipo ya existe"
        )
    if generacion_equipo not in range(1, 9):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La generación del equipo no es válida"
        )
    
    nuevo_equipo = Equipo(
        id=id_equipo,
        nombre=nombre_equipo,
        generacion=generacion_equipo,
        integrantes=[]
    )
    if id_pkm_1 is not None:
        asignacion_datos_integrantes(id_pkm_1, generacion_equipo, id_movimientos_pkm_1, evs_pkm_1, id_naturaleza_1, nuevo_equipo, session)
    if id_pkm_2 is not None:
        asignacion_datos_integrantes(id_pkm_2, generacion_equipo, id_movimientos_pkm_2, evs_pkm_2, id_naturaleza_2, nuevo_equipo, session)
    if id_pkm_3 is not None:
        asignacion_datos_integrantes(id_pkm_3, generacion_equipo, id_movimientos_pkm_3, evs_pkm_3, id_naturaleza_3, nuevo_equipo, session)
    if id_pkm_4 is not None:
        asignacion_datos_integrantes(id_pkm_4, generacion_equipo, id_movimientos_pkm_4, evs_pkm_4, id_naturaleza_4, nuevo_equipo, session)
    if id_pkm_5 is not None:
        asignacion_datos_integrantes(id_pkm_5, generacion_equipo, id_movimientos_pkm_5, evs_pkm_5, id_naturaleza_5, nuevo_equipo, session)
    if id_pkm_6 is not None:
        asignacion_datos_integrantes(id_pkm_6, generacion_equipo, id_movimientos_pkm_6, evs_pkm_6, id_naturaleza_6, nuevo_equipo, session)

    session.add(nuevo_equipo)
    session.commit()
    session.refresh(nuevo_equipo)

    integrantes_publicos: List[IntegrantesEquipoPublic] = []
    ids_integrantes = []
    for integrante in nuevo_equipo.integrantes:
        if integrante.id not in ids_integrantes:
            query_moves_integrante = select(Movimientos).join(IntegrantesEquipo).where(IntegrantesEquipo.id == integrante.id, IntegrantesEquipo.move_id == Movimientos.id)
            moves_integrantes = session.exec(query_moves_integrante).all()
            integrantes_publicos.append(IntegrantesEquipoPublic(
                pokemon=integrante.pokemon,
                movimientos=moves_integrantes,
                naturaleza=integrante.naturaleza,
                evs=integrante.estadisticas
            ))
            ids_integrantes.append(integrante.id)

    
    equipo_publico = EquipoPublic(
        id=nuevo_equipo.id,
        nombre=nuevo_equipo.nombre,
        generacion=nuevo_equipo.generacion,
        integrantes=integrantes_publicos
    )
    
    return equipo_publico
    
def asignacion_datos_integrantes(id_pokemon: int, generacion_equipo, id_movimientos_seleccionados: list[int], ptos_evs: Estadisticas, id_naturaleza: int, equipo_a_asignar: Equipo, session: SessionDep) -> None:
    # Verificaciones
    if not verificar_generacion_del_pokemon(id_pokemon, generacion_equipo, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"El pokemon de id {id_pokemon} no pertenece a la generacion del equipo"
        )
    
    if id_movimientos_seleccionados is None or not verificar_movimientos_pokemon(id_pokemon, id_movimientos_seleccionados, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Algun movimiento del pokemon de id {id_pokemon} no son validos o no tiene movimientos"
        )
    
    if not verificar_evs(ptos_evs):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Los EVs no son validos, asegurarse de que la suma de los EVs no sea mayor a 510 y que cada EV no sea mayor a 255"
        )
    
    # Asignaciones
    nuevo_id = asignar_nueva_id_miembro(session)

    movimientos_elegidos: List["Movimientos"] = []
    for id_movimiento in id_movimientos_seleccionados:
        movimiento = buscar_movimientos_por_id(id_movimiento, session)
        movimientos_elegidos.append(movimiento)

    for movimiento_seleccionado, movimiento_elegido in zip(id_movimientos_seleccionados, movimientos_elegidos):
        nuevo_integrante = IntegrantesEquipo(
            id=nuevo_id,
            pokemon_id=id_pokemon,
            pokemon=buscar_pokemon_por_id(id_pokemon, session),
            equipo_id=equipo_a_asignar.id,
            equipo=equipo_a_asignar,
            move_id=movimiento_seleccionado,
            movimientos=movimiento_elegido,
            naturaleza_id=id_naturaleza,
            naturaleza=buscar_naturaleza_por_id(id_naturaleza, session)
        )
        session.add(nuevo_integrante)
        session.commit()
        session.refresh(nuevo_integrante)
        
    equipo_a_asignar.integrantes.append(nuevo_integrante)

    evs_nuevo_miembro = Estadisticas(
        member_id=nuevo_id,
        vida=ptos_evs.vida,
        ataque=ptos_evs.ataque,
        defensa=ptos_evs.defensa,
        ataque_especial=ptos_evs.ataque_especial,
        defensa_especial=ptos_evs.defensa_especial,
        velocidad=ptos_evs.velocidad
    )
    session.add(evs_nuevo_miembro)
    session.commit()
    session.refresh(evs_nuevo_miembro)

def asignar_nueva_id_miembro(session: SessionDep) -> int:
    query = select(IntegrantesEquipo)
    integrantes = session.exec(query).all()
    if integrantes:
        ultimo_integrante = max(integrantes, key=lambda integrante: integrante.id)
        nuevo_id = ultimo_integrante.id + 1
    else:
        nuevo_id = 1
    return nuevo_id

def buscar_pokemon_por_id(id_pokemon: int, session: SessionDep) -> Pokemon:
    query = select(Pokemon).where(Pokemon.id == id_pokemon)
    pokemon = session.exec(query).first()
    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado."
        )
    return pokemon

def buscar_movimientos_por_id(id_movimiento: int, session: SessionDep) -> Movimientos:
    query = select(Movimientos).where(Movimientos.id == id_movimiento)
    movimiento = session.exec(query).first()
    if not movimiento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento no encontrado."
        )
    return movimiento

def buscar_movimientos_del_pokemon(id_pokemon: int, session: SessionDep) -> list[MovimientosPokemon]:
    query = select(MovimientosPokemon).where(MovimientosPokemon.pokemon_id == id_pokemon)
    movimientos = session.exec(query).all()
    if not movimientos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movimientos del pokemon no encontrados."
        )
    return movimientos
    
def buscar_naturaleza_por_id(id_naturaleza: int, session: SessionDep) -> Naturaleza:
    query = select(Naturaleza).where(Naturaleza.id == id_naturaleza)
    naturaleza = session.exec(query).first()
    if not naturaleza:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Naturaleza no encontrada."
        )
    return naturaleza

def verificar_evs(evs: Estadisticas) -> bool:
    if evs.vida > 255 or evs.ataque > 255 or evs.defensa > 255 or evs.ataque_especial > 255 or evs.defensa_especial > 255 or evs.velocidad > 255:
        return False
    if evs.vida < 0 or evs.ataque < 0 or evs.defensa < 0 or evs.ataque_especial < 0 or evs.defensa_especial < 0 or evs.velocidad < 0:
        return False
    
    suma_evs = evs.vida + evs.ataque + evs.defensa + evs.ataque_especial + evs.defensa_especial + evs.velocidad

    if suma_evs > 510:
        return False
    return True

def verificar_generacion_del_pokemon(id_pokemon: int, generacion_equipo: int, session: SessionDep) -> bool:
    pokemon = buscar_pokemon_por_id(id_pokemon, session)
    if pokemon.generacion > generacion_equipo:
        return False
    return True

def verificar_movimientos_pokemon(id_pokemon: int, id_movimientos: list[int], session: SessionDep) -> bool:
    movimientos_aprendibles = buscar_movimientos_del_pokemon(id_pokemon, session)
    for id_movimiento in id_movimientos:
        if id_movimiento not in [movimiento_pokemon.move_id for movimiento_pokemon in movimientos_aprendibles]:
            return False
    return True
    

# @router.put("/{equipo_id}")
# def editar_equipo(equipo_id: int, equipo_nuevo: Equipo):
#     for equipo in equipos_db:
#         if equipo.id == equipo_id:
#             equipo.nombre = equipo_nuevo.nombre
#             equipo.pokemones = equipo_nuevo.pokemones
#             equipo.generacion = equipo_nuevo.generacion

#             return equipo
            
#     raise HTTPException(status_code=404, detail="El equipo a cambiar no fue encontrado")

# @router.get("/id/{equipo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
# def obtener_equipo_por_id(equipo_id: int) -> Equipo:
#     for equipo in equipos_db:
#         if equipo.id == equipo_id:
#             return equipo
#     raise HTTPException(
#         status_code= status.HTTP_404_NOT_FOUND, detail="Id de equipo inexistente"
#     )
    
# @router.delete("/{equipo_id}")
# def eliminar_equipo(equipo_id: int):
#     for i, equipo in enumerate(equipos):
#         if equipo.id == equipo_id:
#             equipo_eliminado = equipos.pop(i)
#             return {'mensaje': f"El equipo ({equipo_eliminado.nombre}) con id ({equipo_id}) ha sido eliminado."}
        
#     raise HTTPException(status_code=404, detail=f'No se ha encontrado al equipo con id ({equipo_id}).')

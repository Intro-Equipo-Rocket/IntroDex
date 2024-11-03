from fastapi import APIRouter, HTTPException, status
from app.modelos import *
from app.db.equipos_db import *
from app.db.naturaleza_db import *
from app.routers.pokemon import *
from typing import List
# from sqlmodel import Session, select
# from app.database import SessionDep

router = APIRouter()

@router.get("/pagina/{pagina}", response_model=List[Equipo])
def obtener_equipos(pagina: int, cantidad_equipos: int = 10):
    if pagina < 1 or cantidad_equipos < 1:
        raise HTTPException(status_code=404, detail="Algunos de los parámetros están siendo mal introducidas")
    
    skip = (pagina - 1) * 10
    equipos_pagina = equipos_db[skip:skip + cantidad_equipos]

    if not equipos_pagina:
        raise HTTPException(status_code=404, detail="No se encontraron equipos para esta página")
    
    return equipos_pagina

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_equipo(id_equipo: int, nombre_equipo: str, generacion_equipo: int,
                 id_pkm_1: int=None, movimientos_pkm_1: list[int]=None, id_naturaleza_1: int=None, evs_pkm_1: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_2: int=None, movimientos_pkm_2: list[int]=None, id_naturaleza_2: int=None, evs_pkm_2: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_3: int=None, movimientos_pkm_3: list[int]=None, id_naturaleza_3: int=None, evs_pkm_3: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_4: int=None, movimientos_pkm_4: list[int]=None, id_naturaleza_4: int=None, evs_pkm_4: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_5: int=None, movimientos_pkm_5: list[int]=None, id_naturaleza_5: int=None, evs_pkm_5: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
                 id_pkm_6: int=None, movimientos_pkm_6: list[int]=None, id_naturaleza_6: int=None, evs_pkm_6: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),) -> Equipo:
    
    # def crear_equipo(id_equipo: int, nombre_equipo: str, generacion_equipo: int, session: SessionDep,
    # id_pkm_1: int=None, movimientos_pkm_1: list[int]=None, id_naturaleza_1: int=None, evs_pkm_1: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
    # id_pkm_2: int=None, movimientos_pkm_2: list[int]=None, id_naturaleza_2: int=None, evs_pkm_2: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
    # id_pkm_3: int=None, movimientos_pkm_3: list[int]=None, id_naturaleza_3: int=None, evs_pkm_3: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
    # id_pkm_4: int=None, movimientos_pkm_4: list[int]=None, id_naturaleza_4: int=None, evs_pkm_4: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
    # id_pkm_5: int=None, movimientos_pkm_5: list[int]=None, id_naturaleza_5: int=None, evs_pkm_5: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0),
    # id_pkm_6: int=None, movimientos_pkm_6: list[int]=None, id_naturaleza_6: int=None, evs_pkm_6: Estadisticas=Estadisticas(vida=0, ataque=0, defensa=0, ataque_especial=0, defensa_especial=0, velocidad=0)) -> Equipo:
        # query = select(Equipo).where(Equipo.id == id_equipo)
        # equipo = session.exec(query).first()
        # if equipo:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST, detail="Ese equipo ya existe"
        #     )
        # if generacion_equipo not in range(1, 9):
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST, detail="La generación del equipo no es válida"
        #     )
        # nuevo_equipo: Equipo=Equipo(
        #     id=id_equipo,
        #     nombre=nombre_equipo,
        #     pokemones=[],
        #     generacion=generacion_equipo
        # )
    if generacion_equipo not in range(1, 9):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La generación del equipo no es válida"
        )
    for equipo in equipos:
        if id_equipo == equipo.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Ese equipo ya existe"
            )
    
    nuevo_equipo: Equipo=Equipo(
        id=id_equipo,
        nombre=nombre_equipo,
        pokemones=[],
        generacion=generacion_equipo
    )
    if id_pkm_1 is not None:
        asignacion_datos_integrantes(id_pkm_1, generacion_equipo, movimientos_pkm_1, evs_pkm_1, id_naturaleza_1, nuevo_equipo) # , session
    if id_pkm_2 is not None:
        asignacion_datos_integrantes(id_pkm_2, generacion_equipo, movimientos_pkm_2, evs_pkm_2, id_naturaleza_2, nuevo_equipo) # , session
    if id_pkm_3 is not None:
        asignacion_datos_integrantes(id_pkm_3, generacion_equipo, movimientos_pkm_3, evs_pkm_3, id_naturaleza_3, nuevo_equipo) # , session
    if id_pkm_4 is not None:
        asignacion_datos_integrantes(id_pkm_4, generacion_equipo, movimientos_pkm_4, evs_pkm_4, id_naturaleza_4, nuevo_equipo) # , session
    if id_pkm_5 is not None:
        asignacion_datos_integrantes(id_pkm_5, generacion_equipo, movimientos_pkm_5, evs_pkm_5, id_naturaleza_5, nuevo_equipo) # , session
    if id_pkm_6 is not None:
        asignacion_datos_integrantes(id_pkm_6, generacion_equipo, movimientos_pkm_6, evs_pkm_6, id_naturaleza_6, nuevo_equipo) # , session

    # session.add(nuevo_equipo)
    # session.commit()
    # session.refresh(nuevo_equipo)
    # return nuevo_equipo
    equipos.append(nuevo_equipo)
    return nuevo_equipo
    
def asignacion_datos_integrantes(id_pokemon: int, generacion_equipo, movimientos_seleccionados: list[int], ptos_evs: Estadisticas, id_naturaleza: int, equipo_a_asignar: Equipo) -> None: # , session
    naturaleza_pkm = obtener_naturaleza_por_id(id_naturaleza) # , session
    if not verificar_generacion_del_pokemon(id_pokemon, generacion_equipo): # , session
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"El pokemon de id {id_pokemon} no pertenece a la generacion del equipo"
        )
    if movimientos_seleccionados is None or not verificar_movimientos_pokemon(id_pokemon, movimientos_seleccionados): # , session
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Algun movimiento del pokemon de id {id_pokemon} no son validos o no tiene movimientos"
        )
    if not verificar_evs(ptos_evs):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Los EVs no son validos, asegurarse de que la suma de los EVs no sea mayor a 510 y que cada EV no sea mayor a 255"
        )
    
    equipo_a_asignar.pokemones.append(IntegranteEquipo(
            id_pokemon=naturaleza_pkm,
            pokemon=buscar_pokemon(id_pokemon),
            movimientos=movimientos_seleccionados,
            naturaleza=obtener_naturaleza_por_id(id_naturaleza),
            evs=ptos_evs
        )
    )
    
def obtener_naturaleza_por_id(id_naturaleza: int) -> Naturaleza: # , session
    # query = select(Naturaleza).where(Naturaleza.id == id_naturaleza)
    # naturaleza = session.exec(query).first()
    # if not naturaleza:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="Naturaleza no encontrada."
    #     )
    # return naturaleza
    for naturaleza in naturalezas:
        if naturaleza.id == id_naturaleza:
            return naturaleza
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Naturaleza no encontrada."
    )

def verificar_evs(evs: Estadisticas) -> bool:
    if evs.vida > 255 or evs.ataque > 255 or evs.defensa > 255 or evs.ataque_especial > 255 or evs.defensa_especial > 255 or evs.velocidad > 255:
        return False
    if evs.vida < 0 or evs.ataque < 0 or evs.defensa < 0 or evs.ataque_especial < 0 or evs.defensa_especial < 0 or evs.velocidad < 0:
        return False
    
    suma_evs = evs.vida + evs.ataque + evs.defensa + evs.ataque_especial + evs.defensa_especial + evs.velocidad

    if suma_evs > 510:
        return False
    return True

def verificar_generacion_del_pokemon(id_pokemon: int, generacion_equipo: int) -> bool: # , session
    pokemon = buscar_pokemon(id_pokemon) # , session
    if pokemon.generacion > generacion_equipo:
        return False
    return True

def verificar_movimientos_pokemon(id_pokemon: int, id_movimientos: list[int]) -> bool: # , session
    movimientos_aprendibles = obtener_movimientos_del_pokemon(id_pokemon) # , session
    h = 0
    while h < len(movimientos_aprendibles):
        i = 0
        movimiento_esta_en_la_lista = False
        while i < len(id_movimientos) and not movimiento_esta_en_la_lista:
            j = 0
            while j < len(movimientos_aprendibles) and not movimiento_esta_en_la_lista:
                if id_movimientos[i] == movimientos_aprendibles[j].id:
                    movimiento_esta_en_la_lista = True
                j += 1
            i += 1

        if not movimiento_esta_en_la_lista:
            return False
        h+=1

    if len(id_movimientos) > 4 or len(id_movimientos) < 1:
        return False
    return True

@router.put("/{equipo_id}")
def editar_equipo(equipo_id: int, equipo_nuevo: Equipo):
    for equipo in equipos_db:
        if equipo.id == equipo_id:
            equipo.nombre = equipo_nuevo.nombre
            equipo.pokemones = equipo_nuevo.pokemones
            equipo.generacion = equipo_nuevo.generacion

            return equipo
            
    raise HTTPException(status_code=404, detail="El equipo a cambiar no fue encontrado")

@router.get("/id/{equipo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def obtener_equipo_por_id(equipo_id: int) -> Equipo:
    for equipo in equipos_db:
        if equipo.id == equipo_id:
            return equipo
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND, detail="Id de equipo inexistente"
    )
    
@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int):
    for i, equipo in enumerate(equipos):
        if equipo.id == equipo_id:
            equipo_eliminado = equipos.pop(i)
            return {'mensaje': f"El equipo ({equipo_eliminado.nombre}) con id ({equipo_id}) ha sido eliminado."}
        
    raise HTTPException(status_code=404, detail=f'No se ha encontrado al equipo con id ({equipo_id}).')

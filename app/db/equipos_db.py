from app.modelos import *

equipos = [
    Equipo(
        id=1, 
        nombre='Equipo 1', 
        pokemones=[
            IntegranteEquipo(
                pokemon=Pokemon(
                    imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
                    id=25,
                    nombre="Pikachu",
                    tipos=[13],
                    altura=4,
                    peso=60,
                    habilidades=[9],
                    habilidad_oculta=31,
                    vida=35,
                    ataque=55,
                    defensa=40,
                    ataque_especial=50,
                    defensa_especial=50,
                    velocidad=90,
                    total=320,
                    grupo_huevo=[25, 5],
                    evoluciones=[26],
                    imagenes_evoluciones=["https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png"],
                    movimientos_aprendibles_nivel=[33, 84, 98],
                    movimientos_aprendibles_evolucion=[85],
                    movimientos_aprendibles_tms=[24, 25],
                    movimientos_aprendibles_huevo=[],
                    debilidades_tipo=[100, 100, 200, 100, 0, 100, 100, 100, 100, 100, 200, 50, 50, 100, 100, 50, 100, 100],
                    generacion=1
                ),
                movimientos=[14, 15, 22, 33, 34, 35, 38, 45, 72, 73, 74, 75],
                naturaleza=Naturaleza(id=1, nombre="Fuerte", stat_perjudicada_id=2, stat_mejorada_id=2),
                evs=Estadisticas(vida=25, ataque=50, defensa=100, ataque_especial=40, defensa_especial=110, velocidad=25)
            )
        ],
        generacion=1 
    )
]


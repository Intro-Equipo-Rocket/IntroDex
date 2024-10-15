from app.modelos import IntegranteEquipo, Equipo

equipos_db = [
    Equipo(id=1, 
           nombre='Equipo 1', 
           pokemones=[
               IntegranteEquipo(imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
                                id=1,
                                nombre="bulbasaur",
                                tipos=[12, 4],
                                habilidades=[65],
                                habilidad_oculta=34,
                                vida=45,
                                ataque=49,
                                defensa=49,
                                ataque_especial=65,
                                defensa_especial=65,
                                velocidad=45,
                                total=318,
                                movimientos=[14, 15, 22, 33, 34, 35, 38, 45, 72, 73, 74, 75])
           ])
]
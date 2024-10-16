from app.modelos import Pokemon


pokemones: list[Pokemon] = [
    Pokemon(
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
        imagenes_evoluciones=[
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png"
        ],
        movimientos_aprendibles_nivel=[
            33,
            84,
            98,
        ],
        movimientos_aprendibles_evolucion=[85],
        movimientos_aprendibles_tms=[24, 25],
        movimientos_aprendibles_huevo=[],
        debilidades_tipo=[
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
        ],
    ),
    Pokemon(
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/658.png",
        id=658,
        nombre="Greninja",
        tipos=[11, 17],
        altura=15,
        peso=400,
        habilidades=[67],
        habilidad_oculta=168,
        grupo_huevo=[658, 2],
        vida=72,
        ataque=95,
        defensa=67,
        ataque_especial=103,
        defensa_especial=71,
        velocidad=122,
        total=530,
        evoluciones=None,  # Greninja no tiene evoluciones
        imagenes_evoluciones=None,  # No hay imágenes de evoluciones
        movimientos_aprendibles_nivel=[
            1,
            3,
            6,
            10,
            14,
            19,
            23,
            28,
            33,
            36,
            42,
            49,
            56,
            68,
        ],  # IDs de movimientos aprendibles por nivel
        movimientos_aprendibles_evolucion=[],  # IDs de movimientos aprendibles por evolución
        movimientos_aprendibles_tms=[
            13,
            14,
            15,
            21,
            27,
            32,
            42,
            44,
            45,
            46,
            48,
            55,
            56,
            62,
            67,
            68,
            75,
            80,
            81,
            87,
            88,
            89,
            90,
            91,
            92,
            100,
        ],  # IDs de movimientos aprendibles por TMs
        movimientos_aprendibles_huevo=[170, 171, 172, 173, 174],
        debilidades_tipo=[
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
        ],
    ),

]

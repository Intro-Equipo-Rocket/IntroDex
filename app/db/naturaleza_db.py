from app.modelos import Naturaleza

naturalezas: list[Naturaleza] = [
    Naturaleza(
        id=1,
        nombre="Audaz",
        stat_perjudicada_id=5,
        stat_mejorada_id=1
    ),
    Naturaleza(
        id=2,
        nombre="Osada",
        stat_perjudicada_id=5,
        stat_mejorada_id=2
    ),
    Naturaleza(
        id=3,
        nombre="Cauta",
        stat_perjudicada_id=5,
        stat_mejorada_id=3
    ),
    Naturaleza(
        id=4,
        nombre="Alegre",
        stat_perjudicada_id=5,
        stat_mejorada_id=4
    )
]
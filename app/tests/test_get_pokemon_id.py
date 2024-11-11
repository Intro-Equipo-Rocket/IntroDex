from fastapi.testclient import TestClient
from sqlmodel import Session

from app.modelos import *


def test_get_pokemon_por_id_existente(db_session: Session, client: TestClient) -> None:
    db_session.add_all(
        [
            TiposPokemon(type_id=1, pokemon_id=132),
        ]
    )
    db_session.commit()

    db_session.add_all(
        [
            HabilidadesPokemon(pokemon_id=132, ability_id=7, es_oculta=False),
            HabilidadesPokemon(pokemon_id=132, ability_id=150, es_oculta=True),
        ]
    )
    db_session.commit()

    db_session.add_all(
        [
            GrupoHuevoPokemon(species_id=13, egg_group_id=13),
        ]
    )
    db_session.commit()

    db_session.add_all(
        [
            MovimientosPokemon(pokemon_id=132, move_id=144, id_metodo=1, nivel=0),
        ]
    )
    db_session.commit()

    db_session.add_all(
        [
            StatsDelPokemon(pokemon_id=132, stat_id=1, base_stat=48),
            StatsDelPokemon(pokemon_id=132, stat_id=2, base_stat=48),
            StatsDelPokemon(pokemon_id=132, stat_id=3, base_stat=48),
            StatsDelPokemon(pokemon_id=132, stat_id=4, base_stat=48),
            StatsDelPokemon(pokemon_id=132, stat_id=5, base_stat=48),
            StatsDelPokemon(pokemon_id=132, stat_id=6, base_stat=48),
        ]
    )
    db_session.commit()

    # verificar si puede obtener a ditto por pokemon_id.
    response = client.get("/pokemons/id/132")
    assert response.status_code == 200

    data = response.json()

    assert data["nombre"] == "ditto"
    assert (
        data["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png"
    )
    assert data["altura"] == 3
    assert data["peso"] == 40
    assert data["generacion"] == 1
    assert data["id_evolucion"] is None
    assert data["imagen_evolucion"] == ""

    assert len(data["tipos"]) == 1
    assert data["tipos"][0]["nombre"] == "Normal"

    assert len(data["habilidades"]) == 2
    assert sorted([hab["nombre"] for hab in data["habilidades"]]) == [
        "Flexibilidad",
        "Impostor",
    ]

    assert len(data["grupo_huevo"]) == 1
    assert data["grupo_huevo"][0]["nombre"] == "Ditto"

    for stat in data["stats"]:
        assert stat["base_stat"] == 48

    assert len(data["movimientos"]) == 1
    assert data["movimientos"][0]["nombre"] == "Transformación"

    # verificar si puede obtener a ditto por identifier.
    response = client.get("/pokemons/nombre/ditto")
    assert response.status_code == 200

    # verificar si no existe un pokemon.
    response = client.get("/pokemons/id/9999999999999999")
    assert response.status_code == 404

    response = client.get("/pokemons/nombre/dadafgadasdafasd")
    assert response.status_code == 404

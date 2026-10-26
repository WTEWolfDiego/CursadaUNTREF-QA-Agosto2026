import pytest
import requests

API = "https://pokeapi.co/api/v2"


def consultar(recurso):
    respuesta = requests.get(f"{API}/{recurso}", timeout=15)
    assert respuesta.status_code == 200, f"{recurso} respondio {respuesta.status_code}"
    return respuesta.json()


@pytest.fixture(scope="module")
def berry_uno():
    return consultar("berry/1")


def test_caso1_berry_1(berry_uno):
    assert berry_uno["size"] == 20
    assert berry_uno["soil_dryness"] == 15
    assert berry_uno["firmness"]["name"] == "soft"


def test_caso2_berry_2_contra_berry_1(berry_uno):
    berry_dos = consultar("berry/2")

    assert berry_dos["firmness"]["name"] == "super-hard"
    assert berry_dos["size"] > berry_uno["size"]
    assert berry_dos["soil_dryness"] == berry_uno["soil_dryness"]


def test_caso3_pikachu():
    pikachu = consultar("pokemon/pikachu/")

    assert 10 < pikachu["base_experience"] < 1000
    assert "electric" in {t["type"]["name"] for t in pikachu["types"]}

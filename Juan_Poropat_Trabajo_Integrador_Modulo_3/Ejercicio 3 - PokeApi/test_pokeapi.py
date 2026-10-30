import pytest
import requests

BASE_URL = "https://pokeapi.co/api/v2"
TIMEOUT = 10


def consultar(endpoint):
    """Hace un GET al endpoint, valida el status 200 y devuelve el JSON."""
    respuesta = requests.get(f"{BASE_URL}/{endpoint}", timeout=TIMEOUT)
    assert respuesta.status_code == 200, (
        f"GET /{endpoint} devolvió status {respuesta.status_code}"
    )
    return respuesta.json()


@pytest.fixture(scope="module")
def berry_1():
    return consultar("berry/1")


@pytest.fixture(scope="module")
def berry_2():
    return consultar("berry/2")


@pytest.fixture(scope="module")
def pikachu():
    return consultar("pokemon/pikachu")


def test_caso1_berry_1(berry_1):
    size = berry_1["size"]
    assert size == 20, f"size esperado: 20, obtenido: {size}"
    print(f"(Caso 1) size = {size}")

    soil_dryness = berry_1["soil_dryness"]
    assert soil_dryness == 15, f"soil_dryness esperado: 15, obtenido: {soil_dryness}"
    print(f"(Caso 1) soil_dryness = {soil_dryness}")

    firmness = berry_1["firmness"]["name"]
    assert firmness == "soft", f"firmness esperado: soft, obtenido: {firmness}"
    print(f"(Caso 1) firmness = {firmness}")


def test_caso2_berry_2(berry_1, berry_2):
    firmness = berry_2["firmness"]["name"]
    assert firmness == "super-hard", f"firmness esperado: super-hard, obtenido: {firmness}"
    print(f"(Caso 2) firmness = {firmness}")

    # Comparación contra los valores obtenidos en el Caso 1
    assert berry_2["size"] > berry_1["size"], (
        f"size de berry/2 ({berry_2['size']}) no es mayor al de berry/1 ({berry_1['size']})"
    )
    print(f"(Caso 2) size {berry_2['size']} > {berry_1['size']} (berry/1)")

    assert berry_2["soil_dryness"] == berry_1["soil_dryness"], (
        f"soil_dryness de berry/2 ({berry_2['soil_dryness']}) "
        f"distinto al de berry/1 ({berry_1['soil_dryness']})"
    )
    print(f"(Caso 2) soil_dryness {berry_2['soil_dryness']} == {berry_1['soil_dryness']} (berry/1)")


def test_caso3_pikachu(pikachu):
    experiencia = pikachu["base_experience"]
    assert 10 < experiencia < 1000, (
        f"base_experience fuera de rango (10, 1000): {experiencia}"
    )
    print(f"(Caso 3) base_experience = {experiencia}, dentro del rango 10-1000")

    tipos = {t["type"]["name"] for t in pikachu["types"]}
    assert "electric" in tipos, f"tipos obtenidos: {tipos}"
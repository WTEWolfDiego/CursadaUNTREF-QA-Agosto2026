import requests


def obtener_json(url):
    respuesta = requests.get(url, timeout=10)
    assert respuesta.status_code == 200
    return respuesta.json()


def test_caso1_berry_1(base_url_api):
    berry = obtener_json(f"{base_url_api}/berry/1")

    assert berry["size"] == 20
    assert berry["soil_dryness"] == 15
    assert berry["firmness"]["name"] == "soft"


def test_caso2_berry_2(base_url_api):
    berry_1 = obtener_json(f"{base_url_api}/berry/1")
    berry_2 = obtener_json(f"{base_url_api}/berry/2")

    assert berry_2["firmness"]["name"] == "super-hard"
    assert berry_2["size"] > berry_1["size"]
    assert berry_2["soil_dryness"] == berry_1["soil_dryness"]


def test_caso3_pikachu(base_url_api):
    pikachu = obtener_json(f"{base_url_api}/pokemon/pikachu/")

    assert 10 < pikachu["base_experience"] < 1000

    tipos = [tipo["type"]["name"] for tipo in pikachu["types"]]
    assert "electric" in tipos

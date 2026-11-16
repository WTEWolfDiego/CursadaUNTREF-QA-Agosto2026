
import requests

def test_berry_1():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert data["size"] == 20
    assert data["soil_dryness"] == 15
    assert data["firmness"]["name"] == "soft"

def test_berry_2():
    url = "https://pokeapi.co/api/v2/berry/2"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200

    data = response.json()

    assert data["firmness"]["name"] == "super-hard"
    assert data["size"] > 20
    assert data["soil_dryness"] == 15
def test_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert data["base_experience"] > 10
    assert data["base_experience"] < 1000
    assert data["types"][0]["type"]["name"] == "electric"   
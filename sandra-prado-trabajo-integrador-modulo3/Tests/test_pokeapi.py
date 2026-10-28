import requests
 
 
BASE_URL = "https://pokeapi.co/api/v2"
 
 
def test_berry_1():
 
    response = requests.get(

        f"{BASE_URL}/berry/1",

        timeout=10

    )
 
    # Verificar que la API responda correctamente

    assert response.status_code == 200
 
    data = response.json()
 
    print("Berry 1")

    print("Size:", data["size"])

    print("Soil dryness:", data["soil_dryness"])

    print("Firmness:", data["firmness"]["name"])
 
    # Validaciones solicitadas

    assert data["size"] == 20

    assert data["soil_dryness"] == 15

    assert data["firmness"]["name"] == "soft"
 
 
def test_berry_2():
 
    # Obtener berry 1 para poder comparar

    response_berry_1 = requests.get(

        f"{BASE_URL}/berry/1",

        timeout=10

    )
 
    assert response_berry_1.status_code == 200
 
    berry_1 = response_berry_1.json()
 
    # Obtener berry 2

    response_berry_2 = requests.get(

        f"{BASE_URL}/berry/2",

        timeout=10

    )
 
    assert response_berry_2.status_code == 200
 
    berry_2 = response_berry_2.json()
 
    print("Berry 2")

    print("Size:", berry_2["size"])

    print("Soil dryness:", berry_2["soil_dryness"])

    print("Firmness:", berry_2["firmness"]["name"])
 
    # Firmness debe ser super-hard

    assert berry_2["firmness"]["name"] == "super-hard"
 
    # Size debe ser mayor al berry 1

    assert berry_2["size"] > berry_1["size"]
 
    # Soil dryness debe ser igual al berry 1

    assert berry_2["soil_dryness"] == berry_1["soil_dryness"]
 
 
def test_pikachu():
 
    response = requests.get(

        f"{BASE_URL}/pokemon/pikachu/",

        timeout=10

    )
 
    assert response.status_code == 200
 
    data = response.json()
 
    print("Pikachu")

    print("Base experience:", data["base_experience"])
 
    # Verificar experiencia

    assert data["base_experience"] > 10

    assert data["base_experience"] < 1000
 
    # Obtener los tipos del Pokémon

    tipos = [

        tipo["type"]["name"]

        for tipo in data["types"]

    ]
 
    print("Tipos:", tipos)
 
    # Verificar tipo electric

    assert "electric" in tipos
 
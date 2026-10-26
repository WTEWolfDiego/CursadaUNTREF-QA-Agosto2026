import requests

# CASO 1 - Berry 1

def test_caso_1():

    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)

    # Verifico que el status code sea 200
    assert response.status_code == 200, f"Status esperado 200, pero fue {response.status_code}"

    json_data = response.json()

    # Verifico que exista la clave size
    assert "size" in json_data, "No se encontró la clave size"

    # Verifico que size sea 20
    assert json_data["size"] == 20, "El size debe ser 20"

    # Verifico que soil_dryness sea 15
    assert json_data["soil_dryness"] == 15, "El soil_dryness debe ser 15"

    # Verifico que firmness name sea soft
    assert json_data["firmness"]["name"] == "soft", "El firmness debe ser soft"

# CASO 2 - Berry 2

def test_caso_2():

    url = "https://pokeapi.co/api/v2/berry/2"
    response = requests.get(url)

    assert response.status_code == 200, f"Status esperado 200, pero fue {response.status_code}"

    json_data = response.json()

    # Obtengo Berry 1 para la comparación
    response_berry1 = requests.get("https://pokeapi.co/api/v2/berry/1")
    assert response_berry1.status_code == 200, "No se pudo obtener Berry 1"

    json_data1 = response_berry1.json()

    # Verifico que firmness name sea super-hard
    assert json_data["firmness"]["name"] == "super-hard", "El firmness debe ser super-hard"

    # Verifico que size sea mayor al de Berry 1
    assert json_data["size"] > json_data1["size"], "El size debe ser mayor al de Berry 1"

    # Verifico que soil_dryness sea igual al de Berry 1
    assert json_data["soil_dryness"] == json_data1["soil_dryness"], "El soil_dryness debe ser igual al de Berry 1"

# CASO 3 - Pikachu

def test_caso_3():

    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    response = requests.get(url)

    assert response.status_code == 200, f"Status esperado 200, pero fue {response.status_code}"

    json_data = response.json()

    # Verifico que la experiencia base sea mayor a 10 y menor a 1000
    assert json_data["base_experience"] > 10, "La experiencia base debe ser mayor a 10"
    assert json_data["base_experience"] < 1000, "La experiencia base debe ser menor a 1000"

    # Verifico que el tipo sea electric
    assert json_data["types"][0]["type"]["name"] == "electric", "El tipo debe ser electric"

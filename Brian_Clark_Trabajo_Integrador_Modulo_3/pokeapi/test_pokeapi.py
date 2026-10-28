import pytest
import requests

#Pongo como BASE_URL la URL de pokeapi para después simplemente añadir los endpoints necesarios
BASE_URL = "https://pokeapi.co/api/v2"

#Caso 1
def test_get_berry_1():
    #Acá le mando el GET al endpoint de la berry número 1, valido que el status code sea 200 y transformo la respuesta en json para poder trabajarla
    response_1 = requests.get(f"{BASE_URL}/berry/1")
    assert response_1.status_code == 200
    berry_1 = response_1.json()
    
    #En este bloque hago todas las validaciones solicitadas en el Caso 1
    assert berry_1["size"] == 20
    assert berry_1["soil_dryness"] == 15
    assert berry_1["firmness"]["name"] == "soft"

#Caso 2
def test_comparar_berries_1_y_2():
    #Acá hago las llamadas para comparar la berry 1 con la berry 2, posiblemente haya una solución más elegante para crear una función en la cual solamente pongo un argumento (1 o 2), creo que seríá con decorators no? O parametrizando la función
    response_1 = requests.get(f"{BASE_URL}/berry/1")
    assert response_1.status_code == 200
    berry_1 = response_1.json()
    response_2 = requests.get(f"{BASE_URL}/berry/2")
    assert response_2.status_code == 200
    berry_2 = response_2.json()
    
    #En este bloque hago todas las validaciones solicitadas en el Caso 2 que incluyen la comparación con la berry 1
    assert berry_2["firmness"]["name"] == "super-hard"
    assert berry_2["size"] > berry_1["size"]
    assert berry_2["soil_dryness"] == berry_1["soil_dryness"]

#Caso 3
def test_pikachu():
    #Llamada GET a pikachu para obtener la data, verificar que me devolvió un 200 OK y transformar la response en JSON
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
    assert response.status_code == 200
    pikachu = response.json()

    #Verificaciones solicitadas en el Caso 3
    assert 10 < pikachu["base_experience"] < 1000
    #Acá me trabé un poco porque resulta que los tipos de pokemon están en una lista de tipos con slots para cada tipo así que tuve que recorrerla para poder hacer el assert verificando que "electric" esté en la lista tipos que creé
    tipos = []
    for tipo in pikachu["types"]:
        tipos.append(tipo["type"]["name"])
    assert "electric" in tipos
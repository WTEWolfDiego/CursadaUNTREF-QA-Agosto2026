
import requests

def test_verificar_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"

    respuesta = requests.get(url)

    assert respuesta.status_code == 200

    datos = respuesta.json()

    experiencia = datos["base_experience"]
    tipo = datos["types"][0]["type"]["name"]

    print("Experiencia base:", experiencia)
    assert experiencia > 10
    print("La experiencia es mayor a 10: SI CUMPLE")

    assert experiencia < 1000
    print("La experiencia es menor a 1000: SI CUMPLE")

    print("Tipo de Pikachu:", tipo)
    assert tipo == "electric"
    print("El tipo es electric: SI CUMPLE")

    print("Todas las pruebas pasaron correctamente")



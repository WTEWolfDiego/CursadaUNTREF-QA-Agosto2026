import requests

def verificar_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"

    respuesta = requests.get(url)
    datos = respuesta.json()

    experiencia = datos["base_experience"]
    tipo = datos["types"][0]["type"]["name"]

    assert experiencia > 10
    assert experiencia < 1000
    assert tipo == "electric"

    return "Todas las pruebas pasaron correctamente"


print(verificar_pikachu())
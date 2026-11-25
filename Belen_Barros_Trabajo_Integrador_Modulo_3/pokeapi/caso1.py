import requests

def verificar_berry1():
    url = "https://pokeapi.co/api/v2/berry/1"

    respuesta = requests.get(url)
    datos = respuesta.json()

    size = datos["size"]
    soil_dryness = datos["soil_dryness"]
    firmness = datos["firmness"]["name"]

    assert size == 20
    assert soil_dryness == 15
    assert firmness == "soft"

    return "Todas las pruebas pasaron correctamente"


print(verificar_berry1())
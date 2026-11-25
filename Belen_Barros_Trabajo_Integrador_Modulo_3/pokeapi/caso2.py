import requests

def verificar_berry2():
    url = "https://pokeapi.co/api/v2/berry/2"

    respuesta = requests.get(url)
    datos = respuesta.json()

    firmness = datos["firmness"]["name"]
    size = datos["size"]
    soil_dryness = datos["soil_dryness"]

    assert firmness == "super-hard"
    assert size > 20
    assert soil_dryness == 15

    return "Todas las pruebas pasaron correctamente"


print(verificar_berry2())

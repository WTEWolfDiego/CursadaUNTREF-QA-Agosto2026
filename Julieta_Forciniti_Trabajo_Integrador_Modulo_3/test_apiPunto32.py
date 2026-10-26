##### Sitio POKE API
####CASO 1-----------------------------------------------------------------------------------------------------------
import requests

def test_api(): 
    respuesta = requests.get("https://pokeapi.co/api/v2/berry/1")
    datos = respuesta.json()
    assert (datos["size"])==20
    assert(datos["soil_dryness"])== 15
    assert(datos ["firmness"]["name"])== "soft"

#print(datos["size"])
#print (datos["soil_dryness"])
#print (datos ["firmness"]["name"])

#### CASO2---------------------------------------------------------------------------------------------------------
def test_api2():
    respuesta1 = requests.get("https://pokeapi.co/api/v2/berry/1")
    datos1 = respuesta1.json()

    respuesta2 = requests.get("https://pokeapi.co/api/v2/berry/2")
    datos2 = respuesta2.json()

    assert datos2["size"] > datos1["size"]
    assert datos2["soil_dryness"] == datos1["soil_dryness"]
    assert datos2["firmness"]["name"] == "super-hard"
     
     
 ####CASO 3-----------------------------------------------------------------------------------------------------
 #"base_experience":112
 #"type":{"name":"electric","url":"https://pokeapi.co/api/v2/type/13/"}}]
     
def test_api3():
    respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    datos = respuesta.json()
      
    assert (datos["base_experience"]) > 10 and (datos["base_experience"]) < 1000
    assert datos["types"][0]["type"]["name"] == "electric"
       
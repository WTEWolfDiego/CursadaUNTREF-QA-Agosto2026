import requests

def test_prueba_berry2():

    berry1_url="https://pokeapi.co/api/v2/berry/1"
    respuesta1=requests.get(berry1_url)
    datosberry1=respuesta1.json()

    berry1_size=datosberry1['size']
    berry1_soil_dryness=datosberry1['soil_dryness']
    berry1_firmness_name=datosberry1['firmness']['name']

    berry2_url="https://pokeapi.co/api/v2/berry/2"
    respuesta2=requests.get(berry2_url)
    datosberry2=respuesta2.json()
    print(respuesta2.json())

    berry2_firmness_name=datosberry2['firmness']['name']
    berry2_size=datosberry2['size']
    berry2_soil_dryness=datosberry2['soil_dryness']
    print()

    assert berry2_firmness_name == 'super-hard'
    if berry2_firmness_name == 'super-hard':
        print("firmness_name es super-hard")
    else:
        print("NO es super-hard")
    print()

    assert berry2_size > berry1_size
    if berry2_size > berry1_size:
        print("Size caso_2 es mayor a Size caso_1")
    else:
        print("ERROR")
    print()

    assert berry2_soil_dryness == berry1_soil_dryness 
    if berry2_soil_dryness == berry1_soil_dryness:
        print("Son iguales")
    else:
        print("NO son iguales")

    print()

    print ("Se cumplen todos los Asserts")
    print()
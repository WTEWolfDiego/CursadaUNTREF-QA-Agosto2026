
import requests

def test_prueba_berry1():
    berry1_url="https://pokeapi.co/api/v2/berry/1"
    respuesta=requests.get(berry1_url)
    datosberry1=respuesta.json()
    print(respuesta.json())

    berry1_size=datosberry1['size']
    berry1_soil_dryness=datosberry1['soil_dryness']
    berry1_firmness_name=datosberry1['firmness']['name']
    print()

    assert berry1_size == 20
    if berry1_size==20:
        print("size es 20")
    else:
        print("size NO es 20")
    print()
    
    assert berry1_soil_dryness == 15
    if berry1_soil_dryness == 15:
        print("soildryness es 15")
    else:
        print("soildryness NO es 15")
    print()
    
    assert berry1_firmness_name == 'soft'
    if berry1_firmness_name =='soft':
        print("firmness_name es soft")
    else:
        print("firmness_name NO es soft")
    print()

    print ({berry1_size},{berry1_soil_dryness},{berry1_firmness_name})
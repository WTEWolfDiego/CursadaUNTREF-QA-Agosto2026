# 2) Sitio: Poke Api (https://pokeapi.co/api/v2)
# Caso 1 
# ● Hacer un get a berry/1
# ● Verificar que el size sea 20
# ● Verificar que el soil_dryness sea 15 
# ● Verificar que en firmness, el name sea soft.

import requests
import pytest

#TODO: assertions de vacío, strip, etc entre ints y strings no funcionaron

# RECORDATORIO: PYTEST NO TOMA LOS CAMBIOS A MENOS QUE GUARDES EXPRESAMENTE, POR ESO SIGUE FALLANDO

#método
def test_get_berry1():
    # apunta a la api
    url = "https://pokeapi.co/api/v2/berry/1"
    

    # asignación de la respuesta de la url a una variable
    respuesta = requests.get(url)

    # 1 Afirmar que el status code es 200 / Clase 19 
    assert respuesta.status_code == 200, f"Status esperado 200, pero fue {respuesta.status_code}"
    print("Caso 1: Verificación de status exitosa: Status code = 200")

    # pasaje de la respuesta del GET a la API a json para manipularlo y obtener datos
    respuesta_json = respuesta.json()

    #una vez asignado el json, se puede ubicar dentro del mismo información por clave, valor
    # verificaciones tomadas de clase 19 - Existencia de la clave, si es numérica y si tiene información o está vacía
    assert 'size' in respuesta_json, "No existe la clave 'size'"
    assert isinstance(respuesta_json['size'], int), "El campo 'size' no es numerico"
    # assert respuesta_json['size'].strip() != "", "El campo 'size' está vacío"

    # Verificar que el size sea 20
    assert respuesta_json["size"] == 20, f"La clave 'size' tiene un valor distinto al esperado (20)"
    print("Verificación de clave-valor 'size' exitosa: size = 20")

    # verificaciones tomadas de clase 19 - Existencia de la clave, si es numérica y si tiene información o está vacía
    assert "soil_dryness" in respuesta_json, "No existe la clave 'soil dryness'"
    assert isinstance(respuesta_json["soil_dryness"], int), "El campo 'soil dryness' no es numerico"
    # assert respuesta_json["soil_dryness"].strip() != "", "El campo 'soil dryness' está vacío"

    ### Verificar que el "soil_dryness" sea 15
    assert respuesta_json["soil_dryness"] == 15, f"La clave 'soil dryness' tiene un valor distinto al esperado (15)"
    print("Verificación de clave-valor 'soil_dryness' exitosa: soil_dryness = 15")

    # verificaciones tomadas de clase 19 - Existencia de la clave, si es numérica y si tiene información o está vacía
    assert "firmness" in respuesta_json, "No existe la clave 'firmness'"
    #assert isinstance(respuesta_json["firmness"]["name"], int), "El campo 'name' dentro de 'firmness' no contiene una cadena de caracteres"
    #assert respuesta_json["firmness"]["name"].strip() != "", "El campo 'name' dentro de 'firmness' está vacío"

    ### Verificar que en firmness el "name" sea "soft".
    # name está dentro de firmness, como un diccionario. Por eso el acceso doble
    firmness_berry1 = respuesta_json["firmness"]["name"]
    assert respuesta_json["firmness"]["name"] == "soft", f"La clave 'name' dentro de 'firmness' tiene un valor distinto al esperado (soft)"
    print("Verificación de clave-valor 'firmness - name' exitosa: firmness - name = soft")

    print("Verificación de Caso 1 terminada. No se encontraron errores")


    
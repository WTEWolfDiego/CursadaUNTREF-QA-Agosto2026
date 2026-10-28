
# Caso 2 
# ● Hacer un get a berry/2 
# ● Verificar que en firmness, el name sea super-hard 
# ● Verificar que el size sea mayor al del punto anterior 
# ● Verificar que el soil_dryness sea igual al del punto anterior


import requests
import pytest

#TODO: assertions de vacío, strip, etc entre ints y strings no funcionaron

#método
def test_get_berry2():
    # apunta a la api
    url = "https://pokeapi.co/api/v2/berry/2"

    # asignación de la respuesta de la url a una variable
    respuesta = requests.get(url)

    # 1 Afirmar que el status code es 200 / Clase 19 
    assert respuesta.status_code == 200, f"Status esperado 200, pero fue {respuesta.status_code}"
    print("Caso 2: Verificación de status exitosa: Status code = 200")

    # pasaje de la respuesta del GET a la API a json para manipularlo y obtener datos
    respuesta_json = respuesta.json()


    # verificaciones tomadas de clase 19 - Existencia de la clave, si es numérica y si tiene información o está vacía
    assert "firmness" in respuesta_json, "No existe la clave 'firmness'"
    #assert isinstance(respuesta_json["firmness"]["name"], int), "El campo 'name' dentro de 'firmness' no contiene una cadena de caracteres"
    #assert respuesta_json["firmness"]["name"].strip() != "", "El campo 'name' dentro de 'firmness' está vacío"

    ### Verificar que en firmness el "name" sea "super-hard".
    # name está dentro de firmness, como un diccionario. Por eso el acceso doble
    firmness_berry1 = respuesta_json["firmness"]["name"]
    assert respuesta_json["firmness"]["name"] == "super-hard", f"La clave 'name' dentro de 'firmness' tiene un valor distinto al esperado (soft)"
    print("Verificación de clave-valor 'firmness - name' exitosa: firmness - name = super-hard")


    #una vez asignado el json, se puede ubicar dentro del mismo información por clave, valor
    # verificaciones tomadas de clase 19 - Existencia de la clave, si es numérica y si tiene información o está vacía
    assert "size" in respuesta_json, "No existe la clave 'size'"
    # assert isinstance(respuesta_json["size"], int), "El campo 'size' no es numerico"
    # assert respuesta_json["size"].strip() != "", "El campo 'size' está vacío"

    # Verificar que el size sea mayor que el anterior (20) 
    # TODO: luego de la entrega, revisar si hubiera sido posible asignarlo a una variable para no hardcodearlo.
    # supongo que debería ser en un solo .py
    assert respuesta_json["size"] > 20, f"La clave 'size' tiene un valor distinto al esperado (mayor a 20)"
    print("Verificación de clave-valor 'size' exitosa: size > 20")

    # verificaciones tomadas de clase 19 - Existencia de la clave, si es numérica y si tiene información o está vacía
    assert "soil_dryness" in respuesta_json, "No existe la clave 'soil dryness'"
    # assert isinstance(respuesta_json["soil_dryness"], int), "El campo 'soil dryness' no es numerico"
    # assert respuesta_json["soil_dryness"].strip() != "", "El campo 'soil dryness' está vacío"

    ### Verificar que el "soil_dryness" sea igual al anterior (15)
    assert respuesta_json["soil_dryness"] == 15, "La clave 'soil dryness' tiene un valor distinto al esperado (15)"
    print("Verificación de clave-valor 'soil_dryness' exitosa: soil_dryness = 15")


    print("Verificación de Caso 2 terminada. No se encontraron errores")

    
# Importamos la librería requests.
# Permite realizar solicitudes HTTP a una API.
import requests


# Definimos la URL base de PokeAPI.
# Esta dirección será utilizada por todos los casos de prueba.
BASE_URL = 'https://pokeapi.co/api/v2'


# ==========================================================
# FUNCIÓN AUXILIAR: OBTENER DATOS JSON DE LA API
# ==========================================================

def obtener_json(ruta):

    # Realizamos una solicitud HTTP GET.
    # f'{BASE_URL}/{ruta}' construye la URL completa.
    # timeout=15 establece un tiempo máximo de espera
    # de 15 segundos para la solicitud.
    respuesta = requests.get(
        f'{BASE_URL}/{ruta}',
        timeout=15
    )

    # Mostramos la URL consultada.
    print(f'\nURL consultada: {BASE_URL}/{ruta}')

    # Mostramos el código HTTP recibido.
    print(f'Código HTTP: {respuesta.status_code}')

    # Verificamos que la respuesta HTTP sea 200 (OK).
    # Si el código es diferente, la prueba falla
    # y muestra el mensaje de error correspondiente.
    assert respuesta.status_code == 200, (
        f'Error HTTP: {respuesta.status_code}'
    )

    # Convertimos el contenido JSON de la respuesta
    # a un diccionario de Python y lo devolvemos.
    return respuesta.json()


# ==========================================================
# CASO 1: VALIDAR LOS DATOS DE BERRY/1
# ==========================================================

def test_berry_1():

    # Llamamos a la función obtener_json().
    # Consultamos el endpoint berry/1.
    # Guardamos la respuesta en la variable berry.
    berry = obtener_json('berry/1')

    # Mostramos los datos obtenidos.
    print('Size:', berry['size'])
    print('Soil dryness:', berry['soil_dryness'])
    print('Firmness:', berry['firmness']['name'])

    # Verificamos que el tamaño (size) sea igual a 20.
    assert berry['size'] == 20

    # Verificamos que la sequedad del suelo
    # (soil_dryness) sea igual a 15.
    assert berry['soil_dryness'] == 15

    # Accedemos al objeto firmness y luego a su
    # propiedad name.
    # Verificamos que su valor sea 'soft'.
    assert berry['firmness']['name'] == 'soft'

    # Si todos los assert son verdaderos,
    # la prueba finaliza correctamente.
    print('CASO 1: Berry/1 validada correctamente')


# ==========================================================
# CASO 2: VALIDAR LOS DATOS DE BERRY/2
# ==========================================================

def test_berry_2():

    # Consultamos berry/1 para utilizar sus datos
    # como referencia en las comparaciones.
    berry_1 = obtener_json('berry/1')

    # Consultamos berry/2 y guardamos sus datos.
    berry_2 = obtener_json('berry/2')

    # Mostramos los valores de ambas berries.
    print('Size berry/1:', berry_1['size'])
    print('Size berry/2:', berry_2['size'])

    print('Soil dryness berry/1:', berry_1['soil_dryness'])
    print('Soil dryness berry/2:', berry_2['soil_dryness'])

    print('Firmness berry/2:', berry_2['firmness']['name'])

    # Verificamos que la firmeza de berry/2
    # sea igual a 'super-hard'.
    assert berry_2['firmness']['name'] == 'super-hard'

    # Verificamos que el tamaño de berry/2
    # sea mayor que el tamaño de berry/1.
    assert berry_2['size'] > berry_1['size']

    # Verificamos que la sequedad del suelo
    # de berry/2 sea igual a la de berry/1.
    assert berry_2['soil_dryness'] == berry_1['soil_dryness']

    # Mostramos el resultado de las validaciones.
    print('CASO 2: Berry/2 validada correctamente')


# ==========================================================
# CASO 3: VALIDAR LOS DATOS DEL POKÉMON PIKACHU
# ==========================================================

def test_pikachu():

    # Consultamos el endpoint del Pokémon Pikachu.
    # Guardamos los datos JSON en la variable pokemon.
    pokemon = obtener_json('pokemon/pikachu/')

    # Mostramos la experiencia base de Pikachu.
    print('Experiencia base:', pokemon['base_experience'])

    # Verificamos que la experiencia base
    # sea mayor que 10 y menor que 1000.
    #
    # Esta condición equivale a comprobar:
    # pokemon['base_experience'] > 10
    # y
    # pokemon['base_experience'] < 1000
    assert 10 < pokemon['base_experience'] < 1000

    # Creamos una lista con los nombres de los tipos
    # que aparecen en la respuesta JSON.
    #
    # pokemon['types'] contiene una lista de objetos.
    # Cada objeto tiene un campo 'type', que a su vez
    # contiene una propiedad 'name'.
    tipos = [
        tipo['type']['name']
        for tipo in pokemon['types']
    ]

    # Mostramos los tipos obtenidos.
    print('Tipos de Pikachu:', tipos)

    # Verificamos que 'electric' se encuentre
    # dentro de la lista de tipos.
    assert 'electric' in tipos

    # Mostramos el resultado final del caso.
    print('CASO 3: Pikachu validado correctamente')

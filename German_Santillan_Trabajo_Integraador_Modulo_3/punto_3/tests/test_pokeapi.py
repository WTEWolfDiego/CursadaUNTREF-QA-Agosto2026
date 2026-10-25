# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Automatización de los tres casos de prueba de PokeAPI.
# Alumno: Germán Santillán.

# Importamos pytest para etiquetar los tests y el cliente de PokeAPI.
import pytest
from api.pokeapi_client import PokeApiClient


# Caso 1: consultar berry/1 y verificar tamaño, sequedad y firmeza.
@pytest.mark.api
def test_caso_1_berry_1():

    # Realizamos un GET y verificamos que la API responda 200.
    respuesta = PokeApiClient().obtener("berry/1")
    assert respuesta.status_code == 200

    # Convertimos la respuesta de JSON a un diccionario de Python.
    datos = respuesta.json()

    # Validamos los tres valores solicitados por la consigna.
    assert datos["size"] == 20
    assert datos["soil_dryness"] == 15
    assert datos["firmness"]["name"] == "soft"


# Caso 2: consultar berry/2 y comparar los valores con berry/1.
@pytest.mark.api
def test_caso_2_berry_2():

    # Consultamos ambas berries en este mismo test para evitar depender
    # de la ejecución de otro caso de prueba.
    cliente = PokeApiClient()
    respuesta_1 = cliente.obtener("berry/1")
    respuesta_2 = cliente.obtener("berry/2")

    # Verificamos que ambas consultas respondan correctamente.
    assert respuesta_1.status_code == 200
    assert respuesta_2.status_code == 200

    # Obtenemos los diccionarios JSON de ambas respuestas.
    berry_1 = respuesta_1.json()
    berry_2 = respuesta_2.json()

    # Validamos la firmeza exacta de berry/2.
    assert berry_2["firmness"]["name"] == "super-hard"

    # Verificamos que berry/2 sea más grande que berry/1.
    assert berry_2["size"] > berry_1["size"]

    # Comprobamos que ambas berries tengan igual soil_dryness.
    assert berry_2["soil_dryness"] == berry_1["soil_dryness"]


# Caso 3: consultar Pikachu y validar su experiencia y tipo eléctrico.
@pytest.mark.api
def test_caso_3_pikachu():

    # Solicitamos el recurso pokemon/pikachu y verificamos el status HTTP.
    respuesta = PokeApiClient().obtener("pokemon/pikachu/")
    assert respuesta.status_code == 200

    # Convertimos la respuesta JSON y obtenemos la experiencia base.
    pokemon = respuesta.json()
    experiencia = pokemon["base_experience"]

    # Validamos que su experiencia sea mayor que 10 y menor que 1000.
    assert 10 < experiencia < 1000

    # Recuperamos los nombres de los tipos que tiene el Pokémon.
    tipos = [elemento["type"]["name"] for elemento in pokemon["types"]]

    # Verificamos que Pikachu tenga el tipo electric.
    assert "electric" in tipos

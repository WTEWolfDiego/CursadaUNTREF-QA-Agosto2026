# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis

import pytest
from api.pokeapi import PokeApi


# Case 1: Consultamos berry/1 y Verificam
def test_caso1():

    # Hacemos el GET correspondiente
    respuesta = PokeApi().consulta("berry/1")

    # Validamos los valores
    assert respuesta["size"] == 20
    assert respuesta["soil_dryness"] == 15
    assert respuesta["firmness"]["name"] == "soft"


# Caso 2: consultamos berry/2 y comparamos con berry/1
def test_caso2():

    berry_1 = PokeApi().consulta("berry/1")
    berry_2 = PokeApi().consulta("berry/2")

    # Validamos firmness berry/2 == super hard.
    assert berry_2["firmness"]["name"] == "super-hard"

    # Verificamos que berry/2 sea más grande.
    assert berry_2["size"] > berry_1["size"]

    # Verificamos mismo soil_dryness.
    assert berry_2["soil_dryness"] == berry_1["soil_dryness"]


# Caso 3: Pikachu.
def test_caso3():

    # Solicitamos el recurso pokemon/pikachu y verificamos el status HTTP.
    respuesta = PokeApi().consulta("pokemon/pikachu/")

    # Convertimos la respuesta JSON y obtenemos la experiencia base.
    exp = respuesta["base_experience"]

    # Validamos que su experiencia sea mayor que 10 y menor que 1000.
    assert 10 < exp < 1000, f"La experiencia base es {exp}"

    # Recuperamos los nombres de los tipos que tiene el Pokémon.
    tipos = [elemento["type"]["name"] for elemento in respuesta["types"]]

    # Verificamos que Pikachu tenga el tipo electric.
    assert "electric" in tipos
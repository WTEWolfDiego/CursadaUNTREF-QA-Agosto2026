# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis

import requests


class PokeApi:
    BASE_URL = "https://pokeapi.co/api/v2"

    def consulta(self, recurso):

        respuesta = requests.get(f"{self.BASE_URL}/{recurso}", timeout=20)
        assert respuesta.status_code == 200, f"{recurso} respuesta {respuesta.status_code}"
        return respuesta.json()
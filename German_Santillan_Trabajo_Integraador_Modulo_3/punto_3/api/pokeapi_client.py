# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Cliente reutilizable para consultas GET a PokeAPI.
# Alumno: Germán Santillán.

# Importamos requests para realizar solicitudes HTTP desde Python.
import requests


class PokeApiClient:
    BASE_URL = "https://pokeapi.co/api/v2"

    # Definimos un método que recibe el recurso a consultar y retorna la respuesta.
    def obtener(self, recurso):

        # Establecemos un tiempo máximo de espera para evitar requests infinitas.
        respuesta = requests.get(f"{self.BASE_URL}/{recurso}", timeout=20)

        # Retornamos la respuesta para validar el HTTP status y el JSON en el test.
        return respuesta

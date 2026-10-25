# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Configuración general de las pruebas automatizadas.
# Alumno: Germán Santillán.

# Importamos os para leer la variable HEADLESS y pytest para crear el fixture.
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Definimos un fixture para que cada caso UI tenga su propio navegador.
# Esto evita que los productos de un test queden agregados en el carrito de otro.
@pytest.fixture
def driver():

 
    # Configuramos las opciones de Chrome.
    opciones = Options()
    opciones.add_argument("--window-size=1440,900")
    
    #configuracion chrome por alerta de contraseña vulnerable
    opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
    # Si HEADLESS=1, ejecutamos Chrome sin mostrar la ventana.
    if os.getenv("HEADLESS", "0") == "1":
        opciones.add_argument("--headless=new")

    # Selenium Manager gestiona el driver compatible con Chrome.
    navegador = webdriver.Chrome(options=opciones)

    # Entregamos el navegador al caso de prueba.
    yield navegador

    # Cerramos el navegador incluso si el caso falla.
    navegador.quit()

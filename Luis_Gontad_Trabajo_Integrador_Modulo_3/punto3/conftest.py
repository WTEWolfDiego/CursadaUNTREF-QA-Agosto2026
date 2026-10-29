# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--navegador", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):
    navegador = request.config.getoption("--navegador")
    headless = request.config.getoption("--headless")
 
    # Configuración Chrome.
    opciones = Options()
    opciones.add_argument("--window-size=1440,900")
    
    # Configuracion chrome alertas.
    opciones.add_experimental_option("prefs", 
                {"credentials_enable_service": False,
                "profile.password_manager_enabled": False, 
                "profile.password_manager_leak_detection": False})
    
    if headless:
        opciones.add_argument("--headless=new")

    navegador = webdriver.Chrome(options=opciones)

    yield navegador

    navegador.quit()

  

def pytest_html_report_title(report):
    report.title = "Reporte de ejecución Testing Automatizado - Trabajo Integrador Modulo 3"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata["Alumno"] = "Gontad Luis"
    metadata["Proyecto"] = "Trabajo Integrador Módulo 3"
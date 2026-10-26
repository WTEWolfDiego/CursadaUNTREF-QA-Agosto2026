import pytest
from selenium import webdriver

from paginas.login import Login


def pytest_addoption(parser):
    parser.addoption("--navegador", default="chrome", choices=["chrome", "firefox", "edge"])
    parser.addoption("--sin-ventana", action="store_true")


@pytest.fixture
def driver(request):
    nombre = request.config.getoption("--navegador")
    oculto = request.config.getoption("--sin-ventana")

    if nombre == "firefox":
        opciones = webdriver.FirefoxOptions()
        if oculto:
            opciones.add_argument("-headless")
        navegador = webdriver.Firefox(options=opciones)
    elif nombre == "edge":
        opciones = webdriver.EdgeOptions()
        if oculto:
            opciones.add_argument("--headless=new")
        navegador = webdriver.Edge(options=opciones)
    else:
        opciones = webdriver.ChromeOptions()
        opciones.add_argument("--window-size=1366,900")
        opciones.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        if oculto:
            opciones.add_argument("--headless=new")
        navegador = webdriver.Chrome(options=opciones)

    yield navegador
    navegador.quit()


@pytest.fixture
def sesion_iniciada(driver):
    Login(driver).ingresar("standard_user", "secret_sauce")
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when == "call" and reporte.failed and "driver" in item.fixturenames:
        from pytest_html import extras
        captura = item.funcargs["driver"].get_screenshot_as_base64()
        reporte.extras = getattr(reporte, "extras", []) + [extras.image(captura, "Pantalla al fallar")]


def pytest_html_report_title(report):
    report.title = "TP Integrador QA Automation - Resultados"

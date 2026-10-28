import time

import pytest
from selenium import webdriver

URL_SAUCEDEMO = "https://www.saucedemo.com/"
URL_POKEAPI = "https://pokeapi.co/api/v2"


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Ejecutar Chrome sin interfaz")


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(URL_SAUCEDEMO)

    yield driver

    time.sleep(2)
    driver.quit()


@pytest.fixture
def base_url_api():
    return URL_POKEAPI

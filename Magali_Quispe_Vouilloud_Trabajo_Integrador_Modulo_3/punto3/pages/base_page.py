import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAUSA = 1


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esperar(self):
        time.sleep(PAUSA)

    def buscar(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def buscar_todos(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.esperar()

    def escribir(self, locator, texto):
        campo = self.buscar(locator)
        campo.clear()
        campo.send_keys(texto)
        self.esperar()

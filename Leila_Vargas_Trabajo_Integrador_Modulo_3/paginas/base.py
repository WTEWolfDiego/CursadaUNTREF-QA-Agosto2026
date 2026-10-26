from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PaginaBase:
    TITULO = (By.CSS_SELECTOR, "span.title")
    CONTADOR_CARRITO = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    ICONO_CARRITO = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def __init__(self, driver, espera=10):
        self.driver = driver
        self.espera = WebDriverWait(driver, espera)

    def elemento(self, localizador):
        return self.espera.until(EC.visibility_of_element_located(localizador))

    def clic(self, localizador):
        self.espera.until(EC.element_to_be_clickable(localizador)).click()

    def escribir(self, localizador, texto):
        campo = self.elemento(localizador)
        campo.clear()
        campo.send_keys(texto)

    def textos(self, localizador):
        return [e.text for e in self.driver.find_elements(*localizador)]

    def titulo_es(self, texto):
        return self.espera.until(EC.text_to_be_present_in_element(self.TITULO, texto))

    def cantidad_en_carrito(self):
        contador = self.driver.find_elements(*self.CONTADOR_CARRITO)
        return int(contador[0].text) if contador else 0

    def carrito_tiene(self, cantidad):
        try:
            self.espera.until(lambda d: self.cantidad_en_carrito() == cantidad)
            return True
        except TimeoutException:
            return False

    def abrir_carrito(self):
        self.clic(self.ICONO_CARRITO)

    @staticmethod
    def id_producto(nombre):
        return nombre.lower().replace(" ", "-")

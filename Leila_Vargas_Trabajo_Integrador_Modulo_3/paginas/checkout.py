from selenium.webdriver.common.by import By

from paginas.base import PaginaBase


class Checkout(PaginaBase):
    NOMBRE = (By.CSS_SELECTOR, "[data-test='firstName']")
    APELLIDO = (By.CSS_SELECTOR, "[data-test='lastName']")
    CODIGO_POSTAL = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUAR = (By.CSS_SELECTOR, "[data-test='continue']")
    FINALIZAR = (By.CSS_SELECTOR, "[data-test='finish']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    AGRADECIMIENTO = (By.CSS_SELECTOR, "h2.complete-header")

    def completar(self, nombre=None, apellido=None, codigo_postal=None):
        if nombre is not None:
            self.escribir(self.NOMBRE, nombre)
        if apellido is not None:
            self.escribir(self.APELLIDO, apellido)
        if codigo_postal is not None:
            self.escribir(self.CODIGO_POSTAL, codigo_postal)

    def continuar(self):
        self.clic(self.CONTINUAR)

    def finalizar(self):
        self.clic(self.FINALIZAR)

    def mensaje_error(self):
        return self.elemento(self.ERROR).text

    def mensaje_final(self):
        return self.elemento(self.AGRADECIMIENTO).text

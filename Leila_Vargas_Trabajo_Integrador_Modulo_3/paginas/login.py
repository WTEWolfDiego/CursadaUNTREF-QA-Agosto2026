from selenium.webdriver.common.by import By

from paginas.base import PaginaBase


class Login(PaginaBase):
    URL = "https://www.saucedemo.com/"
    USUARIO = (By.CSS_SELECTOR, "[data-test='username']")
    CLAVE = (By.CSS_SELECTOR, "[data-test='password']")
    BOTON_INGRESAR = (By.CSS_SELECTOR, "[data-test='login-button']")

    def ingresar(self, usuario, clave):
        self.driver.get(self.URL)
        self.escribir(self.USUARIO, usuario)
        self.escribir(self.CLAVE, clave)
        self.clic(self.BOTON_INGRESAR)

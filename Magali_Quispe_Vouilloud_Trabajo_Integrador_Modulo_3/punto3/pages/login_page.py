from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    INPUT_USUARIO = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")

    def login(self, usuario="standard_user", password="secret_sauce"):
        self.escribir(self.INPUT_USUARIO, usuario)
        self.escribir(self.INPUT_PASSWORD, password)
        self.click(self.BOTON_LOGIN)

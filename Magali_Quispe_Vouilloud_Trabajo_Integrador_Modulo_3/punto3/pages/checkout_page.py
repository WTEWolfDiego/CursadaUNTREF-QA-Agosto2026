from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    INPUT_NOMBRE = (By.ID, "first-name")
    INPUT_APELLIDO = (By.ID, "last-name")
    INPUT_CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUAR = (By.ID, "continue")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    BOTON_FINALIZAR = (By.ID, "finish")
    MENSAJE_COMPRA_OK = (By.CLASS_NAME, "complete-header")

    def ingresar_nombre(self, nombre):
        self.escribir(self.INPUT_NOMBRE, nombre)

    def ingresar_apellido(self, apellido):
        self.escribir(self.INPUT_APELLIDO, apellido)

    def ingresar_codigo_postal(self, codigo):
        self.escribir(self.INPUT_CODIGO_POSTAL, codigo)

    def continuar(self):
        self.click(self.BOTON_CONTINUAR)

    def obtener_error(self):
        return self.buscar(self.MENSAJE_ERROR).text

    def completar_datos(self, nombre, apellido, codigo):
        self.ingresar_nombre(nombre)
        self.ingresar_apellido(apellido)
        self.ingresar_codigo_postal(codigo)
        self.continuar()

    def finalizar(self):
        self.click(self.BOTON_FINALIZAR)

    def obtener_mensaje_final(self):
        return self.buscar(self.MENSAJE_COMPRA_OK).text

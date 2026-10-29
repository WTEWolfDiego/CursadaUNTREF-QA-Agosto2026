# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CheckoutPage:
    #Localizadores
    LOC_NOMBRE = (By.ID, "first-name")
    LOC_APELLIDO = (By.ID, "last-name")
    LOC_CP = (By.ID, "postal-code")
    LOC_BTN_CONTINUE = (By.ID, "continue")
    LOC_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    LOC_BTN_FINISH = (By.ID, "finish")
    LOC_CONFIRMACION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ingresar_nombre(self, nombre):
        self.wait.until(EC.visibility_of_element_located(self.LOC_NOMBRE)).send_keys(nombre)

    def ingresar_apellido(self, apellido):
        self.driver.find_element(*self.LOC_APELLIDO).send_keys(apellido)

    def ingresar_cp(self, cp):
        self.driver.find_element(*self.LOC_CP).send_keys(cp)

    def continuar(self):
        self.driver.find_element(*self.LOC_BTN_CONTINUE).click()

    def validar_campos(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOC_ERROR)).text

    def completar_campos(self, nombre, apellido, cp):
        self.ingresar_nombre(nombre)
        self.ingresar_apellido(apellido)
        self.ingresar_cp(cp)

    def finalizar_compra(self):
        self.wait.until(EC.element_to_be_clickable(self.LOC_BTN_FINISH)).click()

    def obtener_confirmacion(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOC_CONFIRMACION)).text
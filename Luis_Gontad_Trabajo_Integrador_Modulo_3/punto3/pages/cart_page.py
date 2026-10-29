# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    #Localizadores
    LOC_ITEMS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    LOC_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    LOC_BTN_CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    LOC_BTN_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def get_nombres_producto(self):
        return [e.text for e in self.driver.find_elements(*self.LOC_ITEMS)]

    def get_cantidad_badge(self):
        badges = self.driver.find_elements(*self.LOC_BADGE)
        return int(badges[0].text) if badges else 0

    def remove_item(self, nombre):
        id_boton = "remove-" + nombre.lower().replace(" ", "-")
        # Hacemos clic en el botón de remover
        self.wait.until(EC.element_to_be_clickable((By.ID, id_boton))).click()
        

    def click_seguir_comprando(self):
        self.driver.find_element(*self.LOC_BTN_CONTINUE_SHOPPING).click()

    def go_to_checkout(self):
        self.driver.find_element(*self.LOC_BTN_CHECKOUT).click()
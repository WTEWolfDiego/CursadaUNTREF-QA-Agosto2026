# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    #Localizadores
    LOC_SORT_ORDEN = (By.CLASS_NAME, "product_sort_container")
    LOC_PRECIOS = (By.CLASS_NAME, "inventory_item_price")
    LOC_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    LOC_BTN_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    LOC_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    LOC_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def ordenar_por(self, opcion):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.LOC_SORT_ORDEN)))
        select.select_by_visible_text(opcion)

    def get_orden(self):
        select = Select(self.driver.find_element(*self.LOC_SORT_ORDEN))
        return select.first_selected_option.text

    def get_precios(self):
        precios = self.driver.find_elements(*self.LOC_PRECIOS)
        return [float(precio.text.replace("$", "")) for precio in precios]

    def get_items(self):
        return [item.text for item in self.driver.find_elements(*self.LOC_ITEMS)]

    def add_todos(self):
        boton = self.driver.find_elements(*self.LOC_BTN_AGREGAR)
        while boton:
            boton[0].click()
            boton = self.driver.find_elements(*self.LOC_BTN_AGREGAR)

    def add_item(self, item):
        id_boton = "add-to-cart-" + item.lower().replace(" ", "-")
        self.wait.until(EC.element_to_be_clickable((By.ID, id_boton))).click()
        return [item]

    def get_cantidad_carrito(self):
        try:
            # Espera hasta 5 segundos a que la insignia del carrito sea visible
            badge = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.LOC_BADGE)
        )
            return int(badge.text)
        except:
        # Si no aparece la insignia (carrito vacío), retorna 0
            return 0

    def go_to_carrito(self):
        self.driver.find_element(*self.LOC_LINK).click()
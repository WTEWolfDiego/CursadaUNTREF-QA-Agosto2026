from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITULO = (By.CLASS_NAME, "title")
    SELECT_ORDEN = (By.CLASS_NAME, "product_sort_container")
    PRECIOS = (By.CLASS_NAME, "inventory_item_price")
    NOMBRES = (By.CLASS_NAME, "inventory_item_name")
    BOTONES_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")

    def esta_cargada(self):
        return self.buscar(self.TITULO).text == "Products"

    def ordenar_por(self, texto_opcion):
        Select(self.buscar(self.SELECT_ORDEN)).select_by_visible_text(texto_opcion)
        self.esperar()

    def obtener_precios(self):
        precios = self.buscar_todos(self.PRECIOS)
        return [float(precio.text.replace("$", "")) for precio in precios]

    def obtener_nombres(self):
        return [nombre.text for nombre in self.buscar_todos(self.NOMBRES)]

    def agregar_todos(self):
        botones = self.buscar_todos(self.BOTONES_AGREGAR)
        for boton in botones:
            boton.click()
            self.esperar()
        return len(botones)

    def agregar_productos(self, cantidad):
        nombres = self.obtener_nombres()[:cantidad]
        for _ in range(cantidad):
            self.buscar_todos(self.BOTONES_AGREGAR)[0].click()
            self.esperar()
        return nombres

    def cantidad_en_badge(self):
        return int(self.buscar(self.BADGE_CARRITO).text)

    def ir_al_carrito(self):
        self.click(self.LINK_CARRITO)

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITULO = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "cart_item")
    NOMBRES = (By.CLASS_NAME, "inventory_item_name")
    BOTONES_REMOVER = (By.CSS_SELECTOR, "button[id^='remove']")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    BOTON_CONTINUAR_COMPRANDO = (By.ID, "continue-shopping")
    BOTON_CHECKOUT = (By.ID, "checkout")

    def esta_cargada(self):
        return self.buscar(self.TITULO).text == "Your Cart"

    def obtener_nombres(self):
        return [nombre.text for nombre in self.driver.find_elements(*self.NOMBRES)]

    def cantidad_items(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def remover_primero(self):
        self.click(self.BOTONES_REMOVER)

    def tiene_badge(self):
        return len(self.driver.find_elements(*self.BADGE_CARRITO)) > 0

    def continuar_comprando(self):
        self.click(self.BOTON_CONTINUAR_COMPRANDO)

    def ir_al_checkout(self):
        self.click(self.BOTON_CHECKOUT)

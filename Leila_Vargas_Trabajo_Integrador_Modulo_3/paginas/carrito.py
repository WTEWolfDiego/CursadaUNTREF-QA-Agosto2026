from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from paginas.base import PaginaBase


class Carrito(PaginaBase):
    PRODUCTOS = (By.CSS_SELECTOR, "div.cart_item div.inventory_item_name")
    SEGUIR_COMPRANDO = (By.CSS_SELECTOR, "[data-test='continue-shopping']")
    CHECKOUT = (By.CSS_SELECTOR, "[data-test='checkout']")

    def productos(self):
        return self.textos(self.PRODUCTOS)

    def quitar(self, nombre):
        boton = (By.CSS_SELECTOR, f"[data-test='remove-{self.id_producto(nombre)}']")
        self.clic(boton)
        self.espera.until(EC.invisibility_of_element_located(boton))

    def seguir_comprando(self):
        self.clic(self.SEGUIR_COMPRANDO)

    def ir_a_checkout(self):
        self.clic(self.CHECKOUT)

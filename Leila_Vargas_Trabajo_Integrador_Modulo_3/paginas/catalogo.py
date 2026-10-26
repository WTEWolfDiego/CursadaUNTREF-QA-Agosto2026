from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from paginas.base import PaginaBase


class Catalogo(PaginaBase):
    ORDENAR = (By.CSS_SELECTOR, "select.product_sort_container")
    NOMBRES = (By.CSS_SELECTOR, "div.inventory_item_name")
    PRECIOS = (By.CSS_SELECTOR, "div.inventory_item_price")
    AGREGAR = (By.XPATH, "//button[text()='Add to cart']")

    def ordenar(self, criterio):
        Select(self.elemento(self.ORDENAR)).select_by_visible_text(criterio)

    def criterio_actual(self):
        return Select(self.elemento(self.ORDENAR)).first_selected_option.text

    def lista_precios(self):
        return [float(p.lstrip("$")) for p in self.textos(self.PRECIOS)]

    def lista_productos(self):
        return self.textos(self.NOMBRES)

    def agregar(self, nombre):
        self.clic((By.CSS_SELECTOR, f"[data-test='add-to-cart-{self.id_producto(nombre)}']"))

    def agregar_todo(self):
        while self.driver.find_elements(*self.AGREGAR):
            self.driver.find_elements(*self.AGREGAR)[0].click()

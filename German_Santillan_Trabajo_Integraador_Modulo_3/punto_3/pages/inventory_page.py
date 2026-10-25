# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Acciones reutilizables para el catálogo de productos de SauceDemo.
# Alumno: Germán Santillán.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page import BasePage


class InventoryPage(BasePage):

    # Comprobamos que el inventario ya esté visible antes de utilizarlo.
    def esperar_inventario(self):
        self.esperar_pagina(
            "inventory.html", (By.CSS_SELECTOR, ".inventory_list .inventory_item")
        )

    # Ordenamos los productos por precio de menor a mayor.
    def ordenar_por_precio_ascendente(self):
        self.esperar_inventario()

        # Esperamos a que el selector de ordenamiento esté habilitado.
        selector = self.espera.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="product-sort-container"]'))
        )
        Select(selector).select_by_value("lohi")

        # Verificamos que el selector haya aplicado la opción elegida.
        self.espera.until(
            lambda navegador: Select(
                navegador.find_element(By.CLASS_NAME, "product_sort_container")
            ).first_selected_option.get_attribute("value") == "lohi"
        )

        # Esperamos a que los precios vuelvan a estar visibles tras el cambio.
        self.espera.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
            )
        )

    # Obtenemos los precios tal como aparecen en pantalla.
    def obtener_precios(self):
        self.esperar_inventario()
        elementos = self.espera.until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_price")
            )
        )

        # Convertimos cada precio de texto ('$29.99') a float (29.99).
        return [float(elemento.text.replace("$", "")) for elemento in elementos]

    # Obtenemos los nombres de los productos que ya están visibles.
    def obtener_nombres_productos(self):
        self.esperar_inventario()
        elementos = self.espera.until(
            EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
        return [elemento.text for elemento in elementos]

    # Agregamos al carrito la cantidad indicada de productos disponibles.
    def agregar_primeros_productos(self, cantidad):
        nombres = self.obtener_nombres_productos()
        assert len(nombres) >= cantidad, "No hay suficientes productos en el catálogo."

        # Buscamos el siguiente botón disponible antes de cada clic.
        for _ in range(cantidad):

            # Identificamos el botón en una espera: si el inventario se
            # actualiza y el elemento queda obsoleto, lo buscamos otra vez.
            def obtener_id_siguiente(navegador):
                try:
                    boton = EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, 'button[id^="add-to-cart-"]')
                    )(navegador)
                    if not boton:
                        return False
                    return boton.get_attribute("id")
                except StaleElementReferenceException:
                    return False

            identificador = self.espera.until(obtener_id_siguiente)

            # Hacemos clic usando el ID del producto elegido.
            # hacer_click vuelve a ubicar el botón si cambia el DOM.
            self.hacer_click((By.ID, identificador))

            # Esperamos que Add to cart cambie a Remove antes de continuar.
            identificador_remove = identificador.replace("add-to-cart-", "remove-", 1)
            self.espera.until(
                EC.element_to_be_clickable((By.ID, identificador_remove))
            )

        return nombres[:cantidad]

    # Agregamos todos los productos visibles en el catálogo.
    def agregar_todos_los_productos(self):
        cantidad = len(self.obtener_nombres_productos())
        return self.agregar_primeros_productos(cantidad)

    # Abrimos el carrito y esperamos que su contenido esté disponible.
    def abrir_carrito(self):
        self.hacer_click((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'))
        self.esperar_pagina("cart.html", (By.CLASS_NAME, "cart_list"))

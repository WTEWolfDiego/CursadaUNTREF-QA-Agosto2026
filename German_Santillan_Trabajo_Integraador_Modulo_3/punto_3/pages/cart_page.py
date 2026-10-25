# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Acciones reutilizables para el carrito de SauceDemo.
# Alumno: Germán Santillán.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from pages.base_page import BasePage


class CartPage(BasePage):

    # Obtenemos los nombres del carrito, incluso cuando está vacío.
    def obtener_nombres_productos(self, cantidad_esperada=None):
        self.esperar_pagina("cart.html", (By.CLASS_NAME, "cart_list"))
        localizador = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")

        # Si conocemos la cantidad esperada, aguardamos a que el carrito
        # se actualice antes de leer sus elementos (incluido el caso vacío).
        if cantidad_esperada is not None:
            self.espera.until(
                lambda navegador: len(navegador.find_elements(*localizador))
                == cantidad_esperada
            )

        # Cuando esperamos productos, comprobamos también que estén visibles.
        if cantidad_esperada is not None and cantidad_esperada > 0:
            self.espera.until(EC.visibility_of_all_elements_located(localizador))

        elementos = self.driver.find_elements(*localizador)
        return [elemento.text for elemento in elementos]

    # Quitamos el primer producto del carrito y esperamos su eliminación real.
    def quitar_primer_producto(self):
        self.esperar_pagina("cart.html", (By.CLASS_NAME, "cart_list"))
        localizador = (By.CSS_SELECTOR, '.cart_item button[id^="remove-"]')

        # Verificamos que haya un producto y guardamos la cantidad inicial.
        cantidad_inicial = self.espera.until(
            lambda navegador: len(navegador.find_elements(By.CLASS_NAME, "cart_item")) or False
        )

        # Identificamos el botón por su ID para no terminar quitando
        # otro producto distinto si la página se vuelve a renderizar.
        def obtener_id_boton(navegador):
            try:
                boton = EC.element_to_be_clickable(localizador)(navegador)
                if not boton:
                    return False
                return boton.get_attribute("id")
            except StaleElementReferenceException:
                return False

        identificador = self.espera.until(obtener_id_boton)
        localizador_boton = (By.ID, identificador)

        # Si el botón quedó obsoleto, lo buscamos nuevamente usando
        # el MISMO ID. Nunca repetimos el clic sobre otro producto.
        def intentar_quitar(navegador):
            try:
                boton = EC.element_to_be_clickable(localizador_boton)(navegador)
                if not boton:
                    return False
                boton.click()
                return True
            except (StaleElementReferenceException, NoSuchElementException):
                # Puede haber quedado obsoleto porque el clic ya eliminó
                # el producto. Si desapareció, NO repetimos la acción.
                return not navegador.find_elements(*localizador_boton)

        self.espera.until(
            intentar_quitar,
            message=f"No fue posible quitar el producto: {identificador}",
        )

        # Comprobamos el resultado, no solamente que se intentó el clic.
        self.espera.until(EC.invisibility_of_element_located(localizador_boton))
        self.espera.until(
            lambda navegador: len(navegador.find_elements(By.CLASS_NAME, "cart_item"))
            == cantidad_inicial - 1
        )

    # Volvemos al catálogo y esperamos que aparezcan los productos.
    def continuar_comprando(self):
        self.hacer_click((By.ID, "continue-shopping"))
        self.esperar_pagina(
            "inventory.html", (By.CSS_SELECTOR, ".inventory_list .inventory_item")
        )

    # Iniciamos el checkout y esperamos el formulario de datos personales.
    def iniciar_checkout(self):
        self.hacer_click((By.ID, "checkout"))
        self.esperar_pagina("checkout-step-one.html", (By.ID, "first-name"))

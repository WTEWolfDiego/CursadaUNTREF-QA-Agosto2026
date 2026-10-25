# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Acciones reutilizables para el checkout de SauceDemo.
# Alumno: Germán Santillán.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # Ingresamos el nombre cuando el formulario esté cargado.
    def ingresar_nombre(self, nombre):
        self.esperar_pagina("checkout-step-one.html", (By.ID, "first-name"))
        self.escribir_en_campo((By.ID, "first-name"), nombre)

    # Esperamos el campo del apellido antes de escribir.
    def ingresar_apellido(self, apellido):
        self.escribir_en_campo((By.ID, "last-name"), apellido)

    # Esperamos el campo del código postal antes de escribir.
    def ingresar_codigo_postal(self, codigo_postal):
        self.escribir_en_campo((By.ID, "postal-code"), codigo_postal)

    # Esperamos que Continue esté habilitado antes de hacer clic.
    def continuar(self):
        self.hacer_click((By.ID, "continue"))

    # Esperamos el texto específico que solicita la consigna.
    # Así no leemos por error el mensaje anterior cuando cambia la validación.
    def obtener_mensaje_error(self):
        localizador = (By.CSS_SELECTOR, 'h3[data-test="error"]')
        return self.espera.until(EC.visibility_of_element_located(localizador)).text

    # Finalizamos el pedido desde la pantalla de resumen del checkout.
    def finalizar_compra(self):
        self.esperar_pagina("checkout-step-two.html", (By.ID, "finish"))
        self.hacer_click((By.ID, "finish"))

        # Esperamos la pantalla de compra finalizada y el mensaje de éxito.
        mensaje = self.esperar_pagina(
            "checkout-complete.html", (By.CLASS_NAME, "complete-header")
        )
        return mensaje.text

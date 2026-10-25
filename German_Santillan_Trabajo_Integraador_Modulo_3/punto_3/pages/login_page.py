# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Clase que representa el inicio de sesión de SauceDemo.
# Alumno: Germán Santillán.

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# Reutilizamos los métodos de espera definidos en BasePage.
class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Abrimos la plataforma e ingresamos las credenciales del usuario estándar.
    def iniciar_sesion(self):
        self.driver.get(self.URL)

        # Esperamos que el HTML esté cargado y que el formulario sea visible.
        self.esperar_pagina("saucedemo.com", (By.ID, "user-name"))

        # Escribimos únicamente cuando los campos están listos para interactuar.
        self.escribir_en_campo((By.ID, "user-name"), "standard_user")
        self.escribir_en_campo((By.ID, "password"), "secret_sauce")

        # Esperamos que el botón de login esté habilitado antes de presionarlo.
        self.hacer_click((By.ID, "login-button"))

        # Comprobamos que se abrió el inventario y aparecen sus productos.
        self.esperar_pagina(
            "inventory.html", (By.CSS_SELECTOR, ".inventory_list .inventory_item")
        )

# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Métodos reutilizables para esperar la carga de páginas y sus elementos.
# Alumno: Germán Santillán.

# Importamos las esperas explícitas y condiciones de Selenium.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


# Definimos una clase base para evitar repetir esperas en cada página.
class BasePage:

    def __init__(self, driver):
        self.driver = driver

        # Esperamos hasta 20 segundos por cada condición, sin usar time.sleep().
        self.espera = WebDriverWait(driver, 20)

    # Comprobamos que el navegador haya terminado de cargar el documento HTML.
    def esperar_documento_cargado(self):
        self.espera.until(
            lambda navegador: navegador.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    # Esperamos la URL correcta, la carga del HTML y un elemento visible.
    # El elemento visible confirma que la pantalla ya puede utilizarse.
    def esperar_pagina(self, ruta, localizador_visible):
        self.espera.until(EC.url_contains(ruta))
        self.esperar_documento_cargado()
        return self.espera.until(
            EC.visibility_of_element_located(localizador_visible)
        )

    # Esperamos que el elemento esté visible y habilitado antes del clic.
    # Buscamos el elemento nuevamente en cada intento. Si la página actualiza
    # el DOM y el elemento deja de existir, Selenium vuelve a intentarlo.
    # El clic ocurre dentro de la condición de espera para reducir el tiempo
    # entre la búsqueda del elemento y la interacción.
    def hacer_click(self, localizador):
        self.esperar_documento_cargado()

        def intentar_click(navegador):
            try:
                elemento = EC.element_to_be_clickable(localizador)(navegador)
                if not elemento:
                    return False
                elemento.click()
                return True
            except StaleElementReferenceException:
                # Un elemento obsoleto no se reutiliza: esperamos y lo buscamos otra vez.
                return False

        self.espera.until(
            intentar_click,
            message=f"No fue posible hacer clic en el elemento: {localizador}",
        )

    # Esperamos un campo visible y habilitado antes de ingresar información.
    def escribir_en_campo(self, localizador, valor):
        self.esperar_documento_cargado()
        campo = self.espera.until(EC.element_to_be_clickable(localizador))
        campo.clear()
        campo.send_keys(valor)

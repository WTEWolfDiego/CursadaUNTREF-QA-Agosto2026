from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pytest

opciones = webdriver.ChromeOptions()

opciones.add_argument("--disable-features=TranslateUI,PasswordLeakDetection,PasswordManager")

#para el popup
opciones.add_experimental_option(
    "prefs",
    {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=opciones)

driver.get("https://www.saucedemo.com/")

#logueo
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
print("Login exitoso")

time.sleep(2)

# Agregar un artículo al carrito
driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

print("Se cargó el artículo al carrito")

# Ir al carrito y eliminar el artículo
driver.find_element(By.ID, "shopping_cart_container").click()
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

# Verificar que el carrito esté vacío
assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0, \
        "El carrito no está vacío"

print("El carrito está vacío")

# Continuar comprando
driver.find_element(By.ID, "continue-shopping").click()

# Agregar dos artículos
driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()

driver.find_element(
        By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
    ).click()

# Ir al carrito
driver.find_element(By.ID, "shopping_cart_container").click()

# Validar los artículos
validacion1 = driver.find_element(
        By.ID, "item_1_title_link"
    ).text

assert "Sauce Labs Bolt T-Shirt" in validacion1

validacion2 = driver.find_element(
        By.ID, "item_3_title_link"
    ).text

assert "Test.allTheThings() T-Shirt (Red)" in validacion2

assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 2

print("Validamos que hay 2 artículos en el carrito")
time.sleep(2)

# Iniciar checkout
driver.find_element(By.ID, "checkout").click()

# Completar los datos
driver.find_element(By.ID, "first-name").send_keys("Johanna")
driver.find_element(By.ID, "last-name").send_keys("Mendez")
driver.find_element(By.ID, "postal-code").send_keys("1406")
time.sleep(1)
driver.find_element(By.ID, "continue").click()

# Finalizar la compra
driver.find_element(By.ID, "finish").click()

# Validar la compra
exito = driver.find_element(
        By.XPATH, "//*[@id='checkout_complete_container']/h2"
    ).text

assert "Thank you for your order!" in exito
time.sleep(5)

print("Compra finalizada y validada")
   
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import time


def test_mensajes_error(driver):
    time.sleep(1)
    driver.maximize_window()

    driver.get('https://www.saucedemo.com/')
    time.sleep(1)

    #Ingreso datos de usuario y contraseña.
    driver.find_element(By.ID, 'user-name').send_keys ("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys ('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    #Agrego todos los productos disponibles
    agregar_prod = driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
    print("Botones encontrados:", len(agregar_prod))
    for boton in agregar_prod:
        boton.click()
    time.sleep(2)


    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(5)

    #Verifico cantidad de productos ingresados.
    prod_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    time.sleep(4)
    cantidad_productos = len(prod_en_carrito)
    print("Cantidad de productos en el carrito: " + str(cantidad_productos))
    assert cantidad_productos == 6, ("Se esperaban 6 productos, pero se encontraron: " + str(cantidad_productos))

    driver.find_element(By.ID, 'checkout').click()
    time.sleep(1)

    driver.find_element(By.ID,'first-name').send_keys('Juan Ignacio')
    time.sleep(1)

    driver.find_element(By.ID,'continue').click()

    #Verifico mensaje de error al ingresar solo el nombre
    error_checkout_first = driver.find_element(By.XPATH,"//h3[@data-test='error']").text
    assert error_checkout_first == "Error: Last Name is required", "El mensaje de error es diferente al esperado."
    time.sleep(1)

    driver.find_element(By.ID,'last-name').send_keys('Poropat')
    time.sleep(1)

    driver.find_element(By.ID,'continue').click()

    error_checkout_last = driver.find_element(By.XPATH,"//h3[@data-test='error']").text
    assert error_checkout_last == "Error: Postal Code is required", "El mensaje de error es diferente al esperado."
    time.sleep(3)

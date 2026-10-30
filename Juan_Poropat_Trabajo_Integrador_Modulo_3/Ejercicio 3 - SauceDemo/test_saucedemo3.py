from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_realizar_compra(driver):

    driver.get('https://www.saucedemo.com/')
    time.sleep(1)

    # Ingreso datos de usuario y contraseña.
    driver.find_element(By.ID, 'user-name').send_keys ("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys ('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)

    driver.find_element(By.ID, 'remove-sauce-labs-bike-light').click()
    
    # Verifico si el carrito queda vacío
    carrito_vacio = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(carrito_vacio) == 0, "El carrito NO esta vacío."
    print("Carrito vacio")

    time.sleep(1)

    driver.find_element(By.ID, 'continue-shopping').click()

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(1)

    driver.find_element(By.ID,'add-to-cart-sauce-labs-fleece-jacket').click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)
    
    # Verifico la cantidad de productos en el carrito
    prod_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(prod_carrito) == 2, ("Se esperan 2 productos, se encontraron: " + str(prod_carrito))
    print("Se encontraron 2 productos en el carrito")

    driver.find_element(By.ID,'checkout').click()
    time.sleep(1)

    driver.find_element(By.ID,'first-name').send_keys('Juan Ignacio')
    driver.find_element(By.ID,'last-name').send_keys('Poropat')
    driver.find_element(By.ID,'postal-code').send_keys(1212)
    time.sleep(1)

    driver.find_element(By.ID,'continue').click()
    time.sleep(1)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    mensaje = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
).text
    assert mensaje == "Thank you for your order!"
print("Compra realizada con éxito")
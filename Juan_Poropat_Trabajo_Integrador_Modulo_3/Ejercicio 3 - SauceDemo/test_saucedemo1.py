from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import time

def test_menor_a_mayor(driver):
    time.sleep(1)
    driver.maximize_window()

    driver.get('https://www.saucedemo.com/')
    time.sleep(2)

    # Ingreso credenciales de usuario y contraseña
    driver.find_element(By.ID, 'user-name').send_keys ("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, 'password').send_keys ('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(2)
    # Ordeno los elementos de menor a mayor
    select = Select (driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value ('lohi')
    
    # Verifico orden de precios
    precio_menor = driver.find_element(By.CLASS_NAME, "active_option")
    assert precio_menor.text == "Price (low to high)"
    time.sleep(5) 
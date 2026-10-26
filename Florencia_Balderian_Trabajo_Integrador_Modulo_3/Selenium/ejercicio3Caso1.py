from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# Caso 1
#  El usuario se loguea al sitio como usuario standard user
#  Ordenar los elementos por “price (low to high)”
#  Verificar que los elementos estén ordenados

def test_verificar_orden_por_precio():
    opciones = webdriver.ChromeOptions()
    opciones.add_experimental_option("prefs", {"credentials_enable_service": False,
    "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
    driver = webdriver.Chrome(options=opciones)
    driver.get("https://www.saucedemo.com/")

    driver.maximize_window()
    time.sleep(2)
    
# Login como usuario standard user

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    time.sleep(2)

    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    time.sleep(2)

    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    orden = Select(driver.find_element(
        By.CLASS_NAME, 'product_sort_container'))
    orden.select_by_value('lohi')

    time.sleep(2)

    elementos = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

    precios = []
    for elemento in elementos:
        precios.append(float(elemento.text.replace('$', '')))

    # Verifico que los productos estén ordenados con precios de menor a mayor
    
    assert precios, "No se encontraron precios de productos"
    assert precios == sorted(precios), (
        f"Los precios no están ordenados de menor a mayor: {precios}"
    )
    print("Test OK - Los precios están ordenados de menor a mayor.")

    time.sleep(3)
    driver.quit()

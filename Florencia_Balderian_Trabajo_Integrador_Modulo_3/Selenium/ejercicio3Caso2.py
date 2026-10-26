from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Caso 2
# El usuario se loguea al sitio como usuario standard user
# Incorporar al carrito todos los productos
# Ir al carrito
# Verificar que todos los productos estén en el carrito
# Ir al checkout
# Ingresar nombre y clickear “Continue”
# Verificar que aparece el error “Error: Last Name is required”
# Ingresar un apellido y clickear “Continue”
# Verificar que aparece el error “Error: Postal Code is required”

def test_validar_campos_obligatorios_del_checkout():
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

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    cantidad_productos = len(productos)

    botones = driver.find_elements(By.CLASS_NAME, 'btn_inventory')

    for boton in botones:
        boton.click()
    time.sleep(2)

# Verifico que todos los productos estén en el carrito.

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    productos_carrito = driver.find_elements(By.CLASS_NAME, 'cart_item')

    assert len(productos_carrito) == cantidad_productos

    print("Test OK - Todos los productos están en el carrito")
    time.sleep(2)
    driver.find_element(By.ID, 'checkout').click()
    time.sleep(2)

    driver.find_element(By.ID, 'first-name').send_keys('Florencia')
    time.sleep(2)

    driver.find_element(By.ID, 'continue').click()
    time.sleep(2)

#   Verifico error de apellido obligatorio

    error = driver.find_element(By.CLASS_NAME, 'error-message-container').text

    assert error == 'Error: Last Name is required'

    print("Test OK - Se muestra el error de apellido obligatorio")

    driver.find_element(By.ID, 'last-name').send_keys('Balderian')
    time.sleep(2)

    driver.find_element(By.ID, 'continue').click()
    time.sleep(2)

# Verifico error de código postal obligatorio

    error = driver.find_element(By.CLASS_NAME, 'error-message-container').text

    assert error == 'Error: Postal Code is required'

    print("Test OK - Se muestra el error de código postal obligatorio")
    time.sleep(3)

    driver.quit()

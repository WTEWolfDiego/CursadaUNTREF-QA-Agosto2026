from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Caso 3
# El usuario se loguea al sitio como usuario standard user
# Agregar un elemento al carrito
# Ir al carrito
# Remover el artículo
# Verificar que el sitio no tiene artículos agregados
# Ir a “Continue Shopping”
# Agregar 2 elementos
# Ir al carrito
# Verificar que los elementos existan
# Hacer el checkout
# Finalizar la compra
# Verificar que la compra fue realizada

def test_validar_compra_exitosa():

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

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(2)

    # Verifico que el carrito esté vacío

    productos = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(productos) == 0, "El carrito no está vacío"

    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(2)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Verifico que existan los dos productos

    nombres = [
        producto.text
        for producto in driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
    ]
    esperados = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    assert sorted(nombres) == sorted(esperados), (
        f"Productos esperados: {esperados}; encontrados: {nombres}"
    )
    print("Test OK - Los productos en el carrito son correctos")

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "first-name").send_keys("Florencia")
    time.sleep(2)

    driver.find_element(By.ID, "last-name").send_keys("Balderian")
    time.sleep(2)

    driver.find_element(By.ID, "postal-code").send_keys("1407")
    time.sleep(2)

    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # Verifico compra exitosa

    mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensaje == "Thank you for your order!", "La compra no se realizó correctamente"
    time.sleep(3)
    print("Test OK - Compra realizada correctamente")
    
    driver.quit()

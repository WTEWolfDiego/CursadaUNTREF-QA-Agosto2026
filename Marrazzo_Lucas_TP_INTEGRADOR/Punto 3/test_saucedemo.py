
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

def test_ordenar_productos_por_precio():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    productos = driver.find_element(By.CLASS_NAME, "product_sort_container")
    Select(productos).select_by_value("lohi")

    precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    lista_precios = [float(precio.text.replace("$", "")) for precio in precios]

    assert lista_precios == sorted(lista_precios)

    time.sleep(3)
    driver.quit()

def test_carrito_y_validaciones_checkout():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for boton in botones:
        boton.click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verificar que estén todos los productos
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) == 6
    # Ir al checkout
    driver.find_element(By.ID, "checkout").click()

    # Completar solamente el nombre
    driver.find_element(By.ID, "first-name").send_keys("Lucas")
    driver.find_element(By.ID, "continue").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Error: Last Name is required" in error.text

    # Completar el apellido, pero dejar vacío el código postal
    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "continue").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Error: Postal Code is required" in error.text

    time.sleep(2)
    driver.quit()


def test_eliminar_producto_y_finalizar_compra():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    print("URL después del login:", driver.current_url)
    print("Cantidad de botones:", len(driver.find_elements(By.CLASS_NAME, "btn_inventory")))
    print("Cantidad de enlaces al carrito:", len(driver.find_elements(By.CLASS_NAME, "shopping_cart_link")))
    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    botones[0].click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    print("URL del carrito:", driver.current_url)
    print("Título:", driver.title)
    # Volver a comprar dos productos
    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(2)
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)

    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    print("URL:", driver.current_url)
    print("Título:", driver.title)
    print("Cantidad de botones:", len(botones))
    botones[0].click()
    botones[1].click()
    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    botones[0].click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) == 2

    # Completar la compra
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Lucas")
    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("1870")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "finish").click()

    confirmacion = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in confirmacion.text

    time.sleep(2)
    driver.quit()

import pytest

import time
 
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
 
 
# ==========================================================

# CONFIG

RACIÓN PARA GRABAR LA DEMO

# ==========================================================
 
# Cantidad de segundos entre acciones

PAUSA = 2
 
 
# ==========================================================

# CONFIGURACIÓN DEL DRIVER

# ==========================================================
 
@pytest.fixture

def driver():
 
    # Configuración de Chrome para evitar

    # la alerta de contraseña vulnerable

    opciones = webdriver.ChromeOptions()
 
    opciones.add_experimental_option(

        "prefs",

        {

            "credentials_enable_service": False,

            "profile.password_manager_enabled": False,

            "profile.password_manager_leak_detection": False

        }

    )
 
    # Desactivar notificaciones del navegador

    opciones.add_argument("--disable-notifications")
 
    # Abrir Chrome con las opciones configuradas

    driver = webdriver.Chrome(options=opciones)
 
    driver.maximize_window()
 
    # Entrar a SauceDemo

    driver.get("https://www.saucedemo.com/")
 
    time.sleep(PAUSA)
 
    yield driver
 
    # Pausa final para poder ver el resultado

    time.sleep(3)
 
    # Cerrar navegador

    driver.quit()
 
 
# ==========================================================

# FUNCIÓN DE LOGIN

# ==========================================================
 
def login(driver):
 
    usuario = driver.find_element(By.ID, "user-name")

    usuario.send_keys("standard_user")
 
    time.sleep(PAUSA)
 
    password = driver.find_element(By.ID, "password")

    password.send_keys("secret_sauce")
 
    time.sleep(PAUSA)
 
    driver.find_element(By.ID, "login-button").click()
 
    time.sleep(PAUSA)
 
 
# ==========================================================

# CASO 1

# Ordenar productos por precio de menor a mayor

# ==========================================================
 
def test_ordenar_productos_precio_menor_a_mayor(driver):
 
    print("\n--- CASO 1: ORDENAR PRODUCTOS ---")
 
    # Login

    login(driver)
 
    wait = WebDriverWait(driver, 10)
 
    # Esperar que aparezca el selector

    selector_element = wait.until(

        EC.presence_of_element_located(

            (By.CLASS_NAME, "product_sort_container")

        )

    )
 
    time.sleep(PAUSA)
 
    # Seleccionar Price (low to high)

    selector = Select(selector_element)

    selector.select_by_value("lohi")
 
    # Dejar visible el resultado ordenado

    time.sleep(4)
 
    # Obtener precios

    elementos_precio = driver.find_elements(

        By.CLASS_NAME,

        "inventory_item_price"

    )
 
    precios = [

        float(elemento.text.replace("$", ""))

        for elemento in elementos_precio

    ]
 
    print("Precios encontrados:", precios)
 
    # Verificar que estén ordenados

    assert precios == sorted(precios)
 
    print("CASO 1 OK: Los productos están ordenados.")
 
    time.sleep(3)
 
 
# ==========================================================

# CASO 2

# Agregar todos los productos y validar errores del checkout

# ==========================================================
 
def test_checkout_validacion_campos_obligatorios(driver):
 
    print("\n--- CASO 2: VALIDACIONES CHECKOUT ---")
 
    # Login

    login(driver)
 
    wait = WebDriverWait(driver, 10)
 
    # Obtener productos

    productos = wait.until(

        EC.presence_of_all_elements_located(

            (By.CLASS_NAME, "inventory_item")

        )

    )
 
    cantidad_productos = len(productos)
 
    print("Cantidad de productos:", cantidad_productos)
 
    time.sleep(PAUSA)
 
    # Agregar todos los productos al carrito

    botones_agregar = driver.find_elements(

        By.CSS_SELECTOR,

        "button.btn_inventory"

    )
 
    for boton in botones_agregar:

        boton.click()

        time.sleep(0.5)
 
    time.sleep(PAUSA)
 
    # Ir al carrito

    driver.find_element(

        By.CLASS_NAME,

        "shopping_cart_link"

    ).click()
 
    time.sleep(PAUSA)
 
    # Verificar productos del carrito

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    print(

        f"Productos esperados: {cantidad_productos} - "

        f"Productos en carrito: {len(productos_carrito)}"

    )
 
    assert len(productos_carrito) == cantidad_productos
 
    time.sleep(PAUSA)
 
    # Ir al checkout

    driver.find_element(By.ID, "checkout").click()
 
    time.sleep(PAUSA)
 
    # Ingresar solamente nombre

    driver.find_element(

        By.ID,

        "first-name"

    ).send_keys("Sandra")
 
    time.sleep(PAUSA)
 
    # Continuar

    driver.find_element(By.ID, "continue").click()
 
    time.sleep(3)
 
    # Verificar error Last Name

    error = driver.find_element(

        By.CSS_SELECTOR,

        "[data-test='error']"

    ).text
 
    print("Primer error:", error)
 
    assert error == "Error: Last Name is required"
 
    # Dejar visible el error

    time.sleep(3)
 
    # Ingresar apellido

    driver.find_element(

        By.ID,

        "last-name"

    ).send_keys("Prado")
 
    time.sleep(PAUSA)
 
    # Continuar nuevamente

    driver.find_element(By.ID, "continue").click()
 
    time.sleep(3)
 
    # Verificar error Postal Code

    error = driver.find_element(

        By.CSS_SELECTOR,

        "[data-test='error']"

    ).text
 
    print("Segundo error:", error)
 
    assert error == "Error: Postal Code is required"
 
    print("CASO 2 OK: Se validaron los campos obligatorios.")
 
    # Dejar visible el segundo error

    time.sleep(3)
 
 
# ==========================================================

# CASO 3

# Agregar, remover y realizar una compra completa

# ==========================================================
 
def test_compra_completa(driver):
 
    print("\n--- CASO 3: COMPRA COMPLETA ---")
 
    # Login

    login(driver)
 
    wait = WebDriverWait(driver, 10)
 
    # Obtener botones Add to cart

    botones_agregar = wait.until(

        EC.presence_of_all_elements_located(

            (By.CSS_SELECTOR, "button.btn_inventory")

        )

    )
 
    time.sleep(PAUSA)
 
    # Agregar primer producto

    botones_agregar[0].click()
 
    print("Se agregó un producto.")
 
    time.sleep(PAUSA)
 
    # Ir al carrito

    driver.find_element(

        By.CLASS_NAME,

        "shopping_cart_link"

    ).click()
 
    time.sleep(PAUSA)
 
    # Verificar que haya un producto

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    assert len(productos_carrito) == 1
 
    print("Producto encontrado en el carrito.")
 
    time.sleep(PAUSA)
 
    # Remover producto

    driver.find_element(

        By.CSS_SELECTOR,

        "button.cart_button"

    ).click()
 
    time.sleep(PAUSA)
 
    # Verificar carrito vacío

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    assert len(productos_carrito) == 0
 
    print("Carrito vacío correctamente.")
 
    time.sleep(PAUSA)
 
    # Continue Shopping

    driver.find_element(

        By.ID,

        "continue-shopping"

    ).click()
 
    time.sleep(PAUSA)
 
    # Obtener nuevamente los botones

    botones_agregar = wait.until(

        EC.presence_of_all_elements_located(

            (By.CSS_SELECTOR, "button.btn_inventory")

        )

    )
 
    # Agregar primer producto

    botones_agregar[0].click()
 
    time.sleep(1)
 
    # Agregar segundo producto

    botones_agregar[1].click()
 
    print("Se agregaron dos productos.")
 
    time.sleep(PAUSA)
 
    # Ir al carrito

    driver.find_element(

        By.CLASS_NAME,

        "shopping_cart_link"

    ).click()
 
    time.sleep(PAUSA)
 
    # Verificar que existan dos productos

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    print(

        "Productos encontrados en carrito:",

        len(productos_carrito)

    )
 
    assert len(productos_carrito) == 2
 
    time.sleep(PAUSA)
 
    # Checkout

    driver.find_element(

        By.ID,

        "checkout"

    ).click()
 
    time.sleep(PAUSA)
 
    # Nombre

    driver.find_element(

        By.ID,

        "first-name"

    ).send_keys("Sandra")
 
    time.sleep(1)
 
    # Apellido

    driver.find_element(

        By.ID,

        "last-name"

    ).send_keys("Prado")
 
    time.sleep(1)
 
    # Código postal

    driver.find_element(

        By.ID,

        "postal-code"

    ).send_keys("1653")
 
    time.sleep(PAUSA)
 
    # Continuar

    driver.find_element(

        By.ID,

        "continue"

    ).click()
 
    # Mostrar resumen de compra

    time.sleep(4)
 
    # Finalizar compra

    wait.until(

        EC.element_to_be_clickable(

            (By.ID, "finish")

        )

    ).click()
 
    time.sleep(4)
 
    # Verificar mensaje final

    mensaje = wait.until(

        EC.visibility_of_element_located(

            (By.CLASS_NAME, "complete-header")

        )

    ).text
 
    print("Mensaje final:", mensaje)
 
    assert mensaje == "Thank you for your order!"
 
    print("CASO 3 OK: Compra realizada correctamente.")
 
    # Dejar el mensaje final visible para el video

    time.sleep(5)
 
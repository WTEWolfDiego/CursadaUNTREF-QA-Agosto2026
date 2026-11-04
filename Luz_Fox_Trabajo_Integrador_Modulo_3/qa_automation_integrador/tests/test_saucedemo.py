# ==========================================================
# TRABAJO INTEGRADOR - QA AUTOMATION
# Automatización de SauceDemo con Selenium y Pytest
#
# Caso 1: Ordenar productos por precio ascendente
# Caso 2: Validar errores del formulario de checkout
# Caso 3: Agregar, eliminar y comprar productos
#
# Se utilizan pausas para observar el navegador.
# ==========================================================

# Librería para realizar pausas durante la ejecución
import time

# Framework para ejecutar las pruebas automatizadas
import pytest

# Librería Selenium para controlar el navegador
from selenium import webdriver

# Permite localizar elementos HTML
from selenium.webdriver.common.by import By

# Permite trabajar con listas desplegables y esperas
from selenium.webdriver.support.ui import Select, WebDriverWait

# Condiciones para esperar elementos de la página
from selenium.webdriver.support import expected_conditions as EC


# URL del sitio que vamos a automatizar
URL = "https://www.saucedemo.com/"

# Cantidad de segundos de pausa entre acciones
PAUSA = 1.5


# ==========================================================
# FIXTURE: CONFIGURACIÓN DEL NAVEGADOR
# ==========================================================

@pytest.fixture
def driver():

    # Crear las opciones de configuración de Chrome
    options = webdriver.ChromeOptions()

    # Desactivar los avisos del gestor de contraseñas
    # para evitar interrupciones durante las pruebas
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Abrir el navegador Chrome
    navegador = webdriver.Chrome(options=options)

    # Maximizar la ventana
    navegador.maximize_window()

    # Entregar el navegador al caso de prueba
    try:
        yield navegador

    finally:
        # Cerrar el navegador al finalizar la prueba
        navegador.quit()


# ==========================================================
# FUNCIÓN: INICIAR SESIÓN
# ==========================================================

def iniciar_sesion(driver):

    # Abrir SauceDemo
    driver.get(URL)

    # Esperar para observar la página de login
    time.sleep(PAUSA)

    # Localizar el campo usuario y escribir standard_user
    driver.find_element(
        By.ID, "user-name"
    ).send_keys("standard_user")

    time.sleep(PAUSA)

    # Localizar el campo contraseña y escribirla
    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    time.sleep(PAUSA)

    # Hacer clic en el botón Login
    driver.find_element(
        By.ID, "login-button"
    ).click()

    # Esperar hasta que aparezca el listado de productos
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Verificar que se abrió la página de inventario
    assert "inventory.html" in driver.current_url, (
        "No se pudo ingresar al inventario"
    )

    print("Login realizado correctamente")

    time.sleep(PAUSA)


# ==========================================================
# FUNCIÓN: IR AL CARRITO
# ==========================================================

def ir_al_carrito(driver):

    # Crear una espera máxima de 10 segundos
    wait = WebDriverWait(driver, 10)

    # Esperar hasta que el icono del carrito sea clickeable
    carrito = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    )

    time.sleep(PAUSA)

    # Hacer clic en el carrito
    carrito.click()

    # Esperar hasta que la URL corresponda al carrito
    wait.until(
        EC.url_contains("cart.html")
    )

    # Esperar hasta que aparezca el contenedor del carrito
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_list")
        )
    )

    print("Se ingresó al carrito")

    time.sleep(PAUSA)


# ==========================================================
# CASO 1: ORDENAR PRODUCTOS POR PRECIO ASCENDENTE
# ==========================================================

def test_ordenar_productos_precio_ascendente(driver):

    # Iniciar sesión con el usuario estándar
    iniciar_sesion(driver)

    # Crear una espera explícita
    wait = WebDriverWait(driver, 10)

    # Esperar a que aparezca el selector de ordenamiento
    selector = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "product_sort_container")
        )
    )

    time.sleep(PAUSA)

    # Seleccionar la opción Price (low to high)
    Select(selector).select_by_value("lohi")

    time.sleep(PAUSA)

    # Obtener todos los elementos que muestran precios
    elementos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item_price")
        )
    )

    # Crear una lista para guardar los precios
    precios = []

    # Recorrer todos los precios encontrados
    for elemento in elementos:

        # Obtener el texto del precio y eliminar el signo $
        precio_texto = elemento.text.replace("$", "")

        # Convertir el precio a número decimal
        precio = float(precio_texto)

        # Agregar el precio a la lista
        precios.append(precio)

    # Mostrar los precios obtenidos
    print("Precios encontrados:", precios)

    # Verificar que se encontraron productos
    assert len(precios) > 0, (
        "No se encontraron precios de productos"
    )

    # Verificar que los precios estén ordenados
    # de menor a mayor
    assert precios == sorted(precios), (
        f"Los precios no están ordenados: {precios}"
    )

    print("CASO 1: Los precios están ordenados correctamente")

    time.sleep(PAUSA)


# ==========================================================
# CASO 2: VALIDAR ERRORES DEL CHECKOUT
# ==========================================================

def test_validaciones_checkout(driver):

    # Iniciar sesión antes de buscar los productos
    iniciar_sesion(driver)

    # Crear una espera explícita
    wait = WebDriverWait(driver, 10)

    # Esperar hasta que aparezcan los productos
    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    # Guardar los nombres de los productos
    nombres = []

    for producto in productos:

        nombre = producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        nombres.append(nombre)

    # Verificar que existan productos
    assert len(nombres) > 0, (
        "No se encontraron productos"
    )

    print("Productos encontrados:", nombres)

    # Agregar todos los productos al carrito
    for producto in productos:

        # Localizar el botón Add to cart del producto
        boton = producto.find_element(
            By.CSS_SELECTOR, "button.btn_inventory"
        )

        # Hacer clic en el botón
        boton.click()

        # Pausa para observar cómo se agrega
        time.sleep(PAUSA)

    # Ir al carrito
    ir_al_carrito(driver)

    # Obtener los nombres de los productos del carrito
    elementos_carrito = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    nombres_carrito = []

    for elemento in elementos_carrito:
        nombres_carrito.append(elemento.text)

    # Verificar que todos los productos estén en el carrito
    assert sorted(nombres_carrito) == sorted(nombres), (
        "Los productos del carrito no coinciden"
    )

    print("Todos los productos están en el carrito")

    time.sleep(PAUSA)

    # Esperar que el botón Checkout esté disponible
    boton_checkout = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    )

    # Ingresar al checkout
    boton_checkout.click()

    # Esperar hasta que aparezca el campo First Name
    campo_nombre = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )

    time.sleep(PAUSA)

    # Ingresar solamente el nombre
    campo_nombre.send_keys("Luz")

    time.sleep(PAUSA)

    # Hacer clic en Continue sin ingresar apellido
    driver.find_element(
        By.ID, "continue"
    ).click()

    # Esperar que aparezca el mensaje de error
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="error"]')
        )
    )

    # Verificar que se solicite el apellido
    assert error.text == "Error: Last Name is required", (
        f"Mensaje incorrecto: {error.text}"
    )

    print("Validación de apellido obligatorio: OK")

    time.sleep(PAUSA)

    # Ingresar el apellido
    driver.find_element(
        By.ID, "last-name"
    ).send_keys("Fox")

    time.sleep(PAUSA)

    # Hacer clic en Continue sin código postal
    driver.find_element(
        By.ID, "continue"
    ).click()

    # Esperar el mensaje de código postal obligatorio
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="error"]'),
            "Error: Postal Code is required"
        )
    )

    # Obtener el mensaje de error
    error = driver.find_element(
        By.CSS_SELECTOR, '[data-test="error"]'
    )

    # Verificar el mensaje exacto
    assert error.text == "Error: Postal Code is required", (
        f"Mensaje incorrecto: {error.text}"
    )

    print("Validación de código postal obligatorio: OK")
    print("CASO 2: Validaciones del checkout correctas")

    time.sleep(PAUSA)


# ==========================================================
# CASO 3: AGREGAR, ELIMINAR Y COMPRAR PRODUCTOS
# ==========================================================

def test_compra_completa(driver):

    # Iniciar sesión en SauceDemo
    iniciar_sesion(driver)

    # Crear una espera explícita
    wait = WebDriverWait(driver, 10)

    # Esperar que aparezcan los productos
    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    # Verificar que existan al menos dos productos
    assert len(productos) >= 2, (
        "No hay suficientes productos"
    )

    # Obtener el nombre del primer producto
    primer_nombre = productos[0].find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    print("Primer producto:", primer_nombre)

    # Agregar el primer producto al carrito
    productos[0].find_element(
        By.CSS_SELECTOR, "button.btn_inventory"
    ).click()

    time.sleep(PAUSA)

    # Ir al carrito
    ir_al_carrito(driver)

    # Obtener los productos agregados
    elementos = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    nombres_carrito = []

    for elemento in elementos:
        nombres_carrito.append(elemento.text)

    # Verificar que esté el primer producto
    assert nombres_carrito == [primer_nombre], (
        "El producto no está en el carrito"
    )

    print("Producto agregado correctamente")

    time.sleep(PAUSA)

    # Localizar el botón Remove del producto
    boton_remove = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".cart_item button")
        )
    )

    # Eliminar el producto
    boton_remove.click()

    # Esperar que desaparezcan los artículos del carrito
    wait.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    # Verificar que el carrito esté vacío
    assert len(
        driver.find_elements(By.CLASS_NAME, "cart_item")
    ) == 0, "El carrito no está vacío"

    print("Producto eliminado correctamente")

    time.sleep(PAUSA)

    # Hacer clic en Continue Shopping
    driver.find_element(
        By.ID, "continue-shopping"
    ).click()

    # Esperar que se abra el inventario
    wait.until(
        EC.url_contains("inventory.html")
    )

    # Esperar a que aparezcan nuevamente los productos
    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    # Verificar que existan al menos dos productos
    assert len(productos) >= 2, (
        "No hay dos productos disponibles"
    )

    time.sleep(PAUSA)

    # Guardar los nombres de los dos primeros productos
    nombres = []

    for producto in productos[:2]:

        nombre = producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        nombres.append(nombre)

    print("Productos seleccionados:", nombres)

    # Agregar los dos productos al carrito
    for producto in productos[:2]:

        producto.find_element(
            By.CSS_SELECTOR, "button.btn_inventory"
        ).click()

        time.sleep(PAUSA)

    # Esperar a que el contador del carrito indique 2
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"),
            "2"
        )
    )

    # Ir nuevamente al carrito
    ir_al_carrito(driver)

    # Obtener los nombres de los productos del carrito
    elementos_carrito = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    nombres_carrito = []

    for elemento in elementos_carrito:
        nombres_carrito.append(elemento.text)

    # Verificar que estén los dos productos
    assert sorted(nombres_carrito) == sorted(nombres), (
        "Los productos del carrito no coinciden"
    )

    print("Los dos productos están en el carrito")

    time.sleep(PAUSA)

    # Hacer clic en Checkout
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    ).click()

    # Esperar que aparezca el formulario
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )

    time.sleep(PAUSA)

    # Ingresar el nombre
    driver.find_element(
        By.ID, "first-name"
    ).send_keys("Luz")

    time.sleep(PAUSA)

    # Ingresar el apellido
    driver.find_element(
        By.ID, "last-name"
    ).send_keys("Fox")

    time.sleep(PAUSA)

    # Ingresar el código postal
    driver.find_element(
        By.ID, "postal-code"
    ).send_keys("1030")

    time.sleep(PAUSA)

    # Continuar al resumen de compra
    driver.find_element(
        By.ID, "continue"
    ).click()

    # Esperar a que aparezca el resumen del checkout
    wait.until(
        EC.url_contains("checkout-step-two.html")
    )

    # Obtener los productos del resumen
    productos_resumen = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    # Verificar que existan dos productos
    assert len(productos_resumen) == 2, (
        "El resumen no contiene dos productos"
    )

    print("Resumen de compra correcto")

    time.sleep(PAUSA)

    # Hacer clic en Finish para finalizar la compra
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "finish")
        )
    ).click()

    # Esperar el mensaje de compra finalizada
    mensaje = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    ).text

    # Verificar el mensaje de confirmación
    assert mensaje == "Thank you for your order!", (
        f"Mensaje inesperado: {mensaje}"
    )

    print("CASO 3: Compra realizada correctamente")

    # Pausa final para observar la confirmación
    time.sleep(3)
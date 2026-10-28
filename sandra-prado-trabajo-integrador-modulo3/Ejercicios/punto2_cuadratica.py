import math
 
 
def calcular_raices(a, b, c):
    if a == 0:
        raise ValueError("El valor de 'a' no puede ser 0.")
 
    discriminante = b ** 2 - 4 * a * c
 
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2
 
    elif discriminante == 0:
        x = -b / (2 * a)
        return x, x
 
    else:
        return "La ecuación no tiene raíces reales"
 
 
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
 
resultado = calcular_raices(a, b, c)
 
print("Resultado:", resultado)
def test_compra_completa(driver):
 
    # LOGIN

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()
 
    wait = WebDriverWait(driver, 10)
 
    # Agregar un producto

    botones_agregar = wait.until(

        EC.presence_of_all_elements_located(

            (By.CSS_SELECTOR, "button.btn_inventory")

        )

    )
 
    botones_agregar[0].click()
 
    # Ir al carrito

    driver.find_element(

        By.CLASS_NAME,

        "shopping_cart_link"

    ).click()
 
    # Verificar que haya un producto

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    assert len(productos_carrito) == 1
 
    # Remover el producto

    driver.find_element(

        By.CSS_SELECTOR,

        "button.cart_button"

    ).click()
 
    # Verificar que el carrito esté vacío

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    assert len(productos_carrito) == 0
 
    print("Carrito vacío correctamente")
 
    # Continue Shopping

    driver.find_element(

        By.ID,

        "continue-shopping"

    ).click()
 
    # Agregar dos productos

    botones_agregar = wait.until(

        EC.presence_of_all_elements_located(

            (By.CSS_SELECTOR, "button.btn_inventory")

        )

    )
 
    botones_agregar[0].click()

    botones_agregar[1].click()
 
    # Ir al carrito

    driver.find_element(

        By.CLASS_NAME,

        "shopping_cart_link"

    ).click()
 
    # Verificar que existan los dos productos

    productos_carrito = driver.find_elements(

        By.CLASS_NAME,

        "cart_item"

    )
 
    assert len(productos_carrito) == 2
 
    print("Productos en carrito:", len(productos_carrito))
 
    # Checkout

    driver.find_element(

        By.ID,

        "checkout"

    ).click()
 
    # Completar datos

    driver.find_element(

        By.ID,

        "first-name"

    ).send_keys("Sandra")
 
    driver.find_element(

        By.ID,

        "last-name"

    ).send_keys("Prado")
 
    driver.find_element(

        By.ID,

        "postal-code"

    ).send_keys("1653")
 
    driver.find_element(

        By.ID,

        "continue"

    ).click()
 
    # Finalizar compra

    wait.until(

        EC.element_to_be_clickable(

            (By.ID, "finish")

        )

    ).click()
 
    # Verificar compra realizada

    mensaje = wait.until(

        EC.visibility_of_element_located(

            (By.CLASS_NAME, "complete-header")

        )

    ).text
 
    print("Mensaje final:", mensaje)
 
    assert mensaje == "Thank you for your order!"
 
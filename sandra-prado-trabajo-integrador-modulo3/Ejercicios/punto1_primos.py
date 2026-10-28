def es_primo(numero):
    if numero < 2:
        return False
 
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
 
    return True
 
 
numero = int(input("Ingrese un número: "))
 
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
    def test_checkout_validacion_campos_obligatorios(driver):
 
    # LOGIN
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
 
    wait = WebDriverWait(driver, 10)
 
    # Obtener todos los productos disponibles
    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )
 
    cantidad_productos = len(productos)
 
    # Agregar todos los productos al carrito
    botones_agregar = driver.find_elements(
        By.CSS_SELECTOR,
        "button.btn_inventory"
    )
 
    for boton in botones_agregar:
        boton.click()
 
    # Ir al carrito
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()
 
    # Verificar que estén todos los productos
    productos_carrito = driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )
 
    assert len(productos_carrito) == cantidad_productos
 
    print(
        f"Productos esperados: {cantidad_productos} - "
        f"Productos en carrito: {len(productos_carrito)}"
    )
 
    # Ir al checkout
    driver.find_element(By.ID, "checkout").click()
 
    # Ingresar solamente el nombre
    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys("Sandra")
 
    driver.find_element(By.ID, "continue").click()
 
    # Verificar error de apellido
    error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    ).text
 
    print("Primer error:", error)
 
    assert error == "Error: Last Name is required"
 
    # Ingresar apellido
    driver.find_element(
        By.ID,
        "last-name"
    ).send_keys("Prado")
 
    driver.find_element(By.ID, "continue").click()
 
    # Verificar error de código postal
    error = driver.find_element(
        By.CSS_SELECTOR,
        "[data-test='error']"
    ).text
 
    print("Segundo error:", error)
 
    assert error == "Error: Postal Code is required"
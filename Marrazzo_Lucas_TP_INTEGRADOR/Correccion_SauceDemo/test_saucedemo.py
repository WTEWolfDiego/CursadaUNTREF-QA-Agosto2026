
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crear_driver():
    options = Options()

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    options.add_argument("--disable-save-password-bubble")
    options.add_argument(
        "--disable-features=PasswordLeakDetection,PasswordManagerLeakDetection"
    )

    return webdriver.Chrome(options=options)


def hacer_clic(driver, tipo, valor):
    espera = WebDriverWait(driver, 15)
    boton = espera.until(EC.element_to_be_clickable((tipo, valor)))
    boton.click()


def escribir(driver, campo, texto):
    espera = WebDriverWait(driver, 15)
    casilla = espera.until(
        EC.visibility_of_element_located((By.ID, campo))
    )
    casilla.clear()
    casilla.send_keys(texto)


def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com/")

    escribir(driver, "user-name", "standard_user")
    escribir(driver, "password", "secret_sauce")
    hacer_clic(driver, By.ID, "login-button")

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )


def test_ordenar_productos_por_precio():
    driver = crear_driver()
    try:
        iniciar_sesion(driver)

        productos = driver.find_element(
            By.CLASS_NAME, "product_sort_container"
        )
        Select(productos).select_by_value("lohi")

        WebDriverWait(driver, 15).until(
            lambda d: len(
                d.find_elements(By.CLASS_NAME, "inventory_item_price")
            ) == 6
        )

        precios = [
            float(p.text.replace("$", ""))
            for p in driver.find_elements(
                By.CLASS_NAME, "inventory_item_price"
            )
        ]

        assert precios == sorted(precios)

    finally:
        driver.quit()


def test_carrito_y_validaciones_checkout():
    driver = crear_driver()
    try:
        iniciar_sesion(driver)

        botones = driver.find_elements(
            By.CSS_SELECTOR, "button[data-test^='add-to-cart']"
        )
        ids = [b.get_attribute("id") for b in botones]

        assert len(ids) == 6

        for id_boton in ids:
            hacer_clic(driver, By.ID, id_boton)

        WebDriverWait(driver, 15).until(
            lambda d: d.find_element(
                By.CLASS_NAME, "shopping_cart_badge"
            ).text == "6"
        )

        hacer_clic(driver, By.CLASS_NAME, "shopping_cart_link")

        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_elements(
                By.CLASS_NAME, "cart_item"
            )) == 6
        )

        assert len(driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )) == 6

        hacer_clic(driver, By.ID, "checkout")
        escribir(driver, "first-name", "Lucas")
        hacer_clic(driver, By.ID, "continue")

        error = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )
        assert "Error: Last Name is required" in error.text

        escribir(driver, "last-name", "Tester")
        hacer_clic(driver, By.ID, "continue")

        error = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )
        assert "Error: Postal Code is required" in error.text

    finally:
        driver.quit()


def test_eliminar_producto_y_finalizar_compra():
    driver = crear_driver()
    try:
        iniciar_sesion(driver)

        botones = driver.find_elements(
            By.CSS_SELECTOR, "button[data-test^='add-to-cart']"
        )

        assert len(botones) >= 2

        primer_producto = botones[0].get_attribute("id")
        hacer_clic(driver, By.ID, primer_producto)

        hacer_clic(driver, By.CLASS_NAME, "shopping_cart_link")

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        hacer_clic(driver, By.CSS_SELECTOR, ".cart_item button")

        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_elements(
                By.CLASS_NAME, "cart_item"
            )) == 0
        )

        assert len(driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )) == 0

        hacer_clic(driver, By.ID, "continue-shopping")

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_list")
            )
        )

        botones = driver.find_elements(
            By.CSS_SELECTOR, "button[data-test^='add-to-cart']"
        )

        ids = [
            botones[0].get_attribute("id"),
            botones[1].get_attribute("id")
        ]

        for id_boton in ids:
            hacer_clic(driver, By.ID, id_boton)

        WebDriverWait(driver, 15).until(
            lambda d: d.find_element(
                By.CLASS_NAME, "shopping_cart_badge"
            ).text == "2"
        )

        hacer_clic(driver, By.CLASS_NAME, "shopping_cart_link")

        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_elements(
                By.CLASS_NAME, "cart_item"
            )) == 2
        )

        assert len(driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )) == 2

        hacer_clic(driver, By.ID, "checkout")
        escribir(driver, "first-name", "Lucas")
        escribir(driver, "last-name", "Tester")
        escribir(driver, "postal-code", "1870")

        hacer_clic(driver, By.ID, "continue")
        hacer_clic(driver, By.ID, "finish")

        mensaje = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        assert mensaje.text == "Thank you for your order!"

    finally:
        driver.quit()

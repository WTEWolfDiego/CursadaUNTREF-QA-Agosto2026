from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def hacer_clic(driver, tipo, valor):
    espera = WebDriverWait(driver, 15)
    boton = espera.until(EC.element_to_be_clickable((tipo, valor)))
    boton.click()


def escribir(driver, campo, texto):
    espera = WebDriverWait(driver, 15)
    for intento in range(3):
        casilla = espera.until(EC.element_to_be_clickable((By.ID, campo)))
        casilla.clear()
        casilla.send_keys(texto)
        if driver.find_element(By.ID, campo).get_attribute("value") == texto:
            return
    assert False, f"No se pudo completar {campo}"


def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com/")
    escribir(driver, "user-name", "standard_user")
    escribir(driver, "password", "secret_sauce")
    hacer_clic(driver, By.ID, "login-button")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )


# Caso 1 - Ordenar por precio

def test_ordenar_precios():
    driver = webdriver.Chrome()
    espera = WebDriverWait(driver, 15)
    try:
        iniciar_sesion(driver)
        ordenar = driver.find_element(By.CLASS_NAME, "product_sort_container")
        Select(ordenar).select_by_visible_text("Price (low to high)")

        espera.until(lambda d: len(d.find_elements(By.CLASS_NAME, "inventory_item_price")) > 0)
        precios = []
        for producto in driver.find_elements(By.CLASS_NAME, "inventory_item_price"):
            precios.append(float(producto.text.replace("$", "")))

        assert precios == sorted(precios)
        print("Caso 1: precios ordenados correctamente")
    finally:
        driver.quit()


# Caso 2 - Validar checkout

def test_validaciones_checkout():
    driver = webdriver.Chrome()
    espera = WebDriverWait(driver, 15)
    try:
        iniciar_sesion(driver)

        botones = driver.find_elements(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
        ids = [boton.get_attribute("id") for boton in botones]
        assert len(ids) > 0
        for id_boton in ids:
            hacer_clic(driver, By.ID, id_boton)

        espera.until(lambda d: d.find_element(By.CLASS_NAME, "shopping_cart_badge").text == str(len(ids)))
        hacer_clic(driver, By.CLASS_NAME, "shopping_cart_link")
        espera.until(lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == len(ids))

        hacer_clic(driver, By.ID, "checkout")
        espera.until(EC.visibility_of_element_located((By.ID, "first-name")))

        escribir(driver, "first-name", "Ana")
        hacer_clic(driver, By.ID, "continue")
        espera.until(lambda d: "Last Name is required" in d.find_element(By.CSS_SELECTOR, "[data-test='error']").text)

        escribir(driver, "last-name", "Garcia")
        hacer_clic(driver, By.ID, "continue")
        espera.until(lambda d: "Postal Code is required" in d.find_element(By.CSS_SELECTOR, "[data-test='error']").text)

        print("Caso 2: validaciones correctas")
    finally:
        driver.quit()


# Caso 3 - Finalizar compra

def test_finalizar_compra():
    driver = webdriver.Chrome()
    espera = WebDriverWait(driver, 15)
    try:
        iniciar_sesion(driver)

        botones = driver.find_elements(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
        assert len(botones) >= 2
        hacer_clic(driver, By.ID, botones[0].get_attribute("id"))
        hacer_clic(driver, By.CLASS_NAME, "shopping_cart_link")
        espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
        hacer_clic(driver, By.CSS_SELECTOR, ".cart_item button")
        espera.until(lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == 0)

        hacer_clic(driver, By.ID, "continue-shopping")
        espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        botones = driver.find_elements(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
        assert len(botones) >= 2
        ids = [botones[0].get_attribute("id"), botones[1].get_attribute("id")]
        for id_boton in ids:
            hacer_clic(driver, By.ID, id_boton)

        espera.until(lambda d: d.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2")
        hacer_clic(driver, By.CLASS_NAME, "shopping_cart_link")
        espera.until(lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == 2)

        hacer_clic(driver, By.ID, "checkout")
        espera.until(EC.visibility_of_element_located((By.ID, "first-name")))
        escribir(driver, "first-name", "Ana")
        escribir(driver, "last-name", "Garcia")
        escribir(driver, "postal-code", "1000")
        hacer_clic(driver, By.ID, "continue")
        espera.until(EC.visibility_of_element_located((By.ID, "finish")))
        hacer_clic(driver, By.ID, "finish")

        mensaje = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert mensaje.text == "Thank you for your order!"
        print("Caso 3: compra finalizada correctamente")
    finally:
        driver.quit()

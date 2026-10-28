import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Abriendo el navegador en ventana maximizada y navegando a Saucedemo.
#Maximizo la ventana y le doy tiempo con un sleep por las dudas
#Las primeras 7 líneas del código son para evitar que salga el popup de Chrome de "contraseña insegura", nos habían pasado un código en clase pero no me funcionó así que lo saqué Googleando en un rato
opciones = webdriver.ChromeOptions()
opciones.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})
opciones.add_argument("--disable-features=SafeBrowsing,PasswordLeakToggleMove")
driver = webdriver.Chrome(options=opciones)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)

def test_ordenar_por_precio():
    #Caso 1
    #Primero necesito buscar los elementos por ID del formulario, tanto el de usuario como el de contraseña.
    #Decidí que la mejor manera es por ID porque el sitio de Saucedemo está bien codeado y pensado para ser testeado por lo cual los campos de user y pass tienen un id único.
    #Con un poco de ayuda de Google y Stackoverflow implementé la que me pareció la manera más práctica de hacerlo:
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    #Ahora tengo que hacer click en el botón de log in que convenientemente también tiene un id único
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    #Esta parte fue la que más me costó.
    #Entendí conceptualmente lo que había que hacer (clickear en el dropdown de order by, seleccionar la tercera opción low to high y después extraer los precios de la página para validar)
    #pero realmente estuve un rato largo rompiéndome la cabeza, al final quedó una solución muy rústica que SEGURO se puede hacer de alguna manera más elegante (que seguro el profe la explicó pero yo no la recuerdo en este momento)
    dropdown_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select_orden = Select(dropdown_element)
    #Acá usé el visible text porque me pareció lo más fácil, seguramente haya alguna manera de seleccionar los elementos de la lista de manera menos hardcodeada
    select_orden.select_by_visible_text("Price (low to high)")

    #Y ahora viene toda la parte de la validación que es bastante enredada y rústica pero fue lo que se me ocurrió con ayuda de los apuntes y Google
    #Primero busco los precios de los productos en la página
    precio_productos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    #Ahora hice un masacote para extraer el texto y limpiarlo para poder ordenarlos de menor a mayor
    precios = [float(p.text.replace("$", "")) for p in precio_productos]
    #Después me copié todos esos precios a una lista ordenada de menor a mayor
    precios_expected = sorted(precios)
    #Y finalmente en el assert comparo los precios de la página con los de la lista ordenada de menor a mayor. Si los precios del sitio y de la lista ordenada coinciden, es pass. Si los precios en el sitio no se ordenaron de menor a mayor, no coincide con la lista ordenada y es fail.
    assert precios == precios_expected

    time.sleep(3)

    driver.quit()

##NOTA IMPORTANTE: Le añadí 1 millón de time.sleeps para que se pueda ver la ejecución en video, porque de otra manera se ejecuta todo casi instantáneamente y no se ve nada de lo que hace la automatización
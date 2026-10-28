import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

def test_checkout_errores():
#Acá encontré Googleando que se puede usar un "try/finally" para que el navegador no se quede colgado si falla algo en el medio porque me molestaba mucho al ir escribiendo y probando.
#Con el finally, si algo se rompe, salta directo ahí y ejecuta lo que venga al final (en este caso cerrar el navegador con driver.quit()
    try:
        #Acá entramos al sitio y hacemos login como en el Caso 1, no cambia nada               
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        #Acá tuve que usar lo de buscar por XPATH porque no se me ocurrió otra manera de hacer "únicos" a los botones de agregar al carrito, entonces simplemente con esto recorro el sitio y busca todos los botones
        #Me costó bastante cranear esto y tuve que usar mucho Google, StackOverflow y hasta pregunté en un Discord de programación en el que estoy para que me dieran una mano
        #La función len se usa para contar los botones que encontré para añadir al carrito, que es equivalente al número de productos
        botones_add = driver.find_elements(By.XPATH, "//button[starts-with(@id, 'add-to-cart')]")
        total_productos = len(botones_add)        
        for boton in botones_add:
            boton.click()
        time.sleep(1)
            
        #Clickeamos en el carrito de compras que gracias a dios tiene un nombre único para poder seleccionar
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        
        #Acá usé la función len otra vez para hacer la comparación entre el total de productos en la página y el total en el carrito
        items_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items_en_carrito) == total_productos
        time.sleep(1)
        
        #Vamos al checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        
        #Acá ingresé sólo el primer nombre y dejé el resto de campos vacíos para triggerear el error
        driver.find_element(By.ID, "first-name").send_keys("Pete")
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        
        #Acá verifico que aparezca el error tal cual tiene que aparecer
        mensaje_error = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Error: Last Name is required" in mensaje_error
        time.sleep(1)
        
        #Ahora ingreso solamente el apellido y continuo para triggerear el otro error
        driver.find_element(By.ID, "last-name").send_keys("Mitchell")
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        
        #Y finalmente verifico que el error del código postal aparezca exactamente como tiene que aparecer
        mensaje_error_2 = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Error: Postal Code is required" in mensaje_error_2        
        time.sleep(1)

    finally:
        # 11. Cerrar el navegador pase lo que pase (incluso si falla un assert)
        driver.quit()

##NOTA IMPORTANTE: Le añadí 1 millón de time.sleeps para que se pueda ver la ejecución en video, porque de otra manera se ejecuta todo casi instantáneamente y no se ve nada de lo que hace la automatización
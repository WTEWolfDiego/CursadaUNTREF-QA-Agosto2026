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

        #Agregamos un elemento al carrito (la mochila en este caso), vamos al carrito y lo removemos seleccionando por ID y por clase como ya hicimos en otros ejercicios
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)            
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()              
        time.sleep(1)
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        
        #Verificamos que no haya cosas en el carrito usando len que va a dar 0 siempre que esté vacío y volvemos
        items_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items_en_carrito) == 0
        time.sleep(1)            
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(1)
        
        #Agregamos 2 elementos al carrito y verificamos que ambos existan otra vez con el truco de len
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)        
        items_en_carrito_nuevos = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items_en_carrito_nuevos) == 2
        time.sleep(1)
        
        #Hacemos el proceso de checkout como ya hicimos en el ejercicio anterior
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        driver.find_element(By.ID, "first-name").send_keys("Nick")
        driver.find_element(By.ID, "last-name").send_keys("Bradshaw")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        
        #Finalizamos la compra
        driver.find_element(By.ID, "finish").click()
        time.sleep(1)
        
        #Verificamos que la compra se hizo exitosamente (acá usé el mensaje que sale al comprar, quizá haya otra manera de verificar la compra pero no se me ocurrió otra)
        mensaje_exito = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order" in mensaje_exito
        time.sleep(1)

    finally:
        # Cerrar el navegador al finalizar pase lo que pase
        driver.quit()

##NOTA IMPORTANTE: Le añadí 1 millón de time.sleeps para que se pueda ver la ejecución en video, porque de otra manera se ejecuta todo casi instantáneamente y no se ve nada de lo que hace la automatización
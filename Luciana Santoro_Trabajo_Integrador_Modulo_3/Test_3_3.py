# Caso 2
# El usuario se loguea al sitio como usuario standard user
# ● Agregar un elemento al carrito
# ● Ir al carrito
# ● Remover el artículo
# ● Verificar que el sitio no tiene artículos agregados
# ● Ir a “Continue Shopping”
# ● Agregar 2 elementos
# ● Ir al carrito
# ● Verificar que los elementos existan
# ● Hacer el checkout
# ● Finalizar la compra
# ● Verificar que la compra fue realizada

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


###configuracion chrome por alerta de contraseña vulnerable -> Chequear donde va
opciones = webdriver.ChromeOptions()
opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
driver = webdriver.Chrome(options=opciones)

# ir a la página
driver.get("https://www.saucedemo.com")

#buena práctica = maximizar la ventana
driver.maximize_window()

# espera que cargue
time.sleep(1) 

#ubicar el formulario y completarlo como usuario
driver.find_element(By.ID,"user-name").send_keys("standard_user")
print("Se ingresó el usuario")

#ubicar el formulario y completar el pass 
driver.find_element(By.ID,"password").send_keys("secret_sauce")
print("Se ingresó la contraseña")

time.sleep(1) 

#ubicar el boton de login y clickearlo
driver.find_element(By.ID,"login-button").click()
print("Se inició sesión")

time.sleep(1) 

#ubicar los botones de agregar al carrito
botones_agregar_carrito = driver.find_elements(By.CLASS_NAME, "btn_inventory")

# https://saucelabs.com/resources/blog/selenium-with-python-for-automated-testing
# reconfigurado para que apriete uno solo
for boton in botones_agregar_carrito[:1]:
    boton.click()
print("Se agregó un producto al Carrito")

time.sleep(1) 

# ir al carrito
driver.find_element(By.ID,"shopping_cart_container").click()

time.sleep(1) 

# extraer la cantidad de productos en carrito
cantidadEnCarrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
# retirada de código extra y asignación a otra variable
cantidadEnCarritoTxt = cantidadEnCarrito.text
# Conversión a Int porque sino falla, compara Str con Int
cantidadEnCarritoInt = int(cantidadEnCarritoTxt)

print(f"Antes de remover los productos, hay {cantidadEnCarritoInt} en el carrito.")

time.sleep(1) 

# #ubicar el botón de remover - no sirvió, no es iterable. Para evaluar otro día si vale la pena.
# botones_quitar_carrito = driver.find_elements(By.CLASS_NAME, "btn_inventory")
# # sin index? 
# for boton in botones_quitar_carrito:
#     boton.click()
# time.sleep(1) 

#remueve puntualmente la remera
#driver.find_element(By.ID,"remove-test.allthethings()-t-shirt-(red)").click
# por xpath porque no sé qué item agregó el loop. 
# Corro el riesgo de que agregue otro y no sea el Remove correcto
# TODO: exactamente las partes y como se arma un XPATH
# DEJA DE OLVIDARTE LOS BENDITOS Y HETEROSEXUALES PARENTESIS
driver.find_element(By.XPATH,"//button[@class='btn btn_secondary btn_small cart_button']").click()

time.sleep(1) 

# Revisar nuevamente la cantidad en el carrito ahora 
# QUE RESULTA Y ACONTECE: CAMBIA DE NOMBRE DESPUES DE REMOVER EL ITEM GAH
# cantidad_carrito_removido = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")

cantidad_carrito_removido = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
# retirada de código extra y asignación a otra variable
cantidad_carrito_removido_texto = cantidad_carrito_removido.text


# #por qué fallaba: si no hay nada en el carrito, no devuelve cero, devuelve vacío. 0 =/= vacío, de ahí la conversión a 0 y un numero comparable
# def chequear_string_vacia(cantidad_carrito_removido_texto):
#     if cantidad_carrito_removido_texto == "":
#         cantidad_carrito_removido_int = 0
#         return cantidad_carrito_removido_int
#     else:
#         cantidad_carrito_removido_int = int(cantidad_carrito_removido_texto)
#         return cantidad_carrito_removido_int
    
# cantidad_carrito_removido_int = chequear_string_vacia(cantidad_carrito_removido_texto)


# Conversión a Int porque sino falla, compara Str con Int - 
#cantidad_carrito_removido_int = int(cantidad_carrito_removido)
#print(cantidad_carrito_removido_int)
# print(f"Después de remover los productos del carrito, hay {cantidad_carrito_removido_int } en el carrito.")

#assert cantidad_carrito_removido_int == 0, "No se quitaron los productos del carrito"

# después de hacer todo lo anterior, se me ocurrió que podía hacer el assert directamente sobre el vacío mismo.
assert cantidad_carrito_removido_texto == "", "No se quitaron los productos del carrito"
print("Se removieron los productos del carrito")

time.sleep(1) 

# buscar continue shopping
driver.find_element(By.ID,"continue-shopping").click()

time.sleep(1)

#otra vez hay que asignarlo a variable?
botones_agregar_carrito = driver.find_elements(By.CLASS_NAME, "btn_inventory")

# reagregar al carrito
for boton in botones_agregar_carrito[:2]:
    boton.click()

time.sleep(1) 

# ir al carrito
driver.find_element(By.ID,"shopping_cart_container").click()

# extraer la cantidad de productos en carrito
cantidadEnCarrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
# retirada de código extra y asignación a otra variable
cantidadEnCarritoTxt = cantidadEnCarrito.text
# Conversión a Int porque sino falla, compara Str con Int
cantidadEnCarritoInt = int(cantidadEnCarritoTxt)

print(f"Ahora hay {cantidadEnCarritoInt} productos en el carrito.")

assert cantidadEnCarritoInt == 2, "La cantidad de productos en el carrito no es la esperada. Se esperaban 2 productos."

time.sleep(1) 

driver.find_element(By.ID,"checkout").click()
time.sleep(1) 

# completar el formulario
driver.find_element(By.ID,"first-name").send_keys("Carrot")
driver.find_element(By.ID,"last-name").send_keys("Ironfoundersson")
driver.find_element(By.ID,"postal-code").send_keys("1234")

print("Se completó el formulario con los datos del usuario.")
time.sleep(1) 

driver.find_element(By.ID,"continue").click()
time.sleep(1) 

driver.find_element(By.ID,"finish").click()
time.sleep(1) 
print("Se completó el checkout")

mensaje_check_out = driver.find_element(By.XPATH,"//h2[@class='complete-header']")
mensaje_check_out_text = mensaje_check_out.text

assert mensaje_check_out_text == "Thank you for your order!", "Hubo fallas en la compra"

print("Compra realizada con éxito, no se detectaron errores en esta prueba")

time.sleep(1) 

driver.quit()
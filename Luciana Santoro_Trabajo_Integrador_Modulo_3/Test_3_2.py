# Caso 2
# ● El usuario se loguea al sitio como usuario standard user
# ● Incorporar al carrito todos los elementos
# ● Ir al carrito
# ● Verificar que todos los elementos estén en el carrito
# ● Ir al checkout
# ● Ingresar nombre y clickear “Continue”
# ● Verificar que aparece el error “Error: Last Name is required”
# ● Ingresar un apellido y clickear “Continue”
# ● Verificar que aparece el error “Error: Postal Code is required”

#importa librería
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

#NOTA MENTAL: DESCANSAR. No encontraba los elementos en el DOM porque tadan tadan 
#NO COPIASTE EL COMANDO DEL CLICK Y LOGIN, POR ENDE NUNCA LLEGABA A ESE DOM
#Intentos anecdóticos:
# driver.find_element(By.DATATESTID,"//select[@ID='add-to-cart-sauce-labs-backpack']").click()
# driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
# driver.find_element(By.XPATH,"//select[@id='add-to-cart-sauce-labs-bike-light']").click()


#ubicar los botones Add to Cart y clickearlos? 
#Estos son mis intentos - funciona pero depende de que no cambie el ID ni agreguen más items (o los quiten)
# driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
# driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
# driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
# driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
# driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
# driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()


#este es el código de la documentación de Sauce Labs que inevitablemente iba a encontrar
# ok, propone asignar todos los botones porque tienen el mismo nombre a una variable y loopear el click
# la diferencia es que sólo le pide 3 clicks, acá queremos que agregue todos los botones. Remuevo index.
# Ventaja: es más flexible, no va a romper cuando cambie la cantidad o el nombre de los productos
# Si te cambia el class name o los nuevos tienen otro tipo de identificador, frutibesos.
# fuente: https://saucelabs.com/resources/blog/selenium-with-python-for-automated-testing

botones_agregar_carrito = driver.find_elements(By.CLASS_NAME, "btn_inventory")


#loop para clickear todos los carritos
def clickearBotones(botones_agregar_carrito):
    for boton in botones_agregar_carrito:
        boton.click()


# loop para contar botones de agregar al carrito disponibles
def contarBotones(botones_agregar_carrito):
    cantidadBotonesCarrito = 0
    for boton in botones_agregar_carrito: #por qué dice que no se usa?
        cantidadBotonesCarrito +=1
    return cantidadBotonesCarrito

# llamar al método y clickear los botones
clickearBotones(botones_agregar_carrito)

# asignación de cantidad de botones a una variable nueva
cantidadBotonesCarrito = contarBotones(botones_agregar_carrito)

print(f"Hay {cantidadBotonesCarrito} productos disponibles en la página para comprar")

time.sleep(2) 

# ok, ir al carrito y verificar que estén allí los productos
# idea 1: la documentación propone comparar por número. AHORA sabemos que hay 6 productos. Pero puede cambiar.
# se podría apuntar la igualdad del assert al contenido de de botones_agregar_carrito para no hardcodearlo
# TODO: posible problema: que pasa si se clickea dos veces el mismo producto y ninguna vez otro?
# hay forma de verificar que sea uno de cada uno? Tendrá que ver con comparar el .text del html y verificar que 
# sea distinto? Será revisitado en otro capítulo.
# en esta página sólo puede agregarse un item por producto, así que descartado que pueda duplicarse y agregar 2 del mismo

# RETENEME LA SESION SWAG Y LA GRAN SIETE ME HACES LOGUEARME CADA VEZ
driver.find_element(By.ID,"shopping_cart_container").click()

# El item en el DOM que cambia es shopping-cart-badge - TODO data-test se puede obtener con un findby?
# asignación de la cantidad de items a una variable -> es un solo valor, no hace falta una lista
cantidadEnCarrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")

# retirada de código extra y asignación a otra variable
cantidadEnCarritoTxt = cantidadEnCarrito.text
# Conversión a Int porque sino falla, compara Str con Int
cantidadEnCarritoInt = int(cantidadEnCarritoTxt)


print(f"Hay {cantidadEnCarritoTxt} productos en el Carrito")

#puede ser que falles porque estoy comparando string con int? SI.
assert cantidadEnCarritoInt == cantidadBotonesCarrito, "No se agregaron todos los items al Carrito"

print("Se agregaron todos los productos disponibles al carrito.")

print("Se intentará proceder al Checkout")
#continuar al checkout
driver.find_element(By.ID,"checkout").click()
time.sleep(1) 

#colocar sólo el nombre y clickear
driver.find_element(By.ID,"first-name").send_keys("Carrot")
time.sleep(1) 

print("Se completó el nombre del usuario solamente")

driver.find_element(By.ID,"continue").click()
time.sleep(1) 

# ● Verificar que aparece el error “Error: Last Name is required”
# No sirve porque está como por fuera de ese elemento el mensaje en el DOM. TODO revisar mas CSS y HTML
#mensajeErrorApellido = driver.find_element(By.CLASS_NAME,"error-message-container error")

# tiene que ser un escalón antes en el contenedor
mensajeErrorApellido = driver.find_element(By.XPATH,"//h3[@data-test='error']")
mensajeErrorApellidoText = mensajeErrorApellido.text
mensajeProgramadoApellido = "Error: Last Name is required"

print(f"El mensaje de error mostrado es {mensajeErrorApellidoText}")

assert mensajeErrorApellidoText == mensajeProgramadoApellido, "No se está mostrando el error por Apellido sin completar"

print("Se está mostrando el error 'Apellido sin completar' al usuario")

time.sleep(1) 

print("Se completó el apellido")
#colocar sólo el nombre y clickear
driver.find_element(By.ID,"last-name").send_keys("Ironfoundersson")
time.sleep(1) 

driver.find_element(By.ID,"continue").click()
time.sleep(1) 

mensajeErrorCodigoPostal = driver.find_element(By.XPATH,"//h3[@data-test='error']")
mensajeErrorCodigoPostalText = mensajeErrorCodigoPostal.text
mensajeProgramadoCodigoPostal = "Error: Postal Code is required"

print(f"El mensaje de error mostrado es {mensajeErrorCodigoPostalText}")

assert mensajeErrorCodigoPostalText == mensajeProgramadoCodigoPostal, "No se está mostrando el error por Codigo Postal sin completar"

print("Se está mostrando el error 'Código Postal sin completar' al usuario")

print("No se encontraron errores en esta prueba")

time.sleep(2) 

#cierra el navegador
driver.quit()
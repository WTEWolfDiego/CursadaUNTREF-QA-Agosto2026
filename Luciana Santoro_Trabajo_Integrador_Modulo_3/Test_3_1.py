# Punto 3:
# Automatizar los siguientes casos de prueba. Luego de que sean automatizados, deben ser subidos a un repositorio git, 
# se debe generar el archivo y debe retornar un reporte HTML con los resultados de la ejecución.
# 1) Sitio: https://www.saucedemo.com/
# Caso 1
# ● El usuario se loguea al sitio como usuario standard user
# ● Ordenar los elementos por “price (low to high)”
# ● Verificar que los elementos estén ordenados
# NOTA DE CLASE: tener en cuenta los popups y otras ventanas emergentes

#importa librerías
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import re

###configuracion chrome por alerta de contraseña vulnerable -> Chequear donde va
opciones = webdriver.ChromeOptions()
opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
driver = webdriver.Chrome(options=opciones)


# Nota personal sobre este código y sobre el ejercicio: 
# La indicación de resolver este pop-up hizo que el ejercicio se sintiera como esos tutoriales que pasas de 
# "Hola Mundo" a "Resolvé la hambruna mundial con un for". 
# Busqué en Reddit, StackOverflow, foros de Chromium otras páginas, inclusive tomé el código en Ruby que decía que era
# para configurar la ventana y que lo inhibía desde el vamos y traté de hacerlo pasar a Python.
# Entendí que tenía que hacer, pero no tengo aun las herramientas para hacerlo. 
# Para pedirle una solución que no entiendo a una LLM cualquiera y hacer ping pong entre lenguajes que no utilicé jamás,
# prefiero hacerlo a mi manera y entenderlo en otro navegador. (tampoco logré que funcionara y esquivar todas 
# las respuestas autogeneradas por "AI" para poder hacer el tp lo más pensado posible)
# La respuesta final la dio una compañera que efectivamente uso una LLM. Me parece que este ejercicio
# pronunció la curva de aprendizaje
# en algo donde aun no estamos listos y que terminó sin aportar, porque yo lo iba a terminar haciendo en Firefox


#asigna al webdriver de Firefox a una variable
# driver = webdriver.Firefox() 

# asigna al webdriver de Chrome a una variableb y le solicita que navegue a la página deseada con get
driver.get("https://www.saucedemo.com")

#buena práctica = maximizar la ventana
driver.maximize_window()

# espera que cargue
time.sleep(1) 


#esperar a que cargue todo? Entre paréntesis van los segundos de espera. 
# TODO: Cuánto es mucho? Cuánto es poco? Cual es la demora esperada promedio estándar de una página?
#por lo que entiendo no vale la pena asignarlo a una variable ya que se invoca las veces que sea necesario
time.sleep(1) 

# TODO aparece siempre el de traducir?


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

# # TODO: El formulario de guardar contraseñaAAAA


# aviso de brecha de contraseña -- intento fallido
# driver.switch_to.alert.accept()

# pregunta sobre guardar contraseña -- parecería que la configuración del principio resuelve todos estos pop-ups?
# TODO: chequear borrando cookies antes
# driver.switch_to.alert.dismiss()

#buscar y clickear el dropdown, no tiene ID -> no hace falta clickear

#fallaba porque no le puse el paréntesis al final de click. CAPA. Le estaba asignando el click, no ejecutandolo?
#ordenMenoraMayor = driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
#funcionan los dos pero quería probar By.Class_name

#si ya ponés el select, es necesario abrir el dropdown? parece que no. Al sacar el click() funcionó sin errores
# por qué la variable? -> Reutilización
# por qué el Select() -> Porque lo "envuelve" en la Clase Select y habilita usar sus métodos
ordenMenoraMayor = Select(driver.find_element(By.CLASS_NAME,"product_sort_container")) 

# usando el método de select, elige directamente de las opciones disponibles
ordenMenoraMayor.select_by_visible_text("Price (low to high)")
time.sleep(1) 

#Verificar que estén ordenados... cómo?
# OK, resulta y acontece que cuando se cambia el dropdown, en el DOM se cambia la active_option. También están
# los precios. Según la LLM de turno, realizar el assert sobre active_option es más "débil", ya que sólo verifica
# la aplicación del filtro, no que efectivamente los valores estén ordenados (de < a > en este caso)

# como importar el dom y ordenarlo? Acá necesité ayuda en el COMO
# asignar el contenido de find_element permite manipularlo. Tener en cuenta que atributos se repiten
# permite utilizar find_elementSSS
listaPreciosDom = driver.find_elements(By.CLASS_NAME,"inventory_item_price")

print(f"Esta es la lista de precios obtenida del DOM {listaPreciosDom}")

listaPreciosString = []

#método para obtener sólo el texto del precio, sin la info HTML?
def obtenerTextoPrecio(listaPreciosDom):
    for precio in listaPreciosDom:
        listaPreciosString.append(precio.text)
    return listaPreciosString

listaPreciosString = obtenerTextoPrecio(listaPreciosDom)
print(f"Esta es la lista de precios convertida a String {listaPreciosString}")

listaPreciosSinPeso = []

# método para remover el signo $ - hardcodeado. Hay opciones con REGEX.
def removerCaracteres(listaPreciosString):
    for precio in listaPreciosString:
        precio = precio.strip("$")    
        listaPreciosSinPeso.append(precio)
    return listaPreciosSinPeso

# no logré hacerte andar https://www.geeksforgeeks.org/python/convert-string-to-float-in-python/
# matches = re.findall(r'-?\d*\.?\d+', listaPreciosString)
# listaPreciosInt = [float(x) if '.' in x else int(x) for x in matches]
# print(listaPreciosInt)

listaPreciosSinPeso = removerCaracteres(listaPreciosString)
print(f"Esta es la lista de precios en formato String sin el signo peso {listaPreciosSinPeso}")

listaPreciosInt = []

# método para pasar la lista de String a Float y poder compararla como números
def pasarListaInt(listaPreciosSinPeso):
     for p in listaPreciosSinPeso:
            listaPreciosInt.append(float(p))
     return listaPreciosInt

listaPreciosInt = pasarListaInt(listaPreciosSinPeso)
print(f"Esta es la lista de precios convertida a interger {listaPreciosInt}")

time.sleep(1) 

#Código de LLM. No me gusta, pero no sé usar Assert combinado con una comparación de menor a mayor. Vuelvo a
#comentar: no me sirve una consigna que no puedo cumplir si me faltan las herramientas para hacerlo.
#Entiendo QUE, pero no puedo adivinar el como, ya que las instrucciones deben ser precisas. 
# def verificar_orden(listaPreciosInt):
#   # all() verifica que la condición se cumpla para todos los elementos adyacentes
#   assert all(
#       listaPreciosInt[i] <= listaPreciosInt[i + 1] for i in range(len(listaPreciosInt) - 1)
#   ), 'La lista no está ordenada de menor a mayor'
#   return 'Lista ordenada correctamente'

# Este código es mio pero la idea no. Realmente no se me ocurrió como resoverlo.
# código para ordenar la lista y asignarla a una lista nueva sin modificar la vieja. 
# entonces la comparación no hace falta hardcodearla, se compararía con "la lista que debería ser" vs "la que es"
listaOrdenada = []

#sort ordena la original y sorted una nueva?
listaOrdenada = sorted(listaPreciosInt)
print(f"Esta es la lista de precios ordenada usada para el assert {listaOrdenada}")

#comparación del resultado de ambas listas
assert listaPreciosInt == listaOrdenada, "Los resultados no están ordenados de menor a mayor"
print("Se verificó que los productos se ordenan de menor a mayor")

print("No se detectaron errores en esta prueba.")

#cierra el navegador
driver.quit()


#TODO: investigar
# Assert:
# Assert is used to perform a mandatory check within the test script.
# When an assertion fails, the test is immediately stopped, and the failure is reported.
# It's best suited for critical checks where a failure means the rest of the test is not relevant and should not continue.
# Verify:
# Verify is used when the condition being tested is not crucial for the continuation of the test.
# If a verification fails, the test continues, and all verification failures are collected for reporting at the end.
# This is helpful when you want to gather multiple errors before halting the test.







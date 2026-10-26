from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select  
#CASO 1 ----------------------------------------------------------------------------------------------------------
def test_sauce_Lohi():
###Sacar el alerta de contraseña
    opciones = webdriver.ChromeOptions()
    opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
    driver = webdriver.Chrome(options=opciones)
    driver.get("https://www.saucedemo.com/")
####Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    elemento = driver.find_element(By.CLASS_NAME, "product_sort_container")
    desplegable = Select(elemento)
    desplegable.select_by_value("lohi") #Lohi --> low to high 
    time.sleep(3)
    precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    #devuelve los precios de menor a mayor pero en formato texto
    anterior = 0
    for precio in precios:
        actual = float(precio.text.replace("$", ""))#pasa de texto a float y elimina el signo
        print(actual)

        assert actual >= anterior   #verifica que el precio actual sea mayor o igual al anterior---> contemplando que lo acomodamos de low to high
        anterior = actual

    print(driver.current_url)
    driver.quit()
    
    #CASO 2 ---------------------------------------------------------------------------------------------------------- 
def test_sauce_checkout():
        ###Sacar el alerta de contraseña
        opciones = webdriver.ChromeOptions()
        opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
        driver = webdriver.Chrome(options=opciones)     
        driver.implicitly_wait(5) # Agrego la demora de hasta 5 segundos porque tuve test inestable
        driver.get("https://www.saucedemo.com/")
        ###Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    
        botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
           
        for boton in botones:
            boton.click()
        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        productos = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos) == 6 #Verifico que haya 6 productos en el carrito
                
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Julieta")
        driver.find_element(By.ID, "continue").click()
        mensaje = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert mensaje == "Error: Last Name is required"
        driver.find_element(By.ID, "last-name").send_keys("Forciniti")
        driver.find_element(By.ID, "continue").click()
        mensaje = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert mensaje == "Error: Postal Code is required"
   
        
        
    
        driver.quit()
        
    #CASO 3 ---------------------------------------------------------------------------------------------------------- 
def test_sauce_compra():
                ###Sacar el alerta de contraseña
        opciones = webdriver.ChromeOptions()
        opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
        driver = webdriver.Chrome(options=opciones)     
        driver.implicitly_wait(5) # Agrego la demora de hasta 5 segundos porque tuve test inestable
        driver.get("https://www.saucedemo.com/")
        ###Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        #Agregar y quitar un producto
        botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        botones[0].click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.CLASS_NAME, "cart_button").click()
        productos = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos) == 0 #verifico que el carrito esté vacío
        #Continuar comprando
        driver.find_element(By.ID, "continue-shopping").click()
        botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for boton in botones[:2]:   #agrega los primeros dos productos
            boton.click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        productos = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos) == 2 #verifico que se hayan agregado los dos productos al carrito
        #Proceso de checkout
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Julieta")
        driver.find_element(By.ID, "last-name").send_keys("Forciniti")
        driver.find_element(By.ID, "postal-code").send_keys("1828")
        driver.find_element(By.ID, "continue").click()
        # Finalizar la compra
        driver.find_element(By.ID, "finish").click()
        mensaje = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert mensaje == "Thank you for your order!"
        
        
        
        driver.quit()
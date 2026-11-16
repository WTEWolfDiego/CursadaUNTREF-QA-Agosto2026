from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pytest

opciones = webdriver.ChromeOptions()

opciones.add_argument("--disable-features=TranslateUI,PasswordLeakDetection,PasswordManager")

#para el popup
opciones.add_experimental_option(
    "prefs",
    {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=opciones)

driver.get("https://www.saucedemo.com/")

#logueo
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
print("Login exitoso")

#incorporar todos los articulos al carrito

driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

time.sleep(2)
print()
print("Se cargaron todos los articulos al carrito")

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(5)

#Verificar que esten todos los articulos estén en el carrito

art1=driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div").text 
assert 'Sauce Labs Onesie' in art1
art2=driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text 
assert 'Sauce Labs Bike Light' in art2
art3=driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").text 
assert 'Sauce Labs Bolt T-Shirt' in art3
art4=driver.find_element(By.XPATH, "//*[@id='item_3_title_link']/div").text 
assert 'Test.allTheThings() T-Shirt (Red)' in art4
art5=driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text 
assert 'Sauce Labs Backpack' in art5
art6=driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").text 
assert 'Sauce Labs Fleece Jacket' in art6
print()
print("Estan todos los articulos en el carrito")
print()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test='checkout']")))
time.sleep(10)
driver.find_element(By.XPATH,"//button[@data-test='checkout']").click()

time.sleep(5)


driver.find_element(By.ID, "first-name").send_keys("Peter")
   
driver.find_element(By.ID, "continue").click()




mensaje_error1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))).text 
assert 'Error: Last Name is required' in mensaje_error1

print()
print("Last Name es Requerido")
print()

driver.find_element(By.ID,"last-name").send_keys("PruebaQA")
driver.find_element(By.ID,"continue").click()

mensaje_error2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))).text
assert 'Error: Postal Code is required' in mensaje_error2

print()
print("Postal Code es Requerido")
print("Caso 2 Terminado")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

opciones = webdriver.ChromeOptions()
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

#Ordenar por precio
elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "product_sort_container")
    )
)

ordenamiento = Select(elemento)
ordenamiento.select_by_value("lohi")
print("Se ordenaron los precios")
time.sleep(5)

#

# QA Automation Challenge - UNTREF
 
Trabajo práctico de automatización de pruebas utilizando Python, Selenium, Pytest y Requests.
 
## Contenido
 
### Punto 1 - Número primo
 
Programa que recibe un número y determina si es primo o no.
 
Archivo:
 
`Ejercicios/punto1_primos.py`
 
### Punto 2 - Ecuación cuadrática
 
Programa que recibe los valores `a`, `b` y `c` y calcula las raíces de una ecuación cuadrática.
 
Archivo:
 
`Ejercicios/punto2_cuadratica.py`
 
### Punto 3 - Automatización
 
Se automatizaron casos de prueba sobre SauceDemo y PokeAPI.
 
#### SauceDemo
 
Se utilizó Selenium WebDriver.
 
Casos automatizados:
 
1. Login y ordenamiento de productos por precio de menor a mayor.
2. Agregado de todos los productos al carrito y validación de campos obligatorios durante el checkout.
3. Agregado y eliminación de productos, checkout completo y validación de compra realizada.
 
Archivo:
 
`Tests/test_saucedemo.py`
 
#### PokeAPI
 
Se utilizó Requests para realizar las peticiones HTTP y Pytest para las validaciones.
 
Casos automatizados:
 
1. Validación de Berry 1.
2. Validación y comparación de Berry 2.
3. Validación de experiencia base y tipo de Pikachu.
 
Archivo:
 
`Tests/test_pokeapi.py`
 
## Instalación
 
Instalar las dependencias:
 
```bash
pip install -r requirements.txt
# Trabajo Integrador - QA Automation

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas de interfaz de usuario (UI) y pruebas de API REST desarrolladas en Python.

Se utilizan las siguientes herramientas:

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest-HTML
- Visual Studio Code

El objetivo es automatizar diferentes escenarios funcionales, validar los resultados esperados y generar reportes HTML de las ejecuciones.

## Aplicaciones utilizadas

### SauceDemo - Pruebas UI

Sitio web: https://www.saucedemo.com/

Se utiliza Selenium WebDriver para automatizar el navegador Google Chrome y verificar funcionalidades del sitio.

### PokeAPI - Pruebas API

API REST: https://pokeapi.co/api/v2/

Se utiliza la librería Requests para realizar solicitudes HTTP GET y verificar los datos devueltos por la API.

## Estructura del proyecto

```text
qa_automation_integrador/
│
├── tests/
│   ├── test_saucedemo.py
│   └── test_pokeapi.py
│
├── reports/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

## Requisitos previos

Para ejecutar las pruebas es necesario tener instalado:

- Python 3
- Visual Studio Code
- Extensión Python de Microsoft para VS Code
- Google Chrome para las pruebas de SauceDemo
- Conexión a Internet

## Instalación

### 1. Abrir el proyecto

Abrir Visual Studio Code y seleccionar:

File > Open Folder

Elegir la carpeta `qa_automation_integrador`.

### 2. Crear un entorno virtual

Desde la terminal integrada de VS Code:

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows con PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, se puede utilizar directamente el intérprete:

```powershell
.\.venv\Scripts\python.exe
```

### 4. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` debe incluir:

```text
pytest
pytest-html
selenium
requests
```

## Casos de prueba automatizados

### SauceDemo - Pruebas UI

**Caso 1: Ordenamiento de productos**

1. Iniciar sesión con un usuario válido.
2. Acceder al listado de productos.
3. Ordenar los productos por precio ascendente.
4. Verificar que los precios estén ordenados de menor a mayor.

**Caso 2: Validaciones del checkout**

1. Iniciar sesión.
2. Agregar todos los productos al carrito.
3. Verificar los productos agregados.
4. Iniciar el checkout.
5. Completar solamente el nombre.
6. Verificar el mensaje `Error: Last Name is required`.
7. Completar el apellido.
8. Verificar el mensaje `Error: Postal Code is required`.

**Caso 3: Compra completa**

1. Iniciar sesión.
2. Agregar un producto al carrito.
3. Verificar que se agregó correctamente.
4. Eliminar el producto.
5. Verificar que el carrito quedó vacío.
6. Regresar al listado de productos.
7. Agregar dos productos.
8. Iniciar y completar el checkout.
9. Verificar el mensaje `Thank you for your order!`.

### PokeAPI - Pruebas API REST

**Caso 1: Validar Berry 1**

Endpoint:

```http
GET https://pokeapi.co/api/v2/berry/1
```

Validaciones:

- Código HTTP 200.
- `size` igual a 20.
- `soil_dryness` igual a 15.
- `firmness.name` igual a `soft`.

**Caso 2: Validar Berry 2**

Endpoint:

```http
GET https://pokeapi.co/api/v2/berry/2
```

Validaciones:

- Código HTTP 200.
- `firmness.name` igual a `super-hard`.
- El tamaño debe ser mayor al de Berry 1.
- `soil_dryness` debe coincidir con Berry 1.

**Caso 3: Validar Pikachu**

Endpoint:

```http
GET https://pokeapi.co/api/v2/pokemon/pikachu/
```

Validaciones:

- Código HTTP 200.
- `base_experience` mayor que 10 y menor que 1000.
- El Pokémon debe tener el tipo `electric`.

## Ejecución de pruebas

Las pruebas de SauceDemo y PokeAPI pueden ejecutarse de forma independiente.

### Ejecutar solamente SauceDemo

```powershell
python -m pytest tests/test_saucedemo.py -v -s
```

### Ejecutar solamente PokeAPI

```powershell
python -m pytest tests/test_pokeapi.py -v -s
```

### Ejecutar todas las pruebas

```powershell
python -m pytest tests/ -v -s
```

## Generación de reportes HTML

Los reportes se generan mediante la librería `pytest-html`.

Antes de ejecutar las pruebas, crear la carpeta `reports` si todavía no existe:

```powershell
mkdir reports
```

### Reporte completo

```powershell
python -m pytest tests/ -v -s --html=reports/reporte.html --self-contained-html
```

### Reporte SauceDemo

```powershell
python -m pytest tests/test_saucedemo.py -v -s --html=reports/reporte_saucedemo.html --self-contained-html
```

### Reporte PokeAPI

```powershell
python -m pytest tests/test_pokeapi.py -v -s --html=reports/reporte_pokeapi.html --self-contained-html
```

### Abrir los reportes en Windows

```powershell
start reports/reporte_saucedemo.html
```

```powershell
start reports/reporte_pokeapi.html
```

## Interpretación de resultados

Pytest utiliza diferentes estados para indicar el resultado de una prueba:

| Estado | Descripción |
|---|---|
| PASSED | La prueba se ejecutó correctamente |
| FAILED | La prueba falló |
| ERROR | Se produjo un error durante la ejecución o preparación |
| SKIPPED | La prueba fue omitida |

Los reportes HTML permiten consultar los resultados de cada caso de prueba.

## Manejo de errores

En las pruebas API se utiliza `try/except` para controlar errores relacionados con las solicitudes HTTP y la interpretación de las respuestas JSON.

En las pruebas UI se utilizan esperas explícitas de Selenium WebDriver para esperar que los elementos estén disponibles antes de interactuar con ellos.

## Comandos útiles de Pytest

Ejecutar pruebas con información detallada:

```powershell
python -m pytest -v
```

Mostrar las instrucciones `print()`:

```powershell
python -m pytest -s
```

Ejecutar una prueba específica:

```powershell
python -m pytest tests/test_pokeapi.py::test_pikachu -v
```

Detener la ejecución después del primer fallo:

```powershell
python -m pytest -x
```

## Conclusión

Este trabajo integrador permite aplicar conceptos de automatización de pruebas utilizando Python y selenium.

Se implementan pruebas funcionales de interfaz de usuario mediante Selenium y pruebas de servicios REST mediante Requests.

Pytest permite organizar, ejecutar y validar los casos de prueba, mientras que Pytest-HTML facilita la generación de reportes independientes para SauceDemo y PokeAPI.
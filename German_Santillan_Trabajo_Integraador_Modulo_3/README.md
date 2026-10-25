# Trabajo Integrador — Módulo 3
## Diplomatura en Control de Calidad de Software

**Universidad:** Universidad Nacional de Tres de Febrero (UNTREF)  
**Alumno:** Germán Santillán  
**Lenguaje:** Python  
**Herramientas:** Selenium WebDriver, Requests, Pytest y pytest-html  

---

## 1. Introducción

El presente proyecto corresponde al Trabajo Integrador del Módulo 3 de la Diplomatura en Control de Calidad de Software de la Universidad Nacional de Tres de Febrero.

El trabajo está dividido en tres puntos que permiten aplicar distintos conceptos de programación y automatización de pruebas utilizando Python.

- **Punto 1:** Validación de números primos.
- **Punto 2:** Cálculo de raíces de una ecuación cuadrática.
- **Punto 3:** Automatización de pruebas web y de servicios REST.

Los primeros dos puntos utilizan estructuras de control, funciones, validaciones y manejo de excepciones. El tercer punto incorpora automatización con Selenium y Requests, programación orientada a objetos, Pytest y reportes HTML.

## 2. Punto 1 — Validación de número primo

### 2.1. Objetivo

Desarrollar un programa que permita ingresar un número entero y determinar si es primo o no.

### 2.2. Implementación

Se desarrolló una función denominada `es_primo(numero)`, que recibe un número entero y determina si es primo.

La función comienza verificando que el número sea mayor o igual a 2, ya que los números primos son enteros mayores que 1 que solamente tienen dos divisores positivos: 1 y ellos mismos.

Posteriormente, utiliza un ciclo `for` para recorrer los posibles divisores desde 2 hasta el número ingresado, sin incluirlo.

Mediante el operador módulo (`%`) se comprueba si existe una división exacta:

- Si el resto de una división es cero, se encontró un divisor y la función retorna `False`.
- Si no se encuentran divisores, la función retorna `True`.

El programa principal incorpora un ciclo `while True` para solicitar el ingreso del número y un bloque `try/except` para controlar errores de conversión.

También se valida que el número ingresado no sea negativo.

### 2.3. Resultado esperado

El programa informa si el número ingresado es primo o no.

Ejemplos:

```text
Ingrese un número entero: 7
El número 7 es primo.
```

```text
Ingrese un número entero: 10
El número 10 no es primo.
```

Si el usuario ingresa un valor no numérico o negativo, el programa informa el error correspondiente y solicita nuevamente un número.

## 3. Punto 2 — Ecuación cuadrática

### 3.1. Objetivo

Desarrollar una función que reciba tres coeficientes (`a`, `b`, `c`) y calcule las raíces reales de una ecuación cuadrática.

La ecuación tiene la siguiente forma:

**ax² + bx + c = 0**

### 3.2. Implementación

Se desarrolló una función denominada `calcular_raices(a, b, c)`.

La función calcula el discriminante mediante la expresión:

```python
discriminante = b ** 2 - 4 * a * c
```

Según el resultado del discriminante, pueden presentarse tres situaciones:

| Discriminante | Resultado |
|---|---|
| Mayor que cero | Dos raíces reales distintas |
| Igual a cero | Una raíz real doble |
| Menor que cero | No existen raíces reales |

Para calcular las raíces se utiliza la fórmula general:

**x = (-b ± √(b² - 4ac)) / (2a)**

Se importa el módulo `math`, perteneciente a la biblioteca estándar de Python, para utilizar `math.sqrt()`.

La función devuelve los resultados mediante tuplas:

- Tupla con dos elementos cuando existen dos raíces reales.
- Tupla con un elemento cuando existe una raíz doble.
- Tupla vacía cuando no existen raíces reales.

El programa principal solicita los coeficientes mediante `input()` y los convierte a valores numéricos utilizando `float()`.

Además, incorpora un ciclo `while True`, manejo de excepciones con `try/except` y una validación para impedir que el coeficiente `a` sea cero, ya que en ese caso la ecuación no sería cuadrática.

### 3.3. Resultados esperados

**Dos raíces reales:**

```text
Ingrese el valor de a: 1
Ingrese el valor de b: -3
Ingrese el valor de c: 2

La primera raíz es: 2.0
La segunda raíz es: 1.0
```

**Una raíz doble:**

```text
Ingrese el valor de a: 1
Ingrese el valor de b: 2
Ingrese el valor de c: 1

La ecuación tiene una raíz doble: -1.0
```

**Sin raíces reales:**

```text
Ingrese el valor de a: 1
Ingrese el valor de b: 0
Ingrese el valor de c: 1

La ecuación no tiene raíces reales.
```

El programa también contempla el ingreso de valores incorrectos y permite solicitar nuevamente los coeficientes.

## 4. Punto 3 — Automatización de pruebas

### 4.1. Objetivo

Automatizar los tres casos de prueba de SauceDemo y los tres casos de PokeAPI indicados en la consigna.

Para ello se utilizan las siguientes herramientas:

| Herramienta | Función |
|---|---|
| Python | Lenguaje de programación |
| Selenium WebDriver | Automatización de la interfaz web |
| Requests | Solicitudes HTTP a servicios REST |
| Pytest | Organización y ejecución de las pruebas |
| pytest-html | Generación de reportes HTML |
| Google Chrome | Navegador utilizado en las pruebas web |

El proyecto está organizado para permitir la ejecución conjunta o individual de los casos de prueba.

### 4.2. Cobertura de pruebas

| ID | Plataforma | Descripción |
|---|---|---|
| UI-001 | SauceDemo | Login y ordenamiento ascendente de productos por precio |
| UI-002 | SauceDemo | Agregar todos los productos y validar errores de apellido y código postal |
| UI-003 | SauceDemo | Quitar un producto, agregar dos y finalizar la compra |
| API-001 | PokeAPI | GET `berry/1`: validar tamaño, sequedad del suelo y firmeza |
| API-002 | PokeAPI | GET `berry/2`: validar firmeza y comparar datos con `berry/1` |
| API-003 | PokeAPI | GET `pokemon/pikachu/`: validar experiencia base y tipo eléctrico |

### 4.3. Arquitectura — Page Object Model

Para la automatización web se utiliza **Page Object Model (POM)**, un patrón de diseño que permite representar las pantallas de una aplicación mediante clases.

Cada clase agrupa los localizadores y métodos necesarios para interactuar con una pantalla específica.

Se utiliza una clase `BasePage` para centralizar operaciones comunes, como esperas explícitas y acciones sobre elementos.

Las clases correspondientes a las diferentes pantallas heredan estas funcionalidades, lo que permite reutilizar código y reducir duplicaciones.

Las principales ventajas de esta organización son:

- Separación entre las interacciones web y las validaciones de los tests.
- Reutilización de métodos.
- Mayor legibilidad del código.
- Mantenimiento centralizado de los localizadores.
- Menor duplicación entre casos de prueba.

Los casos API utilizan una clase cliente reutilizable para centralizar las solicitudes HTTP a PokeAPI.

### 4.4. Independencia de las pruebas

Los casos web utilizan una fixture de Pytest para crear y cerrar una instancia de Google Chrome por cada prueba.

Esto evita que el estado del carrito o la sesión de un test afecte a los siguientes.

En los casos API, la segunda prueba consulta tanto `berry/1` como `berry/2`, para poder realizar las comparaciones sin depender de una ejecución anterior.

## 5. Estructura del proyecto

La siguiente estructura representa la organización de los tres puntos. Los nombres de los scripts de los Puntos 1 y 2 deben ajustarse a los archivos reales entregados.

```text
Trabajo_Integrador_Modulo_3/
│
├── punto_1/
│   └── punto_1.py
│
├── punto_2/
│   └── punto_2.py
│
├── punto_3/
│   ├── api/
│   │   ├── __init__.py
│   │   └── pokeapi_client.py
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   │
│   ├── tests/
│   │   ├── test_pokeapi.py
│   │   └── test_saucedemo.py
│   │
│   ├── reports/
│   │
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

**Descripción de los principales componentes:**

| Componente | Responsabilidad |
|---|---|
| `punto_1/` | Programa de validación de números primos |
| `punto_2/` | Programa para calcular raíces cuadráticas |
| `pages/` | Clases y métodos para interactuar con SauceDemo |
| `api/` | Cliente reutilizable de PokeAPI |
| `tests/` | Casos automatizados con Pytest |
| `conftest.py` | Configuración de fixtures y del navegador |
| `pytest.ini` | Configuración y marcas de Pytest |
| `requirements.txt` | Dependencias externas del proyecto |
| `reports/` | Reportes HTML generados por Pytest |
| `.gitignore` | Archivos y carpetas excluidos del repositorio |

## 6. Instalación y configuración en Windows

### 6.1. Requisitos

Se requiere:

- Windows 10 u 11.
- Python 3.10 o superior.
- Google Chrome instalado.
- Conexión a Internet para instalar dependencias y ejecutar las pruebas.
- PowerShell o Símbolo del sistema (CMD).
- Git, si se desea publicar el proyecto en GitHub.

Enlaces oficiales:

- Python: https://www.python.org/downloads/windows/
- Google Chrome: https://www.google.com/chrome/
- Git: https://git-scm.com/downloads/win

Durante la instalación de Python, habilitar la opción para agregar Python al PATH si el instalador la ofrece.

### 6.2. Verificar Python

Abrir PowerShell y ejecutar:

```powershell
py --version
```

También se puede verificar con:

```powershell
python --version
```

Debe mostrarse la versión de Python instalada.

### 6.3. Ubicarse en la carpeta del proyecto

Una vez descargado o descomprimido el trabajo, abrir PowerShell y acceder a la carpeta principal.

Ejemplo:

```powershell
cd "C:\Users\Usuario\Downloads\Trabajo_Integrador_Modulo_3"
```

La ruta debe adaptarse a la ubicación real del proyecto.

### 6.4. Crear el entorno virtual

Ejecutar:

```powershell
py -3 -m venv .venv
```

Esto crea un entorno virtual de Python dentro de la carpeta `.venv`.

### 6.5. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando esté activado, debería aparecer el prefijo `(.venv)` en la terminal.


**Alternativa para CMD:**

```cmd
.venv\Scripts\activate.bat
```

### 6.7. Instalar las dependencias

Desde la carpeta principal del proyecto:

```powershell
python -m pip install -r .\punto_3\requirements.txt
```

Este comando instala las dependencias declaradas para las pruebas automatizadas.

Los Puntos 1 y 2 solamente utilizan funcionalidades incluidas en la biblioteca estándar de Python.


## 7. Ejecución de los ejercicios

### 7.1. Ejecutar Punto 1

Desde la carpeta principal:

```powershell
python .\punto_1\punto_1.py
```

El programa solicitará un número entero y mostrará si es primo o no.

### 7.2. Ejecutar Punto 2

```powershell
python .\punto_2\punto_2.py
```

El programa solicitará los coeficientes `a`, `b` y `c`, y mostrará las raíces reales correspondientes.

### 7.3. Preparar la ejecución del Punto 3

Ingresar a la carpeta del Punto 3:

```powershell
cd .\punto_3
```

Los siguientes comandos deben ejecutarse desde esta carpeta, ya que allí se encuentra el archivo `pytest.ini`.

Crear la carpeta de reportes si no existe:

```powershell
New-Item -ItemType Directory -Force .\reports | Out-Null
```

### 7.5. Ejecutar todos los casos

```powershell
python -m pytest
```

La configuración `addopts = -v` de `pytest.ini` permite mostrar información detallada de los casos durante la ejecución.

### 7.6. Ejecutar solamente las pruebas web

```powershell
python -m pytest -m ui
```

Este comando selecciona los tres casos automatizados de SauceDemo.

### 7.7. Ejecutar solamente las pruebas API

```powershell
python -m pytest -m api
```

Este comando selecciona los tres casos de PokeAPI.

### 7.8. Ejecutar casos mediante marcas combinadas

Pytest permite filtrar mediante expresiones lógicas, siempre que las marcas se encuentren registradas y aplicadas a los tests.

Por ejemplo, si se incorporaron las marcas `caso1`, `caso2` y `caso3`:

```powershell
python -m pytest -m "ui and caso1"
```

Ejecuta solamente el primer caso web.

```powershell
python -m pytest -m "api and caso2"
```

Ejecuta solamente el segundo caso API.

Para consultar las marcas registradas:

```powershell
python -m pytest --markers
```

## 8. Generación de reportes HTML

Los reportes HTML permiten visualizar los resultados reales de las ejecuciones, incluyendo los casos aprobados, fallidos y sus respectivos detalles.

### 8.1. Ejecutar toda la suite y generar el reporte

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

### 8.2. Generar el reporte de las pruebas web

```powershell
python -m pytest -m ui --html=reports/report_ui.html --self-contained-html
```

### 8.3. Generar el reporte de las pruebas API

```powershell
python -m pytest -m api --html=reports/report_api.html --self-contained-html
```

### 8.4. Abrir el reporte

Para abrir el reporte completo en el navegador predeterminado:

```powershell
Start-Process .\reports\report.html
```

## 9. Ejecución de Selenium en modo headless

Las pruebas web pueden ejecutarse sin mostrar la ventana de Chrome.

En PowerShell:

```powershell
$env:HEADLESS = "1"
python -m pytest -m ui --html=reports/report_ui.html --self-contained-html
```

Para volver a la ejecución visible:

```powershell
$env:HEADLESS = "0"
```

Luego ejecutar nuevamente:

```powershell
python -m pytest -m ui
```

El modo headless permite utilizar el navegador sin interfaz gráfica, por ejemplo, durante ejecuciones automatizadas en un pipeline.

La configuración debe estar contemplada en `conftest.py` para que la variable `HEADLESS` tenga efecto.

## 10. Consideraciones técnicas

- Las pruebas UI utilizan las credenciales públicas de demostración de SauceDemo: `standard_user` y `secret_sauce`.
- Cada caso web crea su propia instancia de Chrome mediante una fixture de Pytest, para mantener el aislamiento entre pruebas.
- La automatización utiliza esperas explícitas para aguardar la disponibilidad de los elementos antes de interactuar.
- Las validaciones se realizan mediante instrucciones `assert`.
- Para localizar los elementos se utilizan estrategias como ID, clase y selectores CSS.
- En las pruebas API se verifica el código HTTP y el contenido JSON devuelto por los servicios.
- Las solicitudes a PokeAPI utilizan un tiempo máximo de espera para evitar solicitudes indefinidas.
- Selenium Manager gestiona la obtención del controlador de Chrome compatible cuando es necesario.
- SauceDemo y PokeAPI son servicios externos. Los cambios en sus interfaces, respuestas o disponibilidad pueden afectar los resultados de las pruebas.

**Criterio de validación:** una prueba se considera aprobada solamente cuando sus verificaciones se cumplen. No se modifican los resultados esperados para forzar una ejecución exitosa.


## 12. Solución de errores frecuentes

### Python no se reconoce como comando

Verificar que Python esté instalado correctamente y disponible en PATH.

Probar:

```powershell
py --version
```

Si es necesario, reinstalar Python desde su sitio oficial.

### Error al activar el entorno virtual

Si PowerShell impide ejecutar `Activate.ps1`, utilizar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### ModuleNotFoundError: selenium, pytest o requests

Verificar que el entorno virtual esté activado y reinstalar las dependencias:

```powershell
python -m pip install -r .\punto_3\requirements.txt
```

Este comando corresponde a la ejecución desde la carpeta principal del trabajo.

### No module named pytest_html

Instalar la dependencia correspondiente:

```powershell
python -m pip install pytest-html
```

### Unable to obtain driver for Chrome

Verificar:

- Google Chrome instalado.
- Conexión a Internet.
- Compatibilidad de la versión de Selenium.
- Permisos necesarios para descargar o ejecutar el controlador.

### TimeoutException en SauceDemo

Puede producirse cuando un elemento no aparece o no está disponible dentro del tiempo máximo de espera.

Verificar el estado de SauceDemo, el inicio de sesión y los localizadores utilizados.

### ConnectionError o ReadTimeout en PokeAPI

Verificar la conexión a Internet y la disponibilidad del servicio.

Una respuesta inexistente o un error de conexión no debe considerarse una prueba aprobada.

### Pytest no encuentra los tests

Verificar que:

- Los archivos tengan nombres que comiencen con `test_`.
- Los casos estén definidos mediante funciones reconocidas por Pytest.
- Se estén ejecutando los comandos desde la carpeta `punto_3`.
- El archivo `pytest.ini` tenga la configuración correcta.

---

**Universidad Nacional de Tres de Febrero — UNTREF**  
**Diplomatura en Control de Calidad de Software**  
**Trabajo Integrador — Módulo 3**  
**Alumno: Germán Santillán**
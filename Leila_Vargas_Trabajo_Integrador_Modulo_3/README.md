# TP Integrador - QA Automation (Módulo 3)

**Alumna:** Leila Vargas
**Curso:** Diplomatura QA Automation - Módulo 3

Este proyecto tiene dos ejercicios de Python y pruebas automatizadas sobre una página web y una API.

## Qué incluye

**Punto 1 - Número primo** (`ejercicios/numero_primo.py`)
Pide números y dice si cada uno es primo o no. Se repite hasta que se escribe `salir`.

**Punto 2 - Ecuación cuadrática** (`ejercicios/ecuacion_cuadratica.py`)
Pide los valores a, b y c y calcula las raíces de la ecuación. Se repite hasta que se escribe `salir`.

**Punto 3 - Pruebas automatizadas**

Saucedemo (página web, con Selenium) - `pruebas/ui/test_saucedemo.py`

| Caso | Qué prueba |
|---|---|
| 1 | Ordenar los productos por precio de menor a mayor y verificar el orden |
| 2 | Agregar todos los productos al carrito y validar los errores del checkout |
| 3 | Quitar un producto, agregar dos y completar la compra |

PokeAPI (API, con requests) - `pruebas/api/test_pokeapi.py`

| Caso | Qué prueba |
|---|---|
| 1 | Datos de `berry/1`: size, soil_dryness y firmness |
| 2 | Comparar `berry/2` con `berry/1` |
| 3 | Experiencia base y tipo de `pikachu` |

## Carpetas

| Carpeta | Contenido |
|---|---|
| `ejercicios/` | Puntos 1 y 2 |
| `paginas/` | Una clase por cada pantalla de Saucedemo |
| `pruebas/` | Los casos de prueba de la web y de la API |
| `resultados/` | El reporte HTML con los resultados |

## Cómo usarlo

Se necesita tener instalado Python, Git y Google Chrome.

**1. Preparar el proyecto** (solo la primera vez)

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

**2. Correr las pruebas**

    pytest

El reporte queda en `resultados/reporte_ejecucion.html`.

**3. Probar los ejercicios**

    python ejercicios\numero_primo.py
    python ejercicios\ecuacion_cuadratica.py

## Herramientas usadas

Python, Selenium, requests, pytest, pytest-html y Git.
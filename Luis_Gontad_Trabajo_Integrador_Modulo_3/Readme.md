# Trabajo Integrador - Diplomatura en Control de Calidad de Software (UNTREF)
**Autor:** Luis Gontad  
**Tecnologías:** Python 3, Selenium WebDriver, Pytest, Requests, Pytest-HTML  


Estructura

Integrador/
├── Punto1/                 # Números primos
│   └── 1.py
├── Punto2/                 # Ecuación cuadrática
│   └── 2.py
├── punto3/
│   ├── api/
│   │   └── pokeapi.py      # Funciones auxiliares / API client
│   ├── pages/              # Page Object Model de SauceDemo
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── Reports/            # Reporte HTML generado
│   │   └── report.html
│   ├── Test/               # Casos de prueba
│   │   ├── test_saucedemo.py
│   │   └── test_pokeapi.py
│   ├── conftest.py         # Fixtures globales
│   ├── pytest.ini          # Configuración y generación de reporte
│   └── requeriments.txt
├── .gitignore
└── Readme.md


Instalación

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / Mac

pip install -r punto3/requeriments.txt


Nota: Se requiere Google Chrome instalado. Selenium gestiona el driver automáticamente.

Ejecución

Pruebas Automatizadas (Pytest)

Para ejecutar las pruebas y generar el reporte HTML, situarse en el directorio punto3:

cd punto3

pytest                            # Todos los tests (SauceDemo + PokeAPI)
pytest Test/test_saucedemo.py     # Solo pruebas UI de SauceDemo
pytest Test/test_pokeapi.py       # Solo pruebas de PokeAPI


El reporte ejecutable se genera en punto3/Reports/report.html.

Programas Interactivos

Para ejecutar los scripts de consola de los Puntos 1 y 2 desde la raíz:

python Punto1/1.py
python Punto2/2.py

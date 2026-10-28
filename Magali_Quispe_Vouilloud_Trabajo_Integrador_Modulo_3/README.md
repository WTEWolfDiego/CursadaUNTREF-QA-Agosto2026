# Trabajo Integrador - Módulo 3

Automatización en Python con Pytest, Selenium y Requests.

## Estructura

```
trabajo-integrador/
├── punto1/                 # Número primo
│   ├── primo.py
│   └── test_primo.py
├── punto2/                 # Ecuación cuadrática
│   ├── cuadratica.py
│   └── test_cuadratica.py
├── punto3/
│   ├── conftest.py         # Fixtures: driver de Chrome y URL de la API
│   ├── pages/              # Page Object Model de saucedemo
│   └── tests/
│       ├── ui/test_saucedemo.py
│       └── api/test_pokeapi.py
├── pytest.ini              # Configuración y reporte HTML
└── requirements.txt
```

## Instalación

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / Mac
pip install -r requirements.txt
```

Se necesita Google Chrome instalado. Selenium descarga el driver solo.

## Ejecución

```bash
pytest                       # todos los tests
pytest punto3/tests/ui       # solo saucedemo
pytest punto3/tests/api      # solo PokeAPI
pytest --headless            # Chrome sin ventana
```

El reporte se genera en `reports/reporte.html`.

Para correr los programas en modo interactivo:

```bash
python punto1/primo.py
python punto2/cuadratica.py
```

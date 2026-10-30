# TP Integrador - Módulo 3

Alumno: Juan Ignacio Poropat

## Contenido
- `ejercicio1_primos.py`: programa que indica si un número es primo.
- `ejercicio2_cuadratica.py`: función que calcula las raíces de una ecuación cuadrática.
- `Ejercicio 3 - SauceDemo/`: 3 casos automatizados con Selenium y pytest.
- `Ejercicio 3 - PokeApi/`: 3 casos de API con requests y pytest.
- `reports/`: reportes HTML de la ejecución.

## Requisitos
Python 3 y Google Chrome instalado.

## Instalación
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución
Los comandos se ejecutan parado dentro de esta carpeta.

```powershell
python ejercicio1_primos.py
python ejercicio2_cuadratica.py
pytest "Ejercicio 3 - SauceDemo" -v -s --html=reports/reporte_saucedemo.html --self-contained-html
pytest "Ejercicio 3 - PokeApi" -v -s --html=reports/reporte_pokeapi.html --self-contained-html
```

## Reportes
- `reports/reporte_saucedemo.html`
- `reports/reporte_pokeapi.html`


## Estructura del proyecto

```
Juan_Poropat_Trabajo_Integrador_Modulo_3/
├── Ejercicio 3 - PokeApi/
├── Ejercicio 3 - SauceDemo/
├── reports/
├── ejercicio1_primos.py
├── ejercicio2_cuadratica.py
├── requirements.txt
├── README.md
└── .gitignore
```

# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 2
# Escribir una función que, dado el ingreso de 3 variables (a, b, c),
# retorne las raíces resultantes de una ecuación cuadrática.
# Alumno: Germán Santillán.

# Importamos el módulo math, que pertenece a la biblioteca estándar de Python.
# Lo utilizaremos para calcular la raíz cuadrada del discriminante.
import math


# Definimos la función que calcula las raíces de una ecuación cuadrática.
# La función recibe tres parámetros: a, b y c.
def calcular_raices(a, b, c):

    # Calculamos el discriminante de la ecuación utilizando la fórmula:
    # discriminante = b² - 4ac.
    # El discriminante determina la cantidad de raíces reales.
    discriminante = b ** 2 - 4 * a * c

    # Si el discriminante es negativo, no existen raíces reales.
    # Retornamos un valor vacío para indicar que no hay resultados reales.
    if discriminante < 0:
        return ()

    # Si el discriminante es igual a cero, existe una única raíz real doble.
    # Aplicamos la fórmula: x = -b / (2a).
    elif discriminante == 0:
        raiz = -b / (2 * a)

        # Retornamos una tupla con un único elemento.
        return (raiz,)

    # Si el discriminante es positivo, existen dos raíces reales distintas.
    else:

        # Calculamos la raíz cuadrada del discriminante con math.sqrt().
        raiz_cuadrada = math.sqrt(discriminante)

        # Calculamos la primera raíz utilizando la suma de la fórmula general.
        raiz_1 = (-b + raiz_cuadrada) / (2 * a)

        # Calculamos la segunda raíz utilizando la resta de la fórmula general.
        raiz_2 = (-b - raiz_cuadrada) / (2 * a)

        # Retornamos ambas raíces dentro de una tupla.
        return (raiz_1, raiz_2)


# Comienzo del programa principal, solicitando los tres coeficientes.
# Mientras el usuario no ingrese valores válidos, se solicitarán nuevamente.
while True:

    # Encapsulamos el ingreso de datos en un bloque try-except
    # para manejar posibles errores de conversión.
    try:

        # Solicitamos al usuario el valor del coeficiente a.
        a = input("Ingrese el valor de a: ")

        # Convertimos el valor ingresado a un número decimal.
        a = float(a)

        # Solicitamos al usuario el valor del coeficiente b.
        b = input("Ingrese el valor de b: ")

        # Convertimos el valor ingresado a un número decimal.
        b = float(b)

        # Solicitamos al usuario el valor del coeficiente c.
        c = input("Ingrese el valor de c: ")

        # Convertimos el valor ingresado a un número decimal.
        c = float(c)

        # Verificamos que el coeficiente a sea distinto de cero.
        # Si a es cero, la ecuación deja de ser cuadrática.
        # Además, la fórmula general produciría una división por cero.
        if a == 0:
            print("El valor de 'a' debe ser distinto de cero.")
            continue

        # Llamamos a la función calcular_raices y almacenamos el resultado.
        raices = calcular_raices(a, b, c)

        # Verificamos si la función retornó dos raíces reales.
        # Utilizamos len() para conocer la cantidad de elementos de la tupla.
        if len(raices) == 2:

            # Mostramos las dos raíces calculadas.
            print(f"La primera raíz es: {raices[0]}")
            print(f"La segunda raíz es: {raices[1]}")

        # Si la tupla contiene un único elemento, existe una raíz doble.
        elif len(raices) == 1:

            # Mostramos la única raíz real encontrada.
            print(f"La ecuación tiene una raíz doble: {raices[0]}")

        # Si la tupla está vacía, no existen raíces reales.
        else:

            # Informamos al usuario que no hay soluciones reales.
            print("La ecuación no tiene raíces reales.")

        # Si los valores ingresados son válidos y se procesó la ecuación,
        # rompemos el ciclo para finalizar el programa.
        break

    # En caso de ingresar un valor no numérico, capturamos ValueError.
    # Informamos el error y solicitamos nuevamente los coeficientes.
    except ValueError:
        print("El valor ingresado no es un número válido. Por favor, ingrese todos los numeos de a, b y c nuevamente.")
        continue

# ==========================================================
# PROGRAMA: CÁLCULO DE RAÍCES DE UNA ECUACIÓN CUADRÁTICA
#
# Una ecuación cuadrática tiene la forma:
#
# a*x² + b*x + c = 0
#
# El programa permite:
# 1. Ingresar los coeficientes a, b y c.
# 2. Calcular el discriminante.
# 3. Determinar si existen raíces reales.
# 4. Mostrar las raíces obtenidas.
# 5. Validar entradas incorrectas.
# 6. Repetir el cálculo mediante un menú.
# ==========================================================


# Importamos la librería math.
# La utilizaremos para calcular raíces cuadradas
# mediante la función math.sqrt().
import math


# ==========================================================
# FUNCIÓN: CALCULAR LAS RAÍCES DE LA ECUACIÓN
# ==========================================================

# Definimos una función que recibe tres parámetros:
# a: coeficiente cuadrático
# b: coeficiente lineal
# c: término independiente
def calcular_raices(a, b, c):

    # Verificamos que el coeficiente a sea diferente de 0.
    # Si a es 0, la ecuación deja de ser cuadrática.
    # Además, evitaríamos una división por cero.
    if a == 0:

        # Devolvemos un mensaje de error.
        return "Error: a no puede ser cero."

    # Calculamos el discriminante mediante la fórmula:
    #
    # d = b² - 4ac
    #
    # El discriminante determina cuántas raíces reales
    # tiene la ecuación cuadrática.
    d = b**2 - 4*a*c

    # CASO 1: DISCRIMINANTE POSITIVO
    #
    # Si d > 0, existen dos raíces reales diferentes.
    if d > 0:

        # Calculamos la primera raíz mediante:
        # x1 = (-b + √d) / 2a
        #
        # math.sqrt(d) calcula la raíz cuadrada de d.
        x1 = (-b + math.sqrt(d)) / (2*a)

        # Calculamos la segunda raíz mediante:
        # x2 = (-b - √d) / 2a
        x2 = (-b - math.sqrt(d)) / (2*a)

        # Devolvemos las dos raíces calculadas.
        # La letra f permite incluir variables
        # dentro del texto utilizando llaves {}.
        return f"Raíces: {x1} y {x2}"

    # CASO 2: DISCRIMINANTE IGUAL A CERO
    #
    # Si d == 0, existe una única raíz real doble.
    elif d == 0:

        # Calculamos la raíz mediante:
        # x = -b / 2a
        #
        # Devolvemos el resultado.
        return f"Raíz doble: {-b / (2*a)}"

    # CASO 3: DISCRIMINANTE NEGATIVO
    #
    # Si d < 0, no existen raíces reales.
    # En este programa no calculamos raíces complejas.
    return "No existen raíces reales."


# ==========================================================
# MENÚ PRINCIPAL DEL PROGRAMA
# ==========================================================

# Iniciamos un bucle infinito.
# El menú se repetirá hasta que el usuario
# seleccione la opción 2 para salir.
while True:

    # Mostramos el título del menú.
    # \n genera un salto de línea.
    print("\n===== MENÚ PRINCIPAL =====")

    # Mostramos las opciones disponibles.
    print("1. Calcular raíces cuadráticas")
    print("2. Salir")

    # Solicitamos una opción al usuario.
    # input() devuelve el valor ingresado como texto.
    opcion = input("Seleccione una opción: ")

    # Verificamos si el usuario eligió la opción 1.
    if opcion == "1":

        # Utilizamos try para intentar convertir
        # los valores ingresados a números decimales.
        try:

            # Solicitamos el coeficiente a.
            # float() convierte el texto ingresado
            # en un número decimal.
            a = float(input("Ingrese a: "))

            # Solicitamos el coeficiente b.
            b = float(input("Ingrese b: "))

            # Solicitamos el coeficiente c.
            c = float(input("Ingrese c: "))

            # Llamamos a la función calcular_raices().
            # Le enviamos los coeficientes a, b y c.
            #
            # La función devuelve las raíces
            # o un mensaje de error.
            #
            # print() muestra el resultado en pantalla.
            print(calcular_raices(a, b, c))

        # Capturamos un ValueError cuando el usuario
        # ingresa un valor que no puede convertirse
        # a un número decimal.
        #
        # Ejemplos: abc, @, #, texto vacío.
        except ValueError:

            # Mostramos un mensaje de error.
            # El programa no se cierra y vuelve al menú.
            print("Error: ingrese solo números.")

    # Verificamos si el usuario eligió la opción 2.
    elif opcion == "2":

        # Mostramos un mensaje de despedida.
        print("Fin del programa.")

        # break interrumpe el bucle while True.
        # De esta forma termina el programa.
        break

    # Este bloque se ejecuta cuando el usuario
    # ingresa una opción diferente de 1 o 2.
    else:

        # Informamos que la opción no es válida.
        print("Opción inválida.")
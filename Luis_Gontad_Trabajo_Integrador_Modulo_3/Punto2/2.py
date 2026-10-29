# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis

import math

# Para calcular las raices definimos la siguiente funcion, la misma recibe 3 parámetos ingresados por el usuario
def raices_cuadraticas(a, b, c):

    #Mediante la siguiente fórmula calculamos el discriminante
    #El mismo nos indica la cantidad de raices 
    discriminante = b ** 2 - 4 * a * c

    # Si el discriminante es negativo no hay solución
    if discriminante < 0:
        return ()

    # Si el discriminante es 0, sólo 1 solución.
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return (raiz,)

    # Si discriminante > 0 ( positivo ), hay 2 raíces.
    else:

        # Calculamos.
        raiz = math.sqrt(discriminante)

        # Prime Raiz
        r_1 = (-b + raiz) / (2 * a)

        # Segunda Raiz.
        r_2 = (-b - raiz) / (2 * a)

        return (r_1, r_2)


# Solicitamos al usuario ingresar los tres coeficientes de la función cuadrática.
while True:
    print("Bienvenido al calculador de raices de funciones cuadráticas")
    try:

        # Primer Coeficiente (a). Convertimos el mismo en decimal
        a = float(input("Ingrese el valor de a: "))

        # Segundo Coeficiente (b). Convertimos el mismo en decimal
        b = float(input("Ingrese el valor de b: "))

        # Tercer Coeficiente (c). Convertimos el mismo en decimal
        c = float(input("Ingrese el valor de c: "))

        # Verificación con coeficiente "a" para garantizar función cuadratica y evitar divisiones por 0
        if a == 0:
            print("El coeficiente 'a' deber ser distinto de 0, por favor ingrese los valores nuevamente.")
            continue

        # Llamamos a la función
        raiz = raices_cuadraticas(a, b, c)

        #Identificamos la cantidad de elementos
        if len(raiz) == 1:

            # Presentamos Resultados.
           print("Estos son los resultados para tu función cuadrática")
           print(f"El resultado es una raíz doble: {raiz[0]}")

        elif len(raiz) == 2:

            print("Estos son los resultados para tu función cuadrática")
            print(f"La primer raíz es R1={raiz[0]}")
            print(f"La segunda raíz es R2={raiz[1]}")

        else:
            print("Estos son los resultados para tu función cuadrática")
            print("La ecuación no tiene solucion.")
        break

    # Excepción por error en el valor ingresado, informando al usuario y solicitando ingresar nuevamente.
    except ValueError:
        print("Error en el valor ingresado, por favor ingresá todos los valores nuevamente.")
        continue
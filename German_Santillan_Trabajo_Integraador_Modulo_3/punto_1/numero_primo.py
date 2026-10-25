# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 1
# Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.
# Alumno: Germán Santillán.

#Definimos la función que determina si un número es primo o no.
def es_primo(numero):
    
    # Si el número es menor que 2, no es primo ya que el primer numero primo es 2.
    if numero < 2:
            return False

    # Iteramos desde 2 hasta el número ingresado para verificar si tiene divisores.
    for divisor in range(2, numero):

        # Si el número es divisible por algún otro número, no es primo.
        # El operador módulo (%) devuelve el resto de la división, por lo que si el resto es 0, significa que el número es divisible por el divisor.
        if numero % divisor == 0:
            return False
    # Si no se encontraron divisores, el número es primo.
    return True

# Comienzo del programa principal, solicitando al usuario que ingrese un número entero.
# Mientras el usuario no ingrese un número entero válido, se solicitará nuevamente.
while True:

    # Lo encapsulamos en un bloque try-except para manejar posibles errores.
    try:

        # Solicitamos al usuario que ingrese un número.
        numero = input("Ingrese un número entero: ")
        # Convertimos el valor ingresado a un número entero.
        numero = int(numero)

        # Verificamos si el número es negativo, ya que los números primos son enteros no negativos.
        if numero < 0:
            print("El valor ingresado NO es un número entero no negativo.")
            continue

        # Llamamos a la función es_primo para determinar si el número ingresado es primo o no.
        if es_primo(numero):
            print(f"El número {numero} es primo.")

        else:
            print(f"El número {numero} no es primo.")
        # Si el número ingresado es válido y se ha determinado si es primo o no, se rompe el bucle para finalizar el programa.
        break
    # En caso de que el valor ingresado no sea un número entero válido, se captura la excepción ValueError y se informa al usuario.
    except ValueError:
        print("El valor ingresado NO es un número entero válido. El valor ingresado fue: ", numero)
        continue


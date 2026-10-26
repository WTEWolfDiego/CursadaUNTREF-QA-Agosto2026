import math


def es_numero_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


print("Hola! Bienvenida al programa de numeros primos")
print("Escribi un numero entero, o 'salir' para terminar.")

while True:
    dato = input("Numero: ").strip()

    if dato.lower() == "salir":
        print("Gracias por usar el programa, hasta luego!")
        break

    try:
        numero = int(dato)
    except ValueError:
        print("Eso no es un numero entero, proba de nuevo.")
        continue

    if es_numero_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
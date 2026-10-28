import math


def resolver_cuadratica(a, b, c):
    if a == 0:
        raise ValueError("El valor de 'a' no puede ser 0 en una ecuación cuadrática.")

    discriminante = b ** 2 - 4 * a * c

    if discriminante < 0:
        return []

    if discriminante == 0:
        x = -b / (2 * a)
        return [x]

    raiz = math.sqrt(discriminante)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    return [x1, x2]


def pedir_y_resolver():
    try:
        a = float(input("Ingresá el valor de a: "))
        b = float(input("Ingresá el valor de b: "))
        c = float(input("Ingresá el valor de c: "))
    except ValueError:
        print("Error: los valores tienen que ser numéricos.")
        return

    try:
        raices = resolver_cuadratica(a, b, c)
    except ValueError as error:
        print(f"Error: {error}")
        return

    if len(raices) == 0:
        print("La ecuación no tiene solución en los números reales.")
    elif len(raices) == 1:
        print(f"La ecuación tiene una solución: x = {raices[0]}")
    else:
        print(f"La ecuación tiene dos soluciones: x1 = {raices[0]}, x2 = {raices[1]}")


def main():
    print("¡Bienvenido/a! Este programa calcula las raíces de una ecuación cuadrática (ax² + bx + c = 0).")
    seguir = "si"
    while seguir == "si":
        pedir_y_resolver()
        seguir = input("¿Querés resolver otra ecuación? (si/no): ").strip().lower()

    print("Programa finalizado. ¡Hasta la próxima!")


if __name__ == "__main__":
    main()

import math

def calcular_raices(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante < 0:
        return []

    elif discriminante == 0:
        raiz = -b / (2 * a)
        return [raiz]

    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return [raiz1, raiz2]

while True:
    entrada_a = input(
        "\nIngrese el valor de a o escriba Salir para finalizar: "
    )

    if entrada_a.strip().lower() == "salir":
        print("Programa finalizado.")
        break

    entrada_b = input("Ingrese el valor de b o escriba Salir: ")

    if entrada_b.strip().lower() == "salir":
        print("Programa finalizado.")
        break

    entrada_c = input("Ingrese el valor de c o escriba Salir: ")

    if entrada_c.strip().lower() == "salir":
        print("Programa finalizado.")
        break

    try:
        a = float(entrada_a)
        b = float(entrada_b)
        c = float(entrada_c)
    except ValueError:
        print("Debe ingresar valores numéricos. Use punto para los decimales.")
        continue

    if a == 0:
        print("El valor de a debe ser distinto de 0.")
        continue

    raices = calcular_raices(a, b, c)

    if len(raices) == 0:
        print("La ecuación no tiene raíces reales.")

    elif len(raices) == 1:
        print(f"La ecuación tiene una raíz real: {raices[0]}")

    else:
        print(f"Primera raíz: {raices[0]}")
        print(f"Segunda raíz: {raices[1]}")

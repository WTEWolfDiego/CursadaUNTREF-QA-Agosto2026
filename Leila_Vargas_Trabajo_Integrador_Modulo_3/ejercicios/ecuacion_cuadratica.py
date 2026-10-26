import math


def raices_cuadratica(a, b, c):
    if a == 0:
        raise ValueError("El coeficiente a no puede ser 0")

    delta = b * b - 4 * a * c

    if delta < 0:
        return ()
    if delta == 0:
        return (-b / (2 * a),)

    raiz_delta = math.sqrt(delta)
    return ((-b + raiz_delta) / (2 * a), (-b - raiz_delta) / (2 * a))


def leer_coeficiente(nombre):
    while True:
        dato = input(f"Valor de {nombre}: ").strip()
        if dato.lower() == "salir":
            return None
        try:
            return float(dato)
        except ValueError:
            print("Tiene que ser un numero.")


print("Hola! Bienvenida a la calculadora de ecuaciones cuadraticas")
print("Ingresa a, b y c, o escribi 'salir' en cualquier momento para terminar.")

while True:
    a = leer_coeficiente("a")
    if a is None:
        break
    b = leer_coeficiente("b")
    if b is None:
        break
    c = leer_coeficiente("c")
    if c is None:
        break

    try:
        raices = raices_cuadratica(a, b, c)
    except ValueError as error:
        print(error)
        continue

    if len(raices) == 0:
        print("La ecuacion no tiene raices reales")
    elif len(raices) == 1:
        print(f"Tiene una sola raiz: {raices[0]}")
    else:
        print(f"Raices: {raices[0]} y {raices[1]}")

print("Gracias por usar la calculadora, hasta luego!")
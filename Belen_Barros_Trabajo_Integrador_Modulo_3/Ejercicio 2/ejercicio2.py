import math

def raices(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return "La ecuación no tiene raíces reales"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)

        return x1, x2


a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print("No es una ecuación cuadrática")
else:
    resultado = raices(a, b, c)
    print("resultado:", resultado)

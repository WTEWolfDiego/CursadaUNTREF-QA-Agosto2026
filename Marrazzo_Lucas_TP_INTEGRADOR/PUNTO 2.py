
import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print("No es una ecuación cuadrática")
else:
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("La ecuación no tiene raíces reales")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)

        print("La primera raíz es:", x1)
        print("La segunda raíz es:", x2)

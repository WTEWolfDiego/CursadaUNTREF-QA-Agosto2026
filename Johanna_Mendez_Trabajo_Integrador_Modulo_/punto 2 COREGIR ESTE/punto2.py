
import math

def resolver_ecuacion(a, b, c):

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)

        return x1, x2

    elif discriminante == 0:
        x = -b / (2*a)

        return x

    else:
        return None


# Ingresar los valores
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Llamar a la función
resultado = resolver_ecuacion(a, b, c)

# Mostrar el resultado
if resultado is None:
    print("No hay soluciones reales")
elif isinstance(resultado, tuple):
    print("La ecuación tiene dos soluciones:")
    print("X1 =", resultado[0])
    print("X2 =", resultado[1])
else:
    print("La ecuación tiene una solución:")
    print("X =", resultado)

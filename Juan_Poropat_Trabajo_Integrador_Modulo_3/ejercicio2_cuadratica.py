import math

def calcular_raiz(a, b, c):
    if a == 0:
        if b == 0:
            return ()
        else:
            raiz = -c / b
            return (raiz,)
        
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return ()
    elif discriminante == 0:
        raiz = -b / (2*a)
        return (raiz,)
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (raiz1, raiz2)
print("Programa para calcular las raíces de una ecuación cuadrática")    
print("Ingrese las variables a continuación")

try:
    a = float(input("Valor de la variable A: "))
    b = float(input("Valor de la variable B: "))
    c = float(input("Valor de la variable C: "))
    
    resultado = calcular_raiz(a, b, c)
    if len(resultado) == 0:
        print("No se pueden calcular las raíces. Ecuación sin solución :(")
    elif len(resultado) == 1:
        print(f"La raíz es: {resultado[0]} :)")
    else:
        print(f"Las raíces son: {resultado[0]} y {resultado[1]}  :O")

except ValueError:
    print(f"Error: Ingrese únicamente valores numéricos válidos.")
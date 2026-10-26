###Ingresar las variables para la fx cuadratica: 
# x = (−b ± √[b² − 4·a·c]) / (2·a) ---> siendo d el discriminante: d = b² − 4·a·c
#Si d es > 0, hay 2 soluciones. Si d = 0, hay 1 solución. Si d < 0, no hay soluciones reales.
import math
def raices(a, b, c):

#Calcuar el discriminante: d = b² − 4·a·c
    d = b**2 - 4 * a * c
    print("El valor de d es:", d)

    if d > 0:
        print("Hay dos soluciones")
        raiz = math.sqrt(d)
        print("La raiz del discriminante es:", raiz)
        X1= (-b + raiz) / (2 * a)
        print ("El valor de X1 es:", X1)
        X2= (-b - raiz) / (2 * a)   
        print ("El valor de X2 es:", X2)
        return [X1, X2]
    elif d == 0:
        print("Hay una solución real")
        X= -b / (2 * a)
        print ("El valor de X es:", X) 
        return [X] 
    else:
        print("No hay solucion")
        return []
    

try:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    if a == 0:
        print("Error: a no puede ser 0")
    else:   
        resultado = raices(a, b, c)
        print("Las raíces son:", resultado)
    
except ValueError:                                    
    print("Error: debe ingresar valores numéricos")
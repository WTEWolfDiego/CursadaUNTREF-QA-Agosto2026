#En este ejercicio me costó más la parte matemática que el código en sí, tuve que volver a recordar cosas del secundario que vi hace casi 20 años

#Primero que nada imprto la libreria math como nos dijo el profe para poder usar sqrt y no hacer ** 0.5 como el ejercicio anterior donde no sabía de esta libreria
import math

#Ahora armo la función para calcular las soluciones de la ecuación, dependiendo de los números que ingresamos puede no tener solución, tener una sola solución o tener dos soluciones
def calcular_soluciones(a, b, c):
    #Con esto calculo el discriminante
    discriminante = (b ** 2) - (4 * a * c)
    
    #Uso de vuelta if elif else para controlar el flujo del programa dependiendo del resultado del discriminante, uso el return para devolver directamente las strings que se le van a mostrar al usuario así después simplemente puedo llamar a la función y printear lo que me returne
    if discriminante < 0:
        return "La ecuación no tiene solución"
    elif discriminante == 0:
        x = -b / (2 * a)
        return f"La ecuación tiene una única solución: {x}"
    else:
        raiz_discriminante = math.sqrt(discriminante)
        x1 = (-b + raiz_discriminante) / (2 * a)
        x2 = (-b - raiz_discriminante) / (2 * a)
        return f"Las ecuación tiene dos soluciones: x1 = {x1} y x2 = {x2}"

#Este es el loop principal del programa, similar al primer ejercicio lo metí en un while para que esté siempre activo hasta que el usuario decida salir y no usarlo más
while True:
    
    #Con esto le pido al usuario que ingrese las variables por teclado. Le puse float porque tranquilamente el usuario puede ingresar números con decimales por ejemplo 10.5
    a = float(input("Ingrese variable a: "))
    b = float(input("Ingrese variable b: "))
    c = float(input("Ingrese variable c: "))
    
    #Acá agregué esta validación porque me di cuenta haciendo pruebas que si a es igual a 0 iba a haber una división por 0 y me explotaba todo
    if a == 0:
        print("Error: No podés dividir por cero! Revisá la variable a")
    else:
        #Si a no es igual a 0 entonces llamo a la función para calcular las soluciones con los 3 inputs del usuario como argumentos (a, b, c)
        resultado = calcular_soluciones(a, b, c)
        print(resultado)
    
    #Acá le pregunto al usuario si quiere seguir usando el programa después de obtener el reslutado
    #Usé lower también por si el usuario escribe SI, Sí o sI para que todo pase a minúscula y pueda usar != para operar con el texto exacto
    continuar = input("\n¿Querés seguir usando el programa? (si/no): ").lower()
    
    #Acá directamente verifico si la respuesta es si para seguir, si el usuario pone cualquier otra cosa el programa se termina (para evitar validar NO, nO, etc.)
    if continuar != "si":
        print("Gracias por usar el programa")
        break
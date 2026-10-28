# Punto 2:

# Escribir una función que, dado el ingreso de 3 variables (a, b, c), retorne las raíces resultantes 
# de una ecuación cuadrática. 

# Descripción coloquial de la fórmula:
# Identifica los coeficientes a, b y c de la ecuación cuadrática. Calcula el discriminante: b aL CUADRADO -4ac
# Si el discriminante es positivo, hay dos raíces reales. Si es cero, hay una raíz real. Si es negativo,
# no hay raíces reales.
# Sustituye a, b y el discriminante en la fórmula cuadrática para encontrar las raíces.
# no se puede dividir por 0 => A =/= 0


import math

criterio_salida = 'fin'

def bienvenida():
     print("Este es un programa para calcular una ecuación cuadrática. Creo. Se le solicitarán 3 números: " \
     "A, B y C. Tener en cuenta que A no puede ser igual a 0.")

def solicitar_variable(criterio_salida, indicador_variable): 
    
    while True:
        # primero solicitar el input, después limpiarlo
        coeficiente = input(f"Ingrese el valor del coeficiente {indicador_variable} para calcular la ecuación cuadrática o ingrese 'Fin' si desea salir.") 
        coeficiente = coeficiente.strip().lower() #limpieza + sólo minúsculas

        if coeficiente == criterio_salida: #fin primero porque es el más específico
            print("Fin del programa.")
            return #comparación + corte del while     

        # poner la validacion de la variable A rompe la validación siguiente que entra en el except. 
        # trata de parsear a int cualquier string y da exception por value error que no puede agarrar el try
 
        try:
            coeficiente = int(coeficiente) # parseo a int   

            #TODO: por qué si yo hardcodee la variable como un número la tomaba como un string?
            if int(indicador_variable) == 1 and coeficiente == 0:
                print("La variable A no puede ser igual a 0, ya que no puede dividirse. Ingrese otro número.")
                continue #devuelve al loop sin llegar al return

            return coeficiente  # corte del while y devolución para asignación 


                         
        except ValueError:
            print("Comando inválido. Ingrese un número entero o la palabra 'Fin'.")
            continue



# era esto o la tesis
def calcular_discriminante(coeficiente_a, coeficiente_b, coeficiente_c):
    discriminante = (coeficiente_b * coeficiente_b) - 4 * (coeficiente_a) * (coeficiente_c)
    return discriminante



def evaluar_discriminante(discriminante, coeficiente_a, coeficiente_b, coeficiente_c):
    if discriminante < 0:
        print(f"El discriminante es {discriminante}. No hay raíces reales. Gracias, vuelva prontos.")
    elif discriminante == 0:
        resultado_raiz = -coeficiente_b + math.sqrt (discriminante) / 2 * coeficiente_a
        print(f"El discriminante es {discriminante}. La raíz de la ecuación cuadrática de los valores {coeficiente_a}, {coeficiente_b} y {coeficiente_c} es {resultado_raiz}.")
            
    else:
        resultado_raiz_positivo = (-coeficiente_b + math.sqrt (discriminante)) / (2 * coeficiente_a) #ME CACHO EN LOS PARENTESIS
        resultado_raiz_negativo = (-coeficiente_b - math.sqrt (discriminante)) / (2 * coeficiente_a) #Y LA PRIORIZACION
        print("Esta ecuación tiene dos posibles raíces.")
        print(f"El discriminante es {discriminante}. La raíz positiva de la ecuación cuadrática de los valores {coeficiente_a}, {coeficiente_b} y {coeficiente_c} es {resultado_raiz_positivo}.")
        print(f"El discriminante es {discriminante}. La raíz negativa de la ecuación cuadrática de los valores {coeficiente_a}, {coeficiente_b} y {coeficiente_c} es {resultado_raiz_negativo}.")


def volver_empezar(criterio_salida):
    print("¿Desea realizar otro cálculo?")
    while True:
        eleccion_usuario = input("Escriba Si para continuar. Escriba Fin para detener el programa.")
        eleccion_usuario = eleccion_usuario.strip().lower()
        if eleccion_usuario == criterio_salida:
            print("Fin del programa.")
            return
        
        #no lo tomaba porque faltaba el IF
        try:
            if eleccion_usuario == "si":       
                return True
        
        except ValueError:
            print("Comando inválido. Ingrese la palabra 'Si' o 'Fin'.")
            continue
    


# TODO: relaciones entre break, return, None y como salir de una función no es lo mismo que salir del programa
# Son capas de funciones?

while True:
    bienvenida()


    coeficiente_a = solicitar_variable(criterio_salida, indicador_variable=1)
    if coeficiente_a is None:
        break
    coeficiente_b = solicitar_variable(criterio_salida, indicador_variable=2)
    if coeficiente_b is None:
        break
    coeficiente_c = solicitar_variable(criterio_salida, indicador_variable=3)
    if coeficiente_c is None:
        break

    discriminante = calcular_discriminante(coeficiente_a, coeficiente_b, coeficiente_c)
    evaluar_discriminante(discriminante, coeficiente_a, coeficiente_b, coeficiente_c)

    if not volver_empezar(criterio_salida):
        break



#me hubiera gustado hacer un método que imprima un mensaje aparte personalizado para cada solucion segun
#el resultado pero me excede. Pensé en settear un booleano pero es un montón.
#En otra vida haré a las variables como clases hija de Variable

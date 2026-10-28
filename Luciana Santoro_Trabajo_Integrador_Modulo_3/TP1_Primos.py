# Trabajo Integrador - Módulo 3
# Punto 1:
# Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.
# notas de clase: 
# -> Debe ser por input
# -> debe permitirle al usuario salir
# -> debe loopear hasta que el usuario decida salir

# Pasos 
# Solicitud input
# Validacion del usuario -> Qué puede ingresar el usuario? Letras, números, letras que no son fin, números float
# Validación del valor
# Evaluación


#necesito loopear hasta que el usuario ingrese un número entero o un fin.
# problema-> orden de la validación. Primero el try? primero el if? nunca setea el while a false? sólo con un break?
# el orden de validación de los apuntes dice ir de lo particular a lo general. VER CLASE SEIS
# otra pregunta. En cuántas funciones separaría el ingreso y la validación del usuario?
# por qué validación conviene que comience? si es = a fin? después si es un número válido? #ver validación clase 6


criterio_salida = 'fin'
        
def solicitar_numero(criterio_salida): #creo que no necesita un parámetro más que el criterio de salida, el input no se pone en una lista
    #podría hacer una lista con toooodos los números y todos los resultados pero me parece mucho y no es pertinente a la consigna
    
    while True:
            # primero solicitar el input, después limpiarlo
        numero_ingresado = input(f"Ingrese el número entero mayor a 0 (cero) que desee consultar si es primo o ingrese 'Fin' si desea salir.") 
        numero_ingresado = numero_ingresado.strip().lower() #limpieza + sólo minúsculas

        #validación de si el usuario quiere terminar el programa
        if numero_ingresado == criterio_salida: #fin primero porque es el más específico
                print("No se ingresarán más números para consultar si son primos.")
                return #comparación + corte del while     

        try:
            # TODO ok, como sería un código donde dos métodos se referencian mutuamente?
            # es_primo(int(numero_ingresado)) #falló porque te morfaste el parseo a int
            # entiendo que la evaluación y la impresión irían aparte pero eso funciona y lo otro no me salió.
            numero_ingresado = int(numero_ingresado) #parseo a int

            if int(numero_ingresado) < 0:
                print("Sólo los números mayores a cero pueden ser primos.")

            if numero_ingresado == 1:
                print("Menos pregunta alguna deidad y perdona. Ni los matemáticos se ponen de acuerdo sobre el número.")

            if numero_ingresado == 2: #harcodeado. Si pongo el rango en 1, 2 da como no primo y lo es.
                print(f"El número {numero_ingresado} es primo.")
            
            # ver comentario debajo de todo - código copiado de otro lado y modificado
            for numeros in range(2, numero_ingresado):
                if numero_ingresado % numeros == 0: 
                    #muestra solo el primero. Cambiar a que muestre todos los divisores no es algo que pueda plantearme en este momento.
                    print(f"No es primo {numeros} es divisor de {numero_ingresado}.")
                    break
                    #si pongo continue acá loopea la cantidad de veces hasta el número
                
                print("Es primo")
                break
                #pero si le pongo return acá, no loopea hasta que el usuario de fin, sino que termina.
                #break dio igual, no lo tomó -> era break no te entiendo python.
                
        except ValueError:
            print("Comando inválido. Ingrese un número entero mayor a 0 (cero) o la palabra 'Fin'.")
            continue

numero_ingresado = solicitar_numero(criterio_salida)

#código definitivamente copiado porque yo estudié arte, química orgánica y algo de Freud.
#https://ellibrodepython.com/numeros-primos-python la fuente del código 
#la definición de primo es que es divisible por uno y por si mismo. Este código propone iterar todos los números de 
#2 hasta el ingresado (supongo que cuanto más grande, más lento. Excepto que imprima siemrpe el primero y corte). 
# Por qué 2? porque sino 0 no se puede y 1 va a dar todos falsos positivos.
# Todos los números son divisibles por 1. Si al menos uno de los números que iteran hasta el 
# número propuesto es divisor, dará False, si ninguno es divisor, True -> es primo
# para esto, usa la operación de resto, y revisa si es igual a 0.
# hace un if sin else porque con el return ya tendría la respuesta y el print dentro que la teoría del módulo 3 
# indica que debería separarse la impresión del cálculo. Es tan chico este método que no estoy segura.
# imprime todos los divisores o imprime el primero que encuentra? Vale la pena hacer una lista con todos los divisores?
# y si no entra en el if porque la condición no se cumple, es primo. 

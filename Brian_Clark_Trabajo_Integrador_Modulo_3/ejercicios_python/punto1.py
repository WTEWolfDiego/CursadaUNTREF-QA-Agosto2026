#Comienzo definiendo una función para detectar si un número es primo o no que voy a llamar más adelatne en el loop principal del programa
def esPrimo(numero):

    if numero <= 1:
        return False

    #Esto lo tuve que googlear porque honestamente hace mucho que no toco nada matemático.
    #Resulta que para saber si un número es primo lo que se hace es buscar la raíz cuadrada (de ahí el numero ** 0.5) y después dividir el número por todos los números que están entre 2 y la raíz cuadrada, con un int porque obviamente no todas las raices cuadradas son enteros
    #Le tuve que agregar +1 porque con este método de la raíz cuadrada puede pasar que el segundo número del range no esté incluido en la división (por ejemplo al calcular el número 11, la raiz cuadrada es 3.3 y el range(2,3) no hace la división por 3, pero si le sumo 1 para que sea 4 la hace)
    #Después uso el operador de módulo para saber si las divisiones tienen resto 0 o no

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False  #Esto significa que al iterar por todos los números con el for encontró divisores que no son 1 o el número mismo, entonces el número no es primo
            
    return True  #Si el loop termina sin encontrar divisores significa que el número es primo


#Este sería el loop principal del programa, lo metí adentro de un while para que esté siempre corriendo y no se termine apenas el usuario ingresa un único número.
while True:
    entrada = input('Ingresá un número (o escribí "salir" para salir del programa): ')
    
    #Con este if verificamos si el usuario quiere salir, gogleé el método "lower" por si el usuario escribe SALIR o Salir, transforma la entrada por teclado del usuario a minúscula así puedo usar == para detectarlo
    if entrada.lower() == 'salir':
        print('Gracias por utilizar el programa')
        break

    #Con este try hago las validaciones del número ingresado y de la función esPrimo
    try:
        #Convierto la entrada a integer para poder hacer operaciones matemáticas y por si el usuario ingresa texto que no sea 'salir'
        numero = int(entrada)
        
        #El primer if valida si el número ingresado por el usuario es un número natural mayor a 1 y le explica al usuario por qué cualquier otro número que escribió no puede ser primo
        #El elif y el else revisan si esPrimo es True o False y muestran el mensaje correspondiente 
        if numero <= 1:
            print(f'El {numero} no puede ser primo (los números primos deben ser números enteros naturales mayores a 1 que sólo tienen dos divisores)')
        elif esPrimo(numero):
            print(f'El {numero} es primo')
        else:
            print(f'El {numero} no es primo')

    #Este except de ValueError debería atajar cualquier cosa que escriba el usuario y pedirle que ingrese un número correcto o que salga       
    except ValueError:
        print('Por favor, ingresá un número entero válido o escribí "salir" para salir del programa')
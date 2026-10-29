# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis

#Función que determina número primo.
def  es_primo(numero):
    
    # Los números menores que 2 no son primos.
    if numero < 2:
            return False

    # Realizamos iteración desde el 2 hasta el número ingresado buscando divisores.
    for i in range(2, numero):

        # Si el resto es 0, no es primo.
        if numero % i == 0:
            return False
    # Si no, el número es primo.
    return True

print("Bienvenido al programa de números primos")
# Solicitamos al usuario ingrese un número entero, en caso de error en el número ingresado, el sistema vuelve a solicitar un número.
while True:

    try:
        # Solicitamos ingresar un número.
        texto = input("Por favor ingresá un número entero o 'salir' para finalizar: ")

        if texto.lower() == "salir":
            print("Gracias por participar!!!")
            break

        # convertimos el dato ingresado en número entero.   
        numero = int(texto)

        # Varificamos que el número ingresado no sea negativo.
        if numero < 0:
            print("El valor ingresado debe ser positivo.")
            continue

        if es_primo(numero):
            print(f"El número {numero} es primo.")

        else:
            print(f"El número {numero} no es primo.")
        break
    # Excepción por error en el valor ingresado, informando al usuario y solicitando ingresar nuevamente un numero.
    except ValueError:
        print("El número ingresado fue: ", texto," este número no es válido, reingresá un número válido")
        continue

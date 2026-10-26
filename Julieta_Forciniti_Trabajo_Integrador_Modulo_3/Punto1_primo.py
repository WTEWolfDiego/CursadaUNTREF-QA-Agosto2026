#Solicitud de Nro:
def es_primo(numero):
    primo = True
    if numero < 2:
        primo = False  #Los números menores a 2 no son primos
    for i in range(2, numero):
        if numero % i == 0:  #Si la división es exacta, no es primo.
            primo = False
    return primo 
texto = input("Ingrese un número: ")       

if texto.isdigit():  
    numero = int(texto)
    print("Numero ingresado", numero)
    if es_primo(numero):
        print ("es nro. primo")
    else:
        print ("No es nro. primo")
else:
        print ("Error: Ingrese numero entero positivo")
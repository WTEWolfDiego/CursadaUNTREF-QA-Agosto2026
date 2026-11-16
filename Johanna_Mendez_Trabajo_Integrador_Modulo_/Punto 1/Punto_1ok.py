numero = int(input("Ingrese un numero: "))

if numero <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es primo")
else:
    print("No es primo")
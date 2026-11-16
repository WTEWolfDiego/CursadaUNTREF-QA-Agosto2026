
numero = int(input("Ingrese un número: "))

if numero <= 1:
    print("El número no es primo")
else:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("El número es primo")
    else:
        print("El número no es primo")
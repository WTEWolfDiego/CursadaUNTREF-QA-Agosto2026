numero = int(input("Ingresá un número: "))

primo = numero >= 2

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("Es primo")
else:
    print("No es primo")

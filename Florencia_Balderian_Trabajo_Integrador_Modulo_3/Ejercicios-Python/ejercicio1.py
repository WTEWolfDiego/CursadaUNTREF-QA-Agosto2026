while True:
    entrada = input(
        "\nIngrese un número entero y se le indicará si es o no primo. "
        "Para salir de la ejecución, escriba Salir. "
    )

    if entrada.strip().lower() == "salir":
        print("Programa finalizado.")
        break

    try:
        numero = int(entrada)
    except ValueError:
        print("Debe ingresar un número entero o escribir Salir.")
        continue

    es_primo = True

    if numero < 2:
        es_primo = False
    else:
        for divisor in range(2, numero):
            if numero % divisor == 0:
                es_primo = False
                break
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

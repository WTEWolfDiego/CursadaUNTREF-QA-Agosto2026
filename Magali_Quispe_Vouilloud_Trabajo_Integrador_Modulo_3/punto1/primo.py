def es_primo(numero):
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def main():
    print("¡Bienvenido/a! Este programa te dice si un número es primo o no.")

    seguir = "si"
    while seguir == "si":
        entrada = input("Ingresá un número entero: ")

        try:
            numero = int(entrada)
            if es_primo(numero):
                print(f"El número {numero} es primo.")
            else:
                print(f"El número {numero} no es primo.")
        except ValueError:
            print("Error: tenés que ingresar un número entero.")

        seguir = input("¿Querés probar otro número? (si/no): ").strip().lower()

    print("Programa finalizado. ¡Hasta la próxima!")


if __name__ == "__main__":
    main()

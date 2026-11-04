# ==========================================================
# PROGRAMA: VERIFICAR SI UN NÚMERO ES PRIMO
#
# Funcionalidades:
# 1. Mostrar un menú principal.
# 2. Solicitar un número entero.
# 3. Verificar si el número es primo.
# 4. Validar entradas incorrectas.
# 5. Permitir ingresar varios números.
# 6. Permitir salir del programa.
# ==========================================================


# try permite controlar posibles interrupciones
# durante la ejecución del programa.
try:

    # Bucle principal del programa.
    # Se repite hasta que el usuario elija salir.
    while True:

        # Mostrar las opciones disponibles.
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Verificar número primo")
        print("2. Salir")
        print("==========================")

        # Solicitar al usuario una opción del menú.
        # input() devuelve el dato ingresado como texto.
        opcion = input("Seleccione una opción: ").strip()

        # Verificar si el usuario eligió la opción 1.
        if opcion == "1":

            # Bucle que permite verificar varios números
            # sin regresar al menú principal.
            while True:

                # Intentar convertir la entrada a entero.
                try:

                    # Solicitar un número al usuario.
                    entrada = input(
                        "\nIngrese un número entero: "
                    )

                    # Convertir el texto ingresado
                    # a un número entero.
                    numero = int(entrada)

                    # Suponemos inicialmente que
                    # el número ingresado es primo.
                    es_primo = True

                    # Los números menores o iguales a 1
                    # no son números primos.
                    if numero <= 1:

                        # Cambiamos la variable a False.
                        es_primo = False

                    else:

                        # Recorremos los posibles divisores
                        # desde 2 hasta numero - 1.
                        for i in range(2, numero):

                            # El operador % calcula el resto
                            # de una división.
                            #
                            # Si el resto es 0, significa que
                            # el número es divisible por i.
                            if numero % i == 0:

                                # El número no es primo porque
                                # tiene un divisor distinto
                                # de 1 y de sí mismo.
                                es_primo = False

                                # Interrumpimos el bucle for
                                # porque ya encontramos un divisor.
                                break

                    # Comprobar el resultado de la validación.
                    if es_primo:

                        # Mostrar el resultado cuando es primo.
                        print(
                            f"El número {numero} es primo"
                        )

                    else:

                        # Mostrar el resultado cuando no es primo.
                        print(
                            f"El número {numero} no es primo"
                        )

                # Capturar errores de conversión a entero.
                # Ejemplos: abc, 12.5, @, #, 2a.
                except ValueError:

                    # Mostrar el valor incorrecto ingresado.
                    print(
                        f"Error: '{entrada}' "
                        "no es un número entero válido."
                    )

                # Bucle para consultar si el usuario
                # desea ingresar otro número.
                while True:

                    # Solicitar una respuesta S o N.
                    # strip() elimina espacios al principio
                    # y al final del texto.
                    # upper() convierte el texto a mayúsculas.
                    continuar = input(
                        "\n¿Desea ingresar otro número? (S/N): "
                    ).strip().upper()

                    # Verificar que la respuesta sea válida.
                    if continuar in ("S", "N"):

                        # Salir del bucle de validación
                        # porque la respuesta es correcta.
                        break

                    # Mostrar error si la respuesta
                    # es diferente de S o N.
                    print("Error: ingrese S o N.")

                # Si el usuario responde N,
                # regresar al menú principal.
                if continuar == "N":
                    break

        # Verificar si el usuario eligió salir.
        elif opcion == "2":

            # Mostrar mensaje de despedida.
            print("Gracias por utilizar el programa.")

            # Finalizar el bucle principal.
            break

        # Controlar opciones diferentes de 1 y 2.
        else:

            # Mostrar la opción inválida ingresada.
            print(
                f"Error: la opción '{opcion}' no es válida."
            )

# Capturar Ctrl+C, que interrumpe el programa
# desde la terminal.
except KeyboardInterrupt:

    print("\nPrograma interrumpido por el usuario.")

# Capturar el cierre de la entrada estándar,
# por ejemplo Ctrl+Z y Enter en Windows.
except EOFError:

    print("\nSe cerró la entrada de datos.")

# Este bloque se ejecuta cuando el programa termina,
# incluso si se produjo una de las interrupciones
# anteriores.
finally:

    print("Fin de la ejecución.")
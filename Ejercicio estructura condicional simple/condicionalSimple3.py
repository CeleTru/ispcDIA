while True:
    genero = input("Ingrese su género ('f' para femenino, 'm' para masculino): ").lower()

    if genero == 'f':
        print("Votará en una mesa femenina.")
    elif genero == 'm':
        print("Votará en una mesa masculina.")
    else:
        print("Género no válido. Por favor, ingrese 'f' o 'm'.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break

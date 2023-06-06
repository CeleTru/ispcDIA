while True:
    edad = int(input("Ingrese su edad: "))

    if edad > 16:
        print("Puede votar.")
    else:
        print("No puede votar.")

    opcion = input("¿Desea realizar otra verificación? (s/n): ").lower()
    if opcion != 's':
        break
    
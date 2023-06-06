while True:
    palabra1 = input("Ingrese la primera palabra: ").lower()
    palabra2 = input("Ingrese la segunda palabra: ").lower()

    if palabra1 == palabra2:
        print("Las palabras ingresadas son iguales.")
    else:
        print("Las palabras ingresadas son diferentes.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break

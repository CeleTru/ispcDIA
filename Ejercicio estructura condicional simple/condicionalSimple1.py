while True:
    letra1 = input("Ingrese la primera letra: ").lower()
    letra2 = input("Ingrese la segunda letra: ").lower()

    if letra1 == letra2:
        print("Las letras ingresadas son iguales.")
    else:
        print("Las letras ingresadas son diferentes.")

    opcion = input("¿Desea verificar nuevamente? (s/n): ").lower()
    if opcion != 's':
        break

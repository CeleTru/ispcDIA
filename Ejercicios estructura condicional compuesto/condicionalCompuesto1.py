"""Introducir los lados de un triángulo y visualizar por pantalla si dicho
triángulo es equilátero, isósceles o escaleno. """


while True:
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

    opcion = input("¿Desea ingresar otro triángulo? (s/n): ").lower()
    if opcion != 's':
        break

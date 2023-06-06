"""
Realice un programa que lea tres números, muestre cuál es el mayor y
determine si es par o impar.
"""


while True:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    mayor = max(num1, num2, num3)

    print("El número mayor es:", mayor)

    if mayor % 2 == 0:
        print("El número mayor es par.")
    else:
        print("El número mayor es impar.")

    opcion = input("¿Desea ingresar otros tres números? (s/n): ")
    if opcion.lower() != 's':
        break

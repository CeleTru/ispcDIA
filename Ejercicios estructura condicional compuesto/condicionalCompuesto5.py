"""
Realice un programa que pida un número del 1 al 12 y diga el nombre
del mes correspondiente.
"""

while True:
    numero = int(input("Ingrese un número del 1 al 12: "))

    if numero == 1:
        print("El número corresponde al mes de Enero.")
    elif numero == 2:
        print("El número corresponde al mes de Febrero.")
    elif numero == 3:
        print("El número corresponde al mes de Marzo.")
    elif numero == 4:
        print("El número corresponde al mes de Abril.")
    elif numero == 5:
        print("El número corresponde al mes de Mayo.")
    elif numero == 6:
        print("El número corresponde al mes de Junio.")
    elif numero == 7:
        print("El número corresponde al mes de Julio.")
    elif numero == 8:
        print("El número corresponde al mes de Agosto.")
    elif numero == 9:
        print("El número corresponde al mes de Septiembre.")
    elif numero == 10:
        print("El número corresponde al mes de Octubre.")
    elif numero == 11:
        print("El número corresponde al mes de Noviembre.")
    elif numero == 12:
        print("El número corresponde al mes de Diciembre.")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 12.")

    opcion = input("¿Desea ingresar otro número? (s/n): ")
    if opcion.lower() != 's':
        break

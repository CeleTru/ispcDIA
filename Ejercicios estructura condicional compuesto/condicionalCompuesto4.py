"""
Confeccione un programa que pida un número del 1 al 7 y diga el día de
la semana correspondiente. 
"""

while True:
    numero = int(input("Ingrese un número del 1 al 7: "))

    if numero == 1:
        print("El número corresponde al día Lunes.")
    elif numero == 2:
        print("El número corresponde al día Martes.")
    elif numero == 3:
        print("El número corresponde al día Miércoles.")
    elif numero == 4:
        print("El número corresponde al día Jueves.")
    elif numero == 5:
        print("El número corresponde al día Viernes.")
    elif numero == 6:
        print("El número corresponde al día Sábado.")
    elif numero == 7:
        print("El número corresponde al día Domingo.")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 7.")

    opcion = input("¿Desea ingresar otro número? (s/n): ")
    if opcion.lower() != 's':
        break


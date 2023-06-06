"""Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo. """

import random

while True:
    numeros = []

    for _ in range(10):
        numero = random.randint(1, 1000)
        numeros.append(numero)

    print("Números ingresados:", numeros)

    mayores_100 = 0
    menores_100 = 0
    maximo = max(numeros)
    minimo = min(numeros)

    for numero in numeros:
        if numero > 100:
            mayores_100 += 1
        else:
            menores_100 += 1

    print("Cantidad de números mayores a 100:", mayores_100)
    print("Cantidad de números menores a 100:", menores_100)
    print("Número máximo:", maximo)
    print("Número mínimo:", minimo)

    opcion = input("¿Desea ingresar otro conjunto de números? (s/n): ")
    if opcion.lower() != 's':
        break

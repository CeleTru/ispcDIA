"""Leer 10 números y mostrar solamente los números positivos, y su sumatoria.   """
import random

while True:
    numeros = []
    sumatoria_positivos = 0

    # Generar 10 números aleatorios
    for _ in range(10):
        numero = random.randint(-100, 100)
        numeros.append(numero)

    # Imprimir todos los números generados
    print("Números generados:", numeros)

    # Filtrar y sumar los números positivos
    numeros_positivos = [num for num in numeros if num > 0]
    sumatoria_positivos = sum(numeros_positivos)

    # Imprimir los números positivos y su sumatoria
    print("Números positivos:", numeros_positivos)
    print("Sumatoria de los números positivos:", sumatoria_positivos)

    opcion = input("¿Desea ejecutar el programa nuevamente? (s/n): ")
    if opcion.lower() != 's':
        break

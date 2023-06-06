"""Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.   """
import random

while True:
    numeros_negativos = []

    # Generar 15 números negativos aleatorios
    for _ in range(15):
        numero_negativo = random.randint(-100, -1)
        numeros_negativos.append(numero_negativo)

    # Imprimir números negativos juntos
    print("Números negativos generados:")
    print(*numeros_negativos, sep=" ")

    # Convertir números negativos a positivos
    numeros_positivos = [abs(numero) for numero in numeros_negativos]

    # Imprimir números positivos juntos
    print("Números positivos:")
    print(*numeros_positivos, sep=" ")

    # Preguntar al usuario si desea repetir el programa
    respuesta = input("¿Desea repetir el programa? (s/n): ")
    if respuesta.lower() != "s":
        break

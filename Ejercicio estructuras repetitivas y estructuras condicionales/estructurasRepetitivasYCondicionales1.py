"""Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.  """

while True:
    pares = 0
    sumatoria_pares = 0

    for i in range(1, 5):
        numero = int(input(f"Ingrese el número {i} de 4: "))

        if numero % 2 == 0:
            pares += 1
            sumatoria_pares += numero

    impares = 4 - pares

    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Sumatoria de números pares:", sumatoria_pares)

    opcion = input("¿Desea ingresar otro conjunto de números? (s/n): ")
    if opcion.lower() != 's':
        break

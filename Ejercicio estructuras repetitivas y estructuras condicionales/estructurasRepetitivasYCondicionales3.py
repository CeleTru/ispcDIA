"""Ingresar las edades y el sexo de 15 personas y determinar cuántas 
son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.  """

import random

while True:
    edades = []
    sexos = []
    mujeres = 0
    varones = 0
    mayores_edad = 0
    menores_edad = 0

    # Generar edades y sexos de manera aleatoria
    for _ in range(15):
        edad = random.randint(1, 100)
        sexo = random.choice(['M', 'F'])

        edades.append(edad)
        sexos.append(sexo)

    # Imprimir lista de personas
    print("Lista de personas:")
    for i in range(15):
        print(f"Persona {i+1}: Edad={edades[i]}, Sexo={sexos[i]}")

    # Contar mujeres, varones, mayores de edad y menores de edad
    for i in range(15):
        if sexos[i] == 'F':
            mujeres += 1
        else:
            varones += 1

        if edades[i] >= 18:
            mayores_edad += 1
        else:
            menores_edad += 1

    # Mostrar resultados
    print("Resultados:")
    print("Cantidad de mujeres:", mujeres)
    print("Cantidad de varones:", varones)
    print("Cantidad de mayores de edad:", mayores_edad)
    print("Cantidad de menores de edad:", menores_edad)

    opcion = input("¿Desea ingresar otra lista de personas? (s/n): ")
    if opcion.lower() != 's':
        break

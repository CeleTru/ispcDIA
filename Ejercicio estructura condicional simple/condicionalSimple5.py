def pesos_a_dolares(cantidad):
    return cantidad / 20

def dolares_a_pesos(cantidad):
    return cantidad * 20

while True:
    print("1. Pesos a Dólares")
    print("2. Dólares a Pesos")
    opcion = input("Seleccione el tipo de cambio (1 o 2): ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad en pesos: "))
        resultado = pesos_a_dolares(cantidad)
        print(f"{cantidad} pesos equivale a {resultado} dólares.")
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad en dólares: "))
        resultado = dolares_a_pesos(cantidad)
        print(f"{cantidad} dólares equivale a {resultado} pesos.")
    else:
        print("Opción inválida. Intente nuevamente.")

    opcion = input("¿Desea realizar otra conversión? (s/n): ").lower()
    if opcion != 's':
        break

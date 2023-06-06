"""
    Realice un programa que le permita al usuario simular el pago
    ingresando el importe y la forma de pago:
    • Contado (1): se aplica un descuento del 10% al importe
    • Tarjeta (2): se aplica un interés de 10%
    • Débito (3): se aplica un descuento del 5%
    Mostrar el importe, el descuento o interés y el importe total.
"""


while True:
    importe = float(input("Ingrese el importe a pagar: "))
    forma_pago = int(input("Seleccione la forma de pago:\n1. Contado\n2. Tarjeta\n3. Débito\n"))

    if forma_pago == 1:
        descuento = importe * 0.1  # 10% de descuento
        importe_total = importe - descuento
        print("Importe: $", importe)
        print("Descuento: $", descuento)
        print("Importe total: $", importe_total)
    elif forma_pago == 2:
        interes = importe * 0.1  # 10% de interés
        importe_total = importe + interes
        print("Importe: $", importe)
        print("Interés: $", interes)
        print("Importe total: $", importe_total)
    elif forma_pago == 3:
        descuento = importe * 0.05  # 5% de descuento
        importe_total = importe - descuento
        print("Importe: $", importe)
        print("Descuento: $", descuento)
        print("Importe total: $", importe_total)
    else:
        print("Forma de pago no válida. Intente nuevamente.")

    opcion = input("¿Desea realizar otro pago? (s/n): ")
    if opcion.lower() != 's':
        break
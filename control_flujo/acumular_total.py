
# Crear un programa que solicite precios de productos y acumule el total
# de la compra hasta que el usuario ingrese "fin".

print("Para finalizar escriba fin")
sub_total = 0

while True:

    precio_producto = input("Ingrese precio del producto: ")

    if precio_producto == "fin":
        print(f"El total de la compra es: {sub_total}")
        break

    precio_producto = int(precio_producto)

    sub_total = precio_producto + sub_total
    print(f"subtotal: {sub_total}")


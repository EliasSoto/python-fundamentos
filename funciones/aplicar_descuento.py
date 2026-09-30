
# Función que aplica descuento
def aplicar_descuento(total: int, por_descuento: int):
    total_final = total - (total*(por_descuento / 100))
    return round(total_final)



# Aplicación main
total_pagar = int(input("ingrese lo que va a pagar el cliente: "))
descuento = str(input("necesita descuento si/no: ").strip().lower())

if descuento == "si":
    porcentaje = int(input("Ingrese porcentaje de descuento: "))
    total_descuento = aplicar_descuento(total_pagar, porcentaje)

    print(f"Lo que debe pagar el cliente es: {total_descuento}")
else:
    print(f"El total a pagar por el cliente es: {total_pagar}")

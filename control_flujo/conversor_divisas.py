
# Crear un conversor de divisas que permita convertir una cantidad
# entre USD, EUR y MXN según la divisa de origen seleccionada.

cantidad = int(input("Ingrese cantidad: "))

print("Elige divisa usd, eur, mxn")
divisa_origen = input("Ingresa la divisa de origen: ")

if divisa_origen == "usd":
    eur = cantidad * 0.95
    mxn = eur * 21.36
    print(f"eur: {eur}, mxn: {mxn}")

elif divisa_origen == "eur":
    mxn = cantidad * 21.36
    usd = cantidad / 0.95
    print(f"usd: {usd}, mxn: {mxn}")

elif divisa_origen == "mxn":
    eur = cantidad / 21.36
    usd = cantidad / 20.38
    print(f"usd: {usd}, eur: {eur}")

else:
    print("Divisa no valida")
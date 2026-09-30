
# Crear un programa que determine si el cliente pagó justo, debe dinero
# o tiene vuelto, permitiendo procesar múltiples clientes hasta ingresar "fin".

while True:

    monto_dado = input("Ingrese monto del cliente: ")
    if monto_dado.lower() == "fin":
        print("Programa Finalizado")
        break

    total_cuenta = input("Cuanto costo todo: ")
    if total_cuenta.lower() == "fin":
        print("Programa Finalizado")
        break

    monto_dado = int(monto_dado)
    total_cuenta = int(total_cuenta)

    if monto_dado == total_cuenta:
        print("Pago lo justo, no tiene vuelto.")

    elif monto_dado < total_cuenta:
        debe = monto_dado - total_cuenta
        print(f"El cliente debe {abs(debe)}")

    elif monto_dado > total_cuenta:
        vuelto = monto_dado - total_cuenta
        print(f"El vuelto es {vuelto}")
    else: 
        print("No aplica")
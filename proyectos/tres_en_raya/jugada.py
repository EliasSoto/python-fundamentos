from tablero import verificar_posicion, imprimir_tablero

# Asigna el valor del turno actual
def asignar_valor(tablero: list, posicion: list, valor: str):

    # Hasta que la posición no este ocupada pide una nueva
    while verificar_posicion(tablero, posicion):
        imprimir_tablero(tablero)
        print("Posición ocupada")
        posicion = pedir_posicion()

    # Asigna el valor al tablero en la posición validada
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i == posicion[0] and j == posicion[1]:
                tablero[i][j] = f"[{valor.upper()}]"

    # Retornamos el tablero despues de la modificación 
    # Tambien la posición para despues validar si el turno ganó
    return tablero, posicion


# Pedir la posición del valor a ingresar
def pedir_posicion():
    posicion = []
    posicion.append(int(input("Ingrese posición i: ")))
    posicion.append(int(input("Ingrese posición j: ")))

    while posicion[0] < 0 or posicion[0] > 2 or posicion[1] < 0 or posicion[1] > 2:
        print("Posición inválida")

        posicion[0] = int(input("Ingrese posición i: "))
        posicion[1] = int(input("Ingrese posición j: "))

    return posicion


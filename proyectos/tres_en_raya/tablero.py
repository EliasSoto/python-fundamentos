
# Función para imprimir el tablero
def imprimir_tablero(tablero: list):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()

# Verificar si la posición esta ocupada
def verificar_posicion(tablero: list, posicion: list):
    if tablero[posicion[0]][posicion[1]] != "[ ]":
        return True
    return False


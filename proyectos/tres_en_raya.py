# Tres en línea
# Contexto

# Desarrollar un juego de Gato para dos jugadores que se ejecute por consola. 
# El tablero debe representarse mediante una matriz de 3×3 y los jugadores 
# deben alternar sus turnos hasta que exista un ganador o empate.

# El programa debe permitir
# Mostrar el tablero.
# Identificar a los dos jugadores.
# Alternar los turnos.
# Solicitar la posición donde cada jugador quiere jugar.
# Validar que la posición exista.
# Impedir jugar sobre una posición ocupada.
# Actualizar el tablero después de cada jugada.
# Detectar tres símbolos consecutivos:
# horizontalmente
# verticalmente
# diagonalmente
# Detectar un empate (Hay empate cuando el tablero está lleno y ningún jugador consiguió 3 en línea.)
# Informar el resultado final.
# Permitir comenzar una nueva partida.

def imprimir_tablero(tablero: list):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


def asignar_valor(tablero: list, posicion: list, valor: str):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i == posicion[0] and j == posicion[1]:
                tablero[i][j] = f"[{valor.upper()}]"


def verificar_posicion(tablero: list, posicion: list):
    if tablero[posicion[0]][posicion[1]] != "[ ]":
        return True
    return False


def verificar_ganador(tablero: list, posicion: list):
    fila_gana = True
    columna_gana = True
    diagonal_principal_gana = True
    diagonal_secundaria_gana = True
    jugada = tablero[posicion[0]][posicion[1]]

    # Verificar la fila
    for j in range(len(tablero[posicion[0]])):
        if j != posicion[1]:
            if tablero[posicion[0]][j] != jugada:
                fila_gana = False
                break
    
    # Verificar la columna
    for i in range(len(tablero)):
        if i != posicion[0]:
            if tablero[i][posicion[1]] != jugada:
                columna_gana = False
                break

    # Verificar diagonal principal
    for i in range(len(tablero)):
        if i != posicion[0]:
            if tablero[i][i] != jugada:
                diagonal_principal_gana = False
                break

    # Verificar diagonal secundaria
    j_prima = len(tablero[0]) - 1
    for i in range(len(tablero)):
        if i != posicion[0]:
            if tablero[i][j_prima] != jugada:
                diagonal_secundaria_gana = False
                break
        j_prima -= 1
    
    if columna_gana:
        return True
    if fila_gana:
        return True
    if diagonal_principal_gana:
        return True
    if diagonal_secundaria_gana:
        return True
   
    return False






tablero = [
    ["[ ]", "[X]", "[X]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"]
]



# asignar_valor(tablero, [1,2], "X")
# imprimir_tablero(tablero)


# print(verificar_posicion(tablero, [1,2]))
# imprimir_tablero(tablero)

# asignar_valor(tablero, [2,2], "x")
# posicion = [0,0]
# posicion = [1,1]


posicion = [2,0]
asignar_valor(tablero,posicion, "X")
print(verificar_ganador(tablero, posicion))

imprimir_tablero(tablero)
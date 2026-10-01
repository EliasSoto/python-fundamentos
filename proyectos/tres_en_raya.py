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


# Función para imprimir el tablero
def imprimir_tablero(tablero: list):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


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


# Verificar si la posición esta ocupada
def verificar_posicion(tablero: list, posicion: list):
    if tablero[posicion[0]][posicion[1]] != "[ ]":
        return True
    return False


# Verificamos si la posición ingresada hace que este gane 
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

# Si el tablero esta lleno se considera un empate entonces devolvemos True
def verificar_empate(tablero: list):
    for fila in tablero:
        for elemento in fila:
            if elemento == "[ ]":
                return False
    return True  


# Juego
tablero = [
    ["[X]", "[O]", "[X]"],
    ["[X]", "[O]", "[O]"],
    ["[O]", "[ ]", "[ ]"]
]

turno = "X"

while True:
    imprimir_tablero(tablero)
    posicion = pedir_posicion()
    tablero, posicion = asignar_valor(tablero,posicion, turno)

    if verificar_ganador(tablero, posicion):
        imprimir_tablero(tablero)
        print(f"Ganó {turno}")
        break

    if verificar_empate(tablero):
        imprimir_tablero(tablero)
        print("Hay un empate")
        break

    if turno == "X":
        turno = "O"
    else:
        turno = "X"
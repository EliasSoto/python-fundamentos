
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



# Máximo de una matriz recursivamente

matriz = [
    [4, 8, 2],
    [15, 3, 7],
    [6, 12, 9]
]

def mayor_matriz(matriz, fila, columna, mayor):

    if matriz[fila][columna] > mayor:
        mayor = matriz[fila][columna]

    if columna == len(matriz[fila]) - 1 and fila == len(matriz) - 1:
        return mayor
    
    if columna < len(matriz[fila]) - 1:
        return mayor_matriz(matriz, fila, columna + 1, mayor)

    elif fila < len(matriz) - 1:
        columna = 0
        return mayor_matriz(matriz, fila + 1, columna, mayor)

resultado = mayor_matriz(matriz, 0, 0, 0)

print(resultado)
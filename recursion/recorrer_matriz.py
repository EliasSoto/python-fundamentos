
# Recorrer una matriz recursivamente

def recorrer(matriz, fila, columna):
    print(matriz[fila][columna])

    if columna == len(matriz[fila]) - 1 and fila == len(matriz) - 1:
        return 
    
    if columna < len(matriz[fila]) - 1:
        recorrer(matriz, fila, columna + 1)
        
    elif fila < len(matriz) - 1:
        columna = 0
        recorrer(matriz, fila + 1, columna)
    
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

recorrer(matriz, 0, 0)
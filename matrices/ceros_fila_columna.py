
# Si una celda contiene un 0, convertir en 0 toda su fila y toda su columna

matriz = [
    [1,2,3],
    [4,1,0],
    [7,8,3]
]

columna_cero = 0
fila_cero = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 0:
            columna_cero = j
            fila_cero = i
            break

for i in range(len(matriz[fila_cero])):
    matriz[i][columna_cero] = 0

for j in range(len(matriz[columna_cero])):
    matriz[fila_cero][j] = 0

for fila in matriz:
    print(fila)
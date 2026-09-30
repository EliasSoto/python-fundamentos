
# Si una columna contiene un 0, convertir toda esa columna en 0

matriz = [
    [1,2,3],
    [4,0,6],
    [7,8,9]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 0:
            columa_cero = j
            break

for i in range(len(matriz)):
    matriz[i][columa_cero] = 0

for fila in matriz:
    print(fila)

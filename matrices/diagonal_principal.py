
# Cambiar únicamente la diagonal principal por 0

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matriz[i][j] = 0

for fila in matriz:
    print(fila)

# Si un elemento es negativo, convertir también en 0 a sus vecinos

matriz = [
    [1,2,3],
    [4,-5,6],
    [7,8,9]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < 0:
            if j+1 < len(matriz[i]):
                matriz[i][j+1] = 0
            if j-1 >= 0:
                matriz[i][j-1] = 0
            if i+1 < len(matriz):
                matriz[i+1][j] = 0
            if i-1 >= 0:
                matriz[i-1][j] = 0

for fila in matriz:
    print(fila) 
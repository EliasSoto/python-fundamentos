
# Reflejar respecto de la diagonal principal

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matriz)):
    for j in range(0,i):
        primero = matriz[i][j]
        segundo = matriz[j][i]

        matriz[i][j] = segundo
        matriz[j][i] = primero

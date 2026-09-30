
# Reflejar respecto de la diagonal secundaria

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

j_prima = len(matriz[0]) - 1 
num = len(matriz) - 1

for i in range(len(matriz)):
    i_prima = num
    for j in range(0, j_prima):
        primero = matriz[i][j]
        segundo = matriz[i_prima][j_prima]

        matriz[i][j] = segundo
        matriz[i_prima][j_prima] = primero
        i_prima -=1
    j_prima -=1

for fila in matriz:
    print(fila)
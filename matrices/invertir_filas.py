
# Invertir cada fila

matriz = [
    [1,2,3],
    [4,5,6]
]

for i in range(len(matriz)):
    j_prima = len(matriz[i]) - 1

    for j in range(len(matriz[i])):
        if j < j_prima:
            primer = matriz[i][j]  
            segundo = matriz[i][j_prima]

            matriz[i][j] = segundo
            matriz[i][j_prima] = primer

        j_prima -= 1

for fila in matriz:
    print(fila)

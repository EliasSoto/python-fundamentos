
# Verificar si una matriz es triangular inferior

matriz = [
    [1,0,0],
    [4,5,0],
    [7,8,9]
]

triangular_inferior = True

for i in range(len(matriz)):
    for j in range(i+1, len(matriz[0])):
        if matriz[i][j] != 0:
            triangular_inferior = False

if triangular_inferior:
    print("La matriz es triangular inferior.")

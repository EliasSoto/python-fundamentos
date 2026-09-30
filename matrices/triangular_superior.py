
# Verificar si una matriz es triangular superior

matriz = [
    [1,2,3],
    [0,5,6],
    [0,0,9]
]

triangular_superior = True

for i in range(len(matriz)):
    for j in range(i):
        if matriz[i][j] != 0:
            triangular_superior = False

if triangular_superior:
    print("La matriz es triangular superior.")

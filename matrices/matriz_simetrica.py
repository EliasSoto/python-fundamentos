
# Verificar si una matriz es simétrica

matriz = [
    [1,2,3],
    [2,5,6],
    [3,6,9]
]

matriz_simetrica = True

for i in range(len(matriz)):
    for j in range(i):
        if matriz[i][j] != matriz[j][i]:
            matriz_simetrica = False

if matriz_simetrica:
    print("La matriz es simetrica.")
else:
    print("No.")
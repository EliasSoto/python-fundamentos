
# Verificar si una matriz es identidad

matriz = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
identidad = True

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            if matriz[i][j] != 1:
                identidad = False
        else:
            if matriz[i][j] != 0:
                identidad = False

if identidad:
    print("La matriz es identidad.")

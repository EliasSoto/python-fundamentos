
# Rotar la matriz 270° hacia la derecha

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz_270 = []

for j in reversed(range(len(matriz[0]))):
    lista_aux = []
    for i in range(len(matriz)):
        lista_aux.append(matriz[i][j])
    matriz_270.append(lista_aux)

for fila in matriz_270:
    print(fila)

# Transponer una matriz

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz_transpuesta = []

for j in range(len(matriz[0])):
    lista_aux = []
    for i in range(len(matriz)):
        lista_aux.append(matriz[i][j])
    matriz_transpuesta.append(lista_aux)

for fila in matriz_transpuesta:
    print(fila)
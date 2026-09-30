
# Rotar 180°

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz_180 = []

for i in reversed(range(len(matriz))):
    lista_aux = []
    for j in reversed(range(len(matriz[i]))):
        lista_aux.append(matriz[i][j])
    matriz_180.append(lista_aux)

for lista in matriz_180:
    print(lista)
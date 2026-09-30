
# Modificar una matriz usando posiciones previamente encontradas

matriz = [
    [5,2,3],
    [4,5,6],
    [7,8,5]
]

buscar = 5
nuevo = 100
lista_buscados = []

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == buscar:
            lista_buscados.append((i,j))


for i,j in lista_buscados:
    matriz[i][j] = nuevo

for fila in matriz:
    print(fila)
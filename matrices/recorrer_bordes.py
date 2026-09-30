
# Recorrido por bordes

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

maximo = len(matriz) - 1

#arriba
for j in range(len(matriz[0])):
    print(matriz[0][j])

#derecha
for i in range(1,len(matriz)):
    print(matriz[i][maximo])

#abajo
for j in reversed(range(len(matriz[0])-1)):
    print(matriz[maximo][j])

#izquierda
for i in reversed(range(1, len(matriz)-1)):
    print(matriz[i][0])
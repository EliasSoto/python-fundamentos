
# Intercambiar la primera y la última columna

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

ultima_columna = len(matriz[0]) - 1

for i in range(len(matriz)):
    primer = matriz[i][0]
    ultimo = matriz[i][ultima_columna]

    matriz[i][0] = ultimo
    matriz[i][ultima_columna] = primer

for fila in matriz:
    print(fila)
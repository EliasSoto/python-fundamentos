
# Imprimir todos los elementos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Forma 1
for i in range(len(matriz)): 
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()

# Forma 2
for fila in matriz:
    for numero in fila:
        print(numero, end="")
    print()
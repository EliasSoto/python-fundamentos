
# Intercambiar la primera y la última fila

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

ultima_fila = len(matriz) - 1

for j in range(len(matriz[0])):
    primer = matriz[0][j]
    ultima = matriz[ultima_fila][j]

    matriz[0][j] = ultima
    matriz[ultima_fila][j] = primer

for fila in matriz:
    print(fila)
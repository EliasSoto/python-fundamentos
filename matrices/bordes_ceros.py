
# Cambiar únicamente el borde por 0

matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

ultima_fila = len(matriz)-1
ultima_columna = len(matriz[0])-1

#COLUMNAS
for i in range(len(matriz)):        
    matriz[i][0] = 0
    matriz[i][ultima_columna] = 0

#FILAS
for j in range(len(matriz)):
    matriz[0][j] = 0
    matriz[ultima_fila][j] = 0

# Imprimir Matriz
for fila in matriz:
    print(fila)
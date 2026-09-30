
# Cambiar únicamente la diagonal secundaria por -1

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

j_columna = len(matriz[0]) - 1

for i in range(len(matriz)):
    matriz[i][j_columna] = -1
    j_columna -= 1
    
for fila in matriz: 
    print(fila)
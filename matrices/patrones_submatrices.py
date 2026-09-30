
# Buscar patrones dentro de submatrices

matriz = [
    [0,1,1,0],
    [2,2,1,5],
    [3,3,1,1],
    [6,2,1,1]
]

patron = [
    [1,1],
    [1,1]
]

existe_patron = False

for i in range(len(matriz) - 1):
    for j in range(len(matriz[i])-1):
        if (matriz[i][j] == patron[0][0] and
            matriz[i][j+1] == patron[0][1] and
            matriz[i+1][j] == patron[1][0] and
            matriz[i+1][j+1] == patron[1][1]):

            existe_patron = True

if existe_patron:
    print("Existe el patron definido.")
else:
    print("No esta el patron definido.")
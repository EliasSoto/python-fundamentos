
# Verificar restricciones de una matriz
# Una matriz es válida si ningún 0 tiene otro 0 inmediatamente a su derecha.

matriz = [
    [1,0,3],
    [0,2,0],
    [4,1,0]
]

valida = True

for i in range(len(matriz)):
    longitud_fila = len(matriz[i])

    for j in range(len(matriz[i])):
        if j + 1 < longitud_fila :
            if matriz[i][j] == 0 and matriz[i][j+1] == 0:
                valida = False 

if valida:
    print("Sí")
else:
    print("No")
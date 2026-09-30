
# Transponer una matriz sin crear otra matriz
# Transponer una matriz = reflejarla respecto a la diagonal principal

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# en python puedes hacer intercambio asi
# matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

for i in range(len(matriz)):
    for j in range(i):
        primer_valor = matriz[i][j]
        segundo_valor = matriz[j][i]

        matriz[i][j] = segundo_valor
        matriz[j][i] = primer_valor
        
for fila in matriz:
    print(fila)
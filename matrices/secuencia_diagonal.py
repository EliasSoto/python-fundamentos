
# Buscar una secuencia diagonal principal

matriz = [
    [1,4,7],
    [8,2,5],
    [9,6,3]
]

secuencia = [1,2,3]
longitud = len(secuencia)
contador = 0
hay_secuencia = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            if matriz[i][j] == secuencia[0]:
                contador = 1
            elif matriz[i][j] == secuencia[contador]:
                contador += 1
                if contador == longitud:
                    hay_secuencia = True
                    contador = 0
                    break
            else:
                contador = 0
    if hay_secuencia:
        break

            
print(hay_secuencia)
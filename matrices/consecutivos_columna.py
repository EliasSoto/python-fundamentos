
# Buscar dos números consecutivos en una columna

matriz = [
    [1,2],
    [1,7],
    [1,9]
]

secuencia = [1,2]
contador = 0
hay_secolumna = False
largo = len(secuencia)

for j in range(len(matriz[0])):
    contador = 0
    for i in range(len(matriz)):

        if matriz[i][j] == secuencia[0]:
            contador = 1
        elif matriz[i][j] == secuencia[contador]:
            contador += 1
            if contador == largo:
                hay_secolumna = True
                contador = 0
                break
        else: 
            contador = 0
    if hay_secolumna:
        break

print(hay_secolumna)
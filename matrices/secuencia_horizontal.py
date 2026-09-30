
# Buscar una secuencia horizontal

matriz = [
    [1,1,2,2],
    [1,2,2,3],
    [1,2,3,5]
]

secuencia = [1,2,3,4]
contador = 0
hay_sec = False
largo = len(secuencia)

for fila in matriz:
    contador = 0

    for numero in fila:
        if numero == secuencia[contador]:
                contador += 1
                if contador == largo:
                    hay_sec = True
                    contador = 0
                    break
        elif numero == secuencia[0]:
            contador = 1
        else:
            contador = 0

    if hay_sec:
        break

print(hay_sec)
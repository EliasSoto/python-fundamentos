
# Recorrido en espiral

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

limite_izquierdo = 0
limite_derecho = len(matriz[0]) - 1 
limite_superior = 0
limite_inferior = len(matriz) - 1 

while limite_izquierdo <= limite_derecho and limite_superior <= limite_inferior:

    for j in range(limite_izquierdo, limite_derecho + 1):
        print(matriz[limite_superior][j])

    for i in range(limite_superior + 1, limite_inferior + 1):
        print(matriz[i][limite_derecho])

    if limite_superior < limite_inferior:
        for j in reversed(range(limite_izquierdo, limite_derecho)):
            print(matriz[limite_inferior][j])

    if limite_izquierdo < limite_derecho:
        for i in reversed(range(limite_superior + 1, limite_inferior)):
            print(matriz[i][limite_izquierdo])

    limite_izquierdo += 1
    limite_derecho -= 1 
    limite_superior += 1
    limite_inferior -= 1 
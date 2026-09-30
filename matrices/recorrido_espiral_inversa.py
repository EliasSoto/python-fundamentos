
# Recorrido en espiral inverso

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


limite_superior = 0
limite_izquierdo = 0 
limite_inferior = len(matriz) - 1
limite_derecho = len(matriz[0]) - 1

while limite_izquierdo <= limite_derecho and limite_superior <= limite_inferior:
        
    for j in reversed(range(limite_izquierdo, limite_derecho+1)):
        print(matriz[limite_inferior][j])

    for i in reversed(range(limite_superior + 1, limite_inferior)):
        print(matriz[i][limite_izquierdo])

    if limite_superior < limite_inferior:
        for j in range(limite_izquierdo, limite_derecho + 1):
            print(matriz[limite_superior][j])

    if limite_izquierdo < limite_derecho:
        for i in range(limite_superior + 1, limite_inferior):
            print(matriz[i][limite_derecho])

    limite_superior += 1
    limite_izquierdo += 1
    limite_inferior -= 1
    limite_derecho -= 1
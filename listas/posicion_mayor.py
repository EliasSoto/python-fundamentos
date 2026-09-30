
#Imprime la posición donde está el número más grande.

numeros = [4, 15, 8, 21, 7, 13]
mayor = numeros[0]

for i in range(len(numeros)):
    if numeros[i] >= mayor:
        mayor = numeros[i]
        posicion_mayor = i

print(f"El mayor es {mayor} y esta en la posición {posicion_mayor + 1}")
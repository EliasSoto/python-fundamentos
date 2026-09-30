
#Calcula el promedio de la lista.

numeros = [8, 6, 10, 4, 12]
suma = 0

for numero in numeros:
    suma += numero
promedio = suma/len(numeros)

print(f"Promedio {promedio}")
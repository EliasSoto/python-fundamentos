
#Mayor y menor de una lista

numeros = [12, 5, 18, 3, 9, 20, 7]
mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero

print(f"El mayor es: {mayor} y el menor: {menor}")


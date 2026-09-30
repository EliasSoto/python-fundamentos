
# Mover los ceros al final

numeros = [0,4,0,1,7,0,2]
destino = 0

for numero in numeros:
    if numero != 0:
        numeros[destino] = numero
        destino += 1

for i, _ in enumerate(numeros[destino:]):
        numeros[i+destino] = 0

print(f"Ceros al final", numeros)



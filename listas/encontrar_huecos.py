
# Encontrar todos los huecos
numeros = [1,2,5,6,10]

numeros.sort()
esperado = numeros[0]
faltantes = []

for numero in numeros:
    
    if numero != esperado:
        # El extend agrega elementos de otra colección, el append un cosa.
        faltantes.extend(list(range(esperado, numero)))
        esperado = numero
    
    esperado += 1

print(faltantes)


print(list(range(1,4)))
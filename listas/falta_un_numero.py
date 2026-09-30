
# Falta exactamente un número

numeros = [1,2,3,4,6,7,8]
esperado = numeros[0]

for numero in numeros:
    if numero != esperado:
        print(f"Falta {esperado}")
        break
    esperado += 1
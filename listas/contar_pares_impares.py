
# Cuenta cuántos números pares e impares hay en el arreglo.

numeros = [3, 8, 5, 10, 7, 12, 6]
pares = []
impares = []
contador_pares = 0
contador_impares = 0 

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) 
        contador_pares += 1
    else:
        impares.append(numero)
        contador_impares += 1

print(f"Hay {contador_pares} pares que son {pares}")
print(f"Hay {contador_impares} impares que son {impares}")
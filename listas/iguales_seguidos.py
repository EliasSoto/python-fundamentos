
# ¿Cuál es la mayor cantidad de números iguales seguidos?

numeros = [1,1,2,2,2,3,4,4,4,4]
numero_anterior = numeros[0]
contador = 1
mayor_racha = 0

for numero in numeros[1:]:

    if numero_anterior == numero:
        contador += 1
    else:
        if mayor_racha < contador:
            mayor_racha = contador
        numero_anterior = numero
        contador = 1

if mayor_racha < contador:
            mayor_racha = contador

print(f"La racha mas larga es de: {mayor_racha}")

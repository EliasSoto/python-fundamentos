
# Mayor diferencia

# Estoy parado en la posición actual, ¿qué información del pasado 
# necesito para tomar la mejor decisión ahora?

numeros = [7,1,5,3,6,4]
numeros = [5, 1, 4, 0, 3]
menor_visto = numeros[0]
resta_actual = numeros[0]
mayor_resta = 0

for numero in numeros:
    resta_actual = numero - menor_visto

    if numero < menor_visto:
        menor_visto = numero

    if mayor_resta < resta_actual:
        mayor_resta = resta_actual

print(mayor_resta)
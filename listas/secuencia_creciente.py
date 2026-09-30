
# Secuencia creciente más larga

numeros = [1,2,3,1,2,3,4,5,1]
numero_anterior = numeros[0]
longitud = 1
mayor_racha = 0

for numero in numeros[1:]:
    if numero < numero_anterior:
        longitud = 1
    else: 
        longitud += 1
        if longitud > mayor_racha:
                mayor_racha = longitud

    numero_anterior = numero

print(mayor_racha)

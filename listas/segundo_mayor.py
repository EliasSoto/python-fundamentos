
#Encontrar el segundo mayor

numeros = [18, 7, 25, 12, 30, 21]
mayor = numeros[0]
seg_mayor = numeros[0]

for numero in numeros:

    if numero > mayor:
        seg_mayor = mayor
        mayor = numero
    elif numero > seg_mayor and numero < mayor:
        seg_mayor = numero

print(f"El segundo mayor es: {seg_mayor}")
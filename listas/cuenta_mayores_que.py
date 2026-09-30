
#Cuenta cuántos números son mayores que 10 y negativos

numeros = [8, 15, 3,-19, 20, 11, 9,  12]
mayor_que = 10
contador_mayor_que = 0
mayores = []
negativos = []
cont_negativos = 0

for numero in numeros:
    if numero > mayor_que:
        mayores.append(numero)
        contador_mayor_que += 1
    elif numero < 0:
        negativos.append(numero)
        cont_negativos += 1

print(f"Hay {contador_mayor_que} numeros mayores que {mayor_que} que son {mayores}")
print(f"Hay {cont_negativos} numeros negativos que son {negativos}")
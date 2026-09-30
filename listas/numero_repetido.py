
#Encuentra el primer número que aparece dos veces.

numeros = [4,8,2,5,8,1,2]
lista_auxiliar = []

for numero in numeros:
    if numero in lista_auxiliar:
        print(f"El primer numero que se repite es {numero}")
        break
    lista_auxiliar.append(numero)
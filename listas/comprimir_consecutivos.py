
# Comprimir consecutivos

numeros = [1, 2, 2, 2, 3, 2]
numero_anterior = numeros[0]
contador = 1
lista_tuple = []
lista = [numero_anterior, contador]

for i, numero in enumerate(numeros[1:]):
    if numero == numero_anterior:
        contador += 1
        lista = [numero, contador]
    else:
        lista_tuple.append(tuple(lista))
        numero_anterior = numero
        contador = 1
        lista = [numero, contador]

lista_tuple.append(tuple(lista))
print(lista_tuple)

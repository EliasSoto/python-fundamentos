
# Sumar elementos de una lista recursivamente

def sumar_lista(lista, indice):
    if indice == len(lista):
        return 0
    else:
        return lista[indice] + sumar_lista(lista, indice + 1)

numeros = [2,8,3]

resultado = sumar_lista(numeros, 0)

print(resultado)
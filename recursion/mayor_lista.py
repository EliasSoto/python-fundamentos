
# Encontrar el mayor de una lista recursivamente

numeros = [7, 2, 15, 4, 9, 11]

def mayor(lista, indice, mayor_actual):

    if indice == len(lista) - 1:
        return mayor_actual
    
    if lista[indice] > mayor_actual:
        mayor_actual = lista[indice]  
   
    return mayor(lista, indice + 1, mayor_actual)

resultado = mayor(numeros, 0, 0)

print(resultado)
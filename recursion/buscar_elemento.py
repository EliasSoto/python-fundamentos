
# Buscar un elemento recursivamente

def buscar(lista, objetivo, indice):
    if indice == len(lista):
        return f"No se encontró, el numero {objetivo}."
    else:
        if lista[indice] == objetivo:
            return f"El elemento si está, el indice es {indice}"
        return buscar(lista, objetivo, indice + 1)



numeros = [8, 3, 12, 5, 7]


print(buscar(numeros, 12, 0))
print(buscar(numeros, 20, 0))
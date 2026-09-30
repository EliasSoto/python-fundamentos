
# Detectar palíndromo recursivamente

def es_palindromo(palabra, inicio, fin):
    if inicio >= fin:
        return True
    if palabra[inicio] != palabra[fin]:
        return False

    return es_palindromo(palabra, inicio + 1, fin - 1)

palabra = "reconoce"
print(es_palindromo(palabra, 0, len(palabra) - 1))





# Invertir un string recursivamente

def invertir_texto(texto, indice):
    if indice == len(texto):
        return ""
    else: 
        return invertir_texto(texto, indice + 1) + texto[indice]

texto = "python"

print(invertir_texto(texto, 0))

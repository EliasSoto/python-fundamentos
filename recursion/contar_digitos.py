
# Contar dígitos recursivamente

def contar_digitos(n):

    if n == 0:
        return 0
    else:
        return 1 + contar_digitos(n//10)
    
resultado = contar_digitos(58321)

print(resultado)


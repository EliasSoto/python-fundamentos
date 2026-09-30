
# Suma de dígitos recursivamente

def suma_digitos(n):
    if n == 0:
        return 0
    else: 
        return n % 10 + suma_digitos(n//10)

resultado = suma_digitos(5832)

print(resultado)
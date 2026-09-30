
# Factorial recursivo

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

resultado = factorial(5)

print(resultado)
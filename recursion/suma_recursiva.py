
# Suma recursiva

def suma_n(n):
    if n == 0:  
        return 0 
    else:
        return n + suma_n(n-1) # A la proxima llamada de la función le paso n-1
        
resultado = suma_n(5)
print(resultado)
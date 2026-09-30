
# Potencia recursiva

def potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base*potencia(base, exponente - 1)

resultado = potencia(5, 3)

print(resultado)
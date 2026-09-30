
# Cuenta cuántas veces un número es igual al siguiente

numeros = [2, 2, 5, 7, 7, 7, 1, 4, 5]
numero_anterior = False
contador = 1
dicc = {}

for numero in numeros: 

    if (numero_anterior == False):
        contador = 1  

    elif (numero_anterior != numero):
        dicc[numero_anterior] = contador
        contador = 1
        
    else:
        contador += 1
        dicc[numero_anterior] = contador

    numero_anterior = numero

dicc[numero_anterior] = contador

print(dicc)


# Dos números que sumen 15
# La logica seria cuantos me falta para llegar y si ya lo he visto

numeros = [1,2,3,4,11]
vistos = set()
complemento = 0
suma = 15

for numero in numeros:

    complemento = suma - numero
    if complemento in vistos:
        print(f"{numero} + {complemento} suman {suma}")
        break

    vistos.add(numero)
else:
    print("No hay dos numeros que sumen esa cantidad")  

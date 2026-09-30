
# Contar cuántas veces aparece cada número

matriz = [
    [1,2,2],
    [3,1,4],
    [2,4,1]
]
contador = 0
veces_numero = {}

for fila in matriz:
    for numero in fila:
        if numero not in veces_numero:
            veces_numero[numero] = 1
        else:
            veces_numero[numero] += 1

print(veces_numero)
        

#Sacar el 3er mayor

numeros = [18, 7, 25, 12, 30, 21, 2]
numeros = [
    42, 15, 87, 3, 91, 56, 24, 78, 12, 99,
    67, 5, 31, 88, 73, 18, 94, 27, 61, 45,
    82, 11, 96, 39, 53, 7, 84, 65, 22, 100
]
mayor = float("-inf")
seg_mayor = float("-inf")
ter_mayor = float("-inf")

for numero in numeros:

    if numero > mayor:
        ter_mayor = seg_mayor
        seg_mayor = mayor
        mayor = numero
    
    elif numero > seg_mayor and numero < mayor:
        ter_mayor = seg_mayor
        seg_mayor = numero

    elif numero > ter_mayor and numero < seg_mayor:
        ter_mayor = numero

print(f"Encontrar el tercer mayor: {ter_mayor}")

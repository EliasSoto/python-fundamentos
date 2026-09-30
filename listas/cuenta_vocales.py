
# Cuenta cuántas vocales tiene una cadena

texto = "programacion"
vocales = ["a","e", "i", "o", "u"]
contador = 0

for char in texto:
    if char in vocales:
        contador += 1

print(f"{texto} tiene {contador} vocales")
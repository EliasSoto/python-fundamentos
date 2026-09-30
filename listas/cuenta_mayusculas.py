
#Cuenta cuántas letras mayúsculas hay

texto = "HoLa MuNdO PERO   "
contador = 0

for char in texto:
    if char == " ":
        contador = contador

    elif char == char.upper():
        contador += 1

print(f"Hay {contador} mayusculas en el texto")

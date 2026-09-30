
# Validar que un tweet no esté vacío y que no supere los 20 caracteres.
# Comparar una solución propia con una solución más idiomática de Python.

tweet = input("ingrese un tweet de maximo 20 caracteres: ")

cantidad_caracteres = len(tweet)
print(cantidad_caracteres)

if cantidad_caracteres == 0:
    print("No puedes publicar un tweet vacio")
elif cantidad_caracteres <= 20:
    print("Su tweet ha sido publicado")
else:
    print("Su tweet sobrepasa el limite de 20 caracteres")



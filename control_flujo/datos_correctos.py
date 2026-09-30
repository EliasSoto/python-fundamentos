
# Solicitar un nombre y apellido válidos utilizando un while,
# repitiendo la solicitud hasta que ambos datos sean ingresados correctamente.

while True:
    nombre = (input("ingrese su nombre")).strip().capitalize()
    apellido = (input("ingrese su apellido")).strip().capitalize()

    if not (nombre and apellido): # el if evalua si es true y luego pasa a imprimir si es false no lo ejecuta
        print("vuelve a escribir tu nombre y apellido")
    else:
        break

print(f"nombre completo: {nombre} {apellido}")
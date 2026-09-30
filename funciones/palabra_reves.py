
#Función para retornar una palabra al reves
def palabra_reves(palabra: str):
    texto_reves = ""
    for char in palabra:
        texto_reves = char + texto_reves 

    return(texto_reves)



palabra = "hola"

print(palabra_reves(palabra))
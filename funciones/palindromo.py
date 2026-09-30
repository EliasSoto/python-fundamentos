
# Funcion para ver si una palabra es palindroma
def es_palindroma(palabra: str):
    palindroma = ""
    palabra = palabra.lower().strip()

    # Para recorrer un elemento en reversa solo ocupa reversed
    for caracter in reversed(palabra):
        palindroma += caracter

    if palabra == palindroma:
        print(f"La palabra es palindroma: {palabra} en reversa es {palindroma}")
    else:
        print(f"No es palindroma: {palabra} en reversa es {palindroma}")

es_palindroma(" RecoNOcer ")



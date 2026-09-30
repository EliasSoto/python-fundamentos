
# Conversor de Unidades de Tiempo
# minuto,hora,dı́a,mes(30dı́as),año(365días)

# Función para convertir unidades a segundos.
def a_segundos(cantidad: int, unidad: str):

    unidad = unidad.lower().strip()
    minutos_s = 60
    hora_s = 60*minutos_s
    dias_s = 24*hora_s
    mes_s = 30*dias_s
    anho_s = 365*dias_s

    if unidad == "minuto":
        conversion = cantidad * minutos_s

    elif unidad == "hora":
        conversion = cantidad * hora_s

    elif unidad == "dia":
        conversion = cantidad * dias_s
    
    elif unidad == "mes":
        conversion = cantidad * mes_s

    elif unidad == "anho":
        conversion = cantidad * anho_s
    else:
        print("Su opcion de unidad no esta.")
        return 0
    
    return conversion

# Función para convertir de segundos a una unidad.
def de_segundos(cantidad_segundos: int, unidad: str):

    unidad = unidad.lower().strip()
    minutos_s = 60
    hora_s = 60*minutos_s
    dias_s = 24*hora_s
    mes_s = 30*dias_s
    anho_s = 365*dias_s

    if unidad == "minuto":
        conversion = cantidad_segundos / minutos_s

    elif unidad == "hora":
        conversion = cantidad_segundos / hora_s

    elif unidad == "dia":
        conversion = cantidad_segundos / dias_s
    
    elif unidad == "mes":
        conversion = cantidad_segundos / mes_s

    elif unidad == "anho":
        conversion = cantidad_segundos / anho_s
    else:
        print("Su opcion de unidad no esta.")
        return 0
    
    return conversion  

# Crear una función llamada convertir_tiempo que utilice las dos funciones anteriores.
# Ejemplo: Quiero convertir 2 días a horas.

def convertir_tiempo(cantidad: int, unidad_inicial: str, unidad_final: str):

    conversion_s = a_segundos(cantidad, unidad_inicial)
    conversion_unidad_final = de_segundos(conversion_s, unidad_final)
    print(f"Tu conversion de {cantidad} {unidad_inicial} es: {conversion_unidad_final} {unidad_final}")

    return conversion_unidad_final


# Aplicar la Función
convertir_tiempo(24,"hora", "dia")




import random

# Función para lanzar un dado n lanzamientos y dar porcentajes
def lanzar_dado(lanzamientos: int = 0):
    veces_1 = 0
    veces_2 = 0
    veces_3 = 0
    veces_4 = 0
    veces_5 = 0
    veces_6 = 0

    if lanzamientos <= 0:
        return "Ingresa un numero del 1 en adelante."
    
    for _ in range(lanzamientos):
        cara_dado = random.randint(1,6)
        
        if cara_dado == 1:
            veces_1 += 1
        elif cara_dado == 2:
            veces_2 += 1
        elif cara_dado == 3:
            veces_3 += 1
        elif cara_dado == 4:
            veces_4 += 1
        elif cara_dado == 5:
            veces_5 += 1
        elif cara_dado == 6:
            veces_6 += 1

    porcentaje_1 = veces_1/lanzamientos*100
    porcentaje_2 = veces_2/lanzamientos*100
    porcentaje_3 = veces_3/lanzamientos*100
    porcentaje_4 = veces_4/lanzamientos*100
    porcentaje_5 = veces_5/lanzamientos*100
    porcentaje_6 = veces_6/lanzamientos*100

    mensaje = f"""
    Veces que salio y porcentajes:\n
    Cara 1: {veces_1} Porcentaje: {porcentaje_1}%\n
    Cara 2: {veces_2} Porcentaje: {porcentaje_2}%\n
    Cara 3: {veces_3} Porcentaje: {porcentaje_3}%\n
    Cara 4: {veces_4} Porcentaje: {porcentaje_4}%\n
    Cara 5: {veces_5} Porcentaje: {porcentaje_5}%\n
    Cara 6: {veces_6} Porcentaje: {porcentaje_6}%\n
    """
    return mensaje

print(lanzar_dado(10000))

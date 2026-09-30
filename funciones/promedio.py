
# Función para calcular promedio
def calcular_promedio(*numeros: int):
    
    if not numeros:
        return "No haz ingresado ningun número."
    
    suma = 0
    for numero in numeros:
        suma += numero
        
    promedio = suma/(len(numeros))

    # Puedes retornar todos los tipos de datos
    return f"El promedio es: {promedio}"

print(calcular_promedio(0))
print(calcular_promedio(1,2,3,4,6,7,8,10))

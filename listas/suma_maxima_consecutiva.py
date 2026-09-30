
# Máxima suma consecutiva

numeros = [-2,1,-3,4,-1,2,1,-5,4]

suma_actual = numeros[0]
mejor_suma = numeros[0]

for numero in numeros[1:]:
    suma_actual += numero 

    if suma_actual < numero:
        suma_actual = numero

    if suma_actual >= mejor_suma:
        mejor_suma = suma_actual
    
print(mejor_suma)   

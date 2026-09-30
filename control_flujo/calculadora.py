
# Crear una calculadora con un ciclo while que permita realizar
# operaciones básicas hasta que el usuario escriba "salir".

print("Bienvenido a la calculadora")
print("las operaciones son sum, res, mul, div, salir")

num1 = float(input("ingresa un numero"))
operacion = ""

while True:
    
    operacion = str(input("ingrese operacion"))
    if operacion.lower() == "salir":
        break

    num2 = float(input("ingrese segundo numero"))
    
    if operacion.lower() == "sum":
        num1 += num2
        print(num1)
    
    elif operacion.lower() == "res":
        num1 -= num2
        print(num1)

    elif operacion.lower() == "mul":
        num1 *= num2
        print(num1)

    elif operacion.lower() == "div":
        num1 /= num2
        print(num1)

    else:
        print("sigue intentando, la operacion no existe")


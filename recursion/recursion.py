
# Ejemplo 

def ejemplo(n):

    if n == 0:
        return 0
    else:
        print("ANTES", n)

        ejemplo(n - 1)

        print("DESPUÉS", n)

ejemplo(3) 
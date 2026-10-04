# Tres en raya

from tablero import imprimir_tablero
from ganador import verificar_empate, verificar_ganador
from jugada import pedir_posicion, asignar_valor
import random

# Juego
tablero = [
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"]
]

turno = random.choice(["X", "O"])

while True:
    imprimir_tablero(tablero)
    print(f"Turno de: {turno}")
    posicion = pedir_posicion()
    tablero, posicion = asignar_valor(tablero,posicion, turno)

    if verificar_ganador(tablero, posicion):
        imprimir_tablero(tablero)
        print(f"Ganó {turno}")
        break

    if verificar_empate(tablero):
        imprimir_tablero(tablero)
        print("Hay un empate")
        break

    if turno == "X":
        turno = "O"
    else:
        turno = "X"
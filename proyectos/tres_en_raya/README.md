# 🎮 Tres en raya

> **Proyecto de estudio y práctica de lógica y programación mediante el desarrollo de un juego de Tres en raya (Gato).**

> [!NOTE]
>
> *El proyecto está desarrollado bajo mi propia lógica y razonamiento. El objetivo principal es comprender la estructura necesaria para construir un juego desde cero, aplicando funciones, matrices, ciclos, validaciones y control de flujo.*

---

## 📋 Contexto

> *Desarrollar un juego de* **Tres en raya (Gato)** *para dos jugadores que se ejecute por consola.*

> *El tablero debe representarse mediante una matriz de* **3×3** *y los jugadores deben alternar sus turnos hasta que exista un ganador o empate.*

---

## 📌 Requisitos

El programa debe permitir:

* Mostrar el tablero.
* Identificar a los dos jugadores.
* Alternar los turnos.
* Solicitar la posición donde cada jugador quiere jugar.
* Validar que la posición exista.
* Impedir jugar sobre una posición ocupada.
* Actualizar el tablero después de cada jugada.
* Detectar tres símbolos consecutivos:

  * Horizontalmente.
  * Verticalmente.
  * Diagonalmente.
* Detectar un empate.
* Informar el resultado final.

> *Se considera empate cuando el tablero está lleno y ningún jugador consiguió tres símbolos en raya.*

---

## 📂 Estructura

```text
tres-en-raya/

│
├── 📄 README.md
├── 🐍 main.py
├── 🟦 tablero.py
├── 🟩 jugada.py
└── 🟥 ganador.py
```

---

## 🧩 Organización

| 📌 Archivo      | 📝 Contenido                          |
| :-------------- | :------------------------------------ |
| 🐍 `main.py`    | Flujo principal y control del juego   |
| 🟦 `tablero.py` | Funciones relacionadas con el tablero |
| 🟩 `jugada.py`  | Solicitud y asignación de jugadas     |
| 🟥 `ganador.py` | Detección de ganador y empate         |

---

## 🎯 Objetivo

> *Aplicar los conocimientos de programación mediante la construcción de un juego funcional, utilizando matrices, funciones, ciclos, validaciones y control de flujo.*

---

**Creado y desarrollado por Elías Soto**

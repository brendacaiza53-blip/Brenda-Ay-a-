
# ==========================================
# Proyecto de Programación I
# Autora: Brenda Caiza
# ==========================================

print("===================================")
print("      PROYECTO DE PROGRAMACIÓN")
print("===================================")

print("Nombre: Brenda Caiza")
print("Carrera: Ingeniería en Software")
print("Materia: Programación I")
import random

# ===============================
# PIEDRA, PAPEL O TIJERA
# ===============================

print("===================================")
print("   PIEDRA, PAPEL O TIJERA ")
print("===================================")
print("Bienvenido al juego ")

# MENÚ PRINCIPAL
print("\n----- MENÚ PRINCIPAL -----")
print("1. Iniciar juego")
print("2. Ver reglas")
print("3. Salir")

opcion = input("\nElige una opción: ")

if opcion == "1":
    print("\nIniciando el juego... ")

elif opcion == "2":
    print("\nREGLAS DEL JUEGO:")
    print("- Piedra gana a tijera")
    print("- Tijera gana a papel")
    print("- Papel gana a piedra")

elif opcion == "3":
    print("\nGracias por visitar el juego ")
    exit()

else:
    print("\nOpción inválida")

# ===============================
# JUEGO PRINCIPAL
# ===============================

victorias = 0
derrotas = 0
empates = 0

while True:
    print("\n--- MENÚ DEL JUEGO ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Ver resultados")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        usuario = "piedra"
    elif opcion == "2":
        usuario = "papel"
    elif opcion == "3":
        usuario = "tijera"
    elif opcion == "4":
        print("\nRESULTADOS:")
        print("Victorias:", victorias)
        print("Derrotas:", derrotas)
        print("Empates:", empates)
        continue
    elif opcion == "5":
        print("\nGracias por jugar ")
        break
    else:
        print("Opción inválida")
        continue

    computadora = random.choice(["piedra", "papel", "tijera"])

    print("\nTú elegiste:", usuario)
    print("Computadora eligió:", computadora)

    if usuario == computadora:
        print(" EMPATE")
        empates += 1

    elif (
        (usuario == "piedra" and computadora == "tijera") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijera" and computadora == "papel")
    ):
        print(" ¡GANASTE!")
        victorias += 1

    else:
        print(" PERDISTE")
        derrotas += 1

    # JUGAR OTRA VEZ
    repetir = input("\n¿Quieres jugar otra vez? (s/n): ")

    if repetir.lower() != "s":
        print("\nFin del juego  Gracias por jugar")
        break
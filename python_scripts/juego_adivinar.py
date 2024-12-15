import random

numero_secreto = random.randint(1, 10)
intentos = 0

print("¡Bienvenido al Juego de Adivinar el Número!")
while True:
    adivinar = int(input("Adivina un número entre 1 y 10: "))
    intentos += 1

    if adivinar < numero_secreto:
        print("¡Demasiado bajo! Intenta de nuevo.")
    elif adivinar > numero_secreto:
        print("¡Demasiado alto! Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
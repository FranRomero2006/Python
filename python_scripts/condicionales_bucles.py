numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"Cuadrado de {num} es {num**2}")

intentos = 0
while intentos < 3:
    adivinar = input("Adivina un número (0-10): ")
    if adivinar == "7":
        print("¡Correcto!")
        break
    intentos += 1
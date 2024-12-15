def calcular(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return a / b if b != 0 else "Error: División por cero"

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
op = input("Ingresa la operación (+, -, *, /): ")
resultado = calcular(num1, num2, op)
print(f"Resultado: {resultado}")
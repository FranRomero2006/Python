estudiantes = ["Juan", "Ana", "Luis", "María"]
for estudiante in estudiantes:
    print(estudiante)

info_contacto = {
    "Juan": "juan@email.com",
    "Ana": "ana@email.com",
    "Luis": "luis@email.com"
}

for nombre, correo in info_contacto.items():
    print(f"Nombre: {nombre}, Correo: {correo}")

estudiantes.append(input("Ingresa un nuevo nombre de estudiante: "))
nuevo_correo = input("Ingresa el correo del nuevo estudiante: ")
info_contacto[estudiantes[-1]] = nuevo_correo
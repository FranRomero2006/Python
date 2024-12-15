from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['universidad']
coleccion_estudiantes = db['estudiantes']

estudiantes = [
    {"nombre": "Juan", "edad": 20, "ciudad": "Bogotá"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Medellín"},
    {"nombre": "Luis", "edad": 19, "ciudad": "Cali"}
]
coleccion_estudiantes.insert_many(estudiantes)

print("Todos los estudiantes:")
for estudiante in coleccion_estudiantes.find():
    print(estudiante)

rint("\nEstudiantes de Bogotá:")
for estudiante in coleccion_estudiantes.find({"ciudad": "Bogotá"}):
    print(estudiante)

print("\nEstudiantes mayores de 20 años:")
for estudiante in coleccion_estudiantes.find({"edad": {"$gt": 20}}):
    print(estudiante)
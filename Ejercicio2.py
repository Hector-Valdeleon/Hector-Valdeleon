import numpy as np

# Datos de los 6500 estudiantes en listas
codigos = np.random.randint(1000, 9999, 6500)  # Códigos 
nombres = np.array([f"Estudiante{i}" for i in range(6500)])  # Nombres 
promedios = np.random.uniform(0, 5, 6500)  # Promedios 
carreras = np.random.randint(1, 6, 6500)  # Código de la carrera 
años_ingreso = np.random.randint(1980, 2025, 6500)  # Año de ingreso

def listar_estudiantes_promedio_carrera(codigo_carrera):
    indices = np.where((carreras == codigo_carrera) & (promedios >= 4))
    estudiantes_carrera = zip(codigos[indices], nombres[indices])
    contador = 0
    print(f"Estudiantes de la carrera {codigo_carrera} con promedio igual o mayor a 4:")
    for codigo, nombre in estudiantes_carrera:
        print(f"Código: {codigo}, Nombre: {nombre}")
        contador += 1
    print(f"Total de estudiantes: {contador}")
def listar_estudiantes_condicionales_antes_1990():
    indices = np.where((años_ingreso < 1990) & (promedios<3.2))
    estudiantes_condicionales = zip(codigos[indices], nombres[indices])
    print("Estudiantes que ingresaron antes de 1990 y están condicionalidad:")
    for codigo, nombre in estudiantes_condicionales:
        print(f"Código: {codigo}, Nombre: {nombre}")


codigo_carrera = int(input("Ingrese el código de la carrera a listar: "))
listar_estudiantes_promedio_carrera(codigo_carrera)
listar_estudiantes_condicionales_antes_1990()

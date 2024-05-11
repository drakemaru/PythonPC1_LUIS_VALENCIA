
alumnos = []  

n = int(input("Ingrese la cantidad de alumnos: "))

i = 0
while i < n:
    nombre = input("Ingrese el nombre del alumno: ")
    calificaciones = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j+1} del alumno {nombre}: "))
        calificaciones.append(calificacion)
    
    alumno = {"Alumno": nombre, "Notas": calificaciones}
    alumnos.append(alumno)
    i += 1

print("\nListado completo de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")




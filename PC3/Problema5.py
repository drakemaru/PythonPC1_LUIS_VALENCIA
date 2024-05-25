
class Alumno:

    def __init__(self,nombre, registro):
        self.nombre = nombre
        self.registro = registro
        pass
    
    def Display(self):
        print(f'El nombre del usuario es {self.nombre}')
        print(f'El número de registro del usuario es {self.registro}')
    
    def SetAge(self,edad):
        self.edad = edad
        print(f'la edad del alumno es: {self.edad}')
    
    def SetNota(self,nota):
        self.nota = nota
        print(f'Las notas del alumno son: ', self.nota)
      
    
alumno1 = Alumno('Jose Perez','123456789')
alumno1.Display()
alumno1.SetAge(24)
alumno1.SetNota([10,20,14,15,16])
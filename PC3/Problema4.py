class Rectangulo:
    def __init__(self, largo:int, ancho:int):
        self.largo = largo
        self.ancho = ancho
        pass

    def calcular_area(self):
        return self.largo * self.ancho
    
    def __str__(self) -> str:
        return f'El rectango de largo {self.largo}m y de ancho {self.ancho}m'

n1= float(input('Ingrese el largo del rectangulo: '))
n2= float(input('Ingrese el ancho del rectangulo: '))
rectangulo1=Rectangulo(largo=n1,ancho=n2)
print(rectangulo1)
area = rectangulo1.calcular_area()
print(f'El rectangulo tiene un área de {area}m**2')
        
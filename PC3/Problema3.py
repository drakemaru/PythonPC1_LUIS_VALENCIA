import math

class Circulo: 
    PI = 3.14
    def __init__(self, radio : float):

        self.radio = radio 
        pass

    def calcular_area(self) :
        return self.PI * pow(self.radio,2)
    

    def __str__(self) -> str:
        return f'El circulo posee un radio: {self.radio}m'

n = int(input('Ingrese el radio del circulo: '))

circulo1 = Circulo(n)
print(circulo1)
area = circulo1.calcular_area()
print(f'El área del circulo es: {area}m**2')

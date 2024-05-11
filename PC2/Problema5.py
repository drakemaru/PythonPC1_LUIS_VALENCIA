
def contador (x, y) :
    numero = str(x)
    contar = numero.count(str(y))
    return contar 


numero_1 = int(input('Ingrese un número entero: '))
numero_2 = int(input('Ingrese un dígito entero: '))
total = contador(numero_1, numero_2)
print(f'EL número ingresado es: {numero_1} y el dígito es: {numero_2}')
print(f'Las veces que se repite el dígito es: {total}')


#leemos datos
print('***BIENVENIDO AL PROGRAMA QUE CALCULA LA SUMA DE LOS N PRIMEROS NUMEROS ENTEROS POSITIVOS***')
num=int(input('Ingrese el  valor del número entero positivo N a calcular: '))

#sol
suma=(num*(num + 1))/2

print(f'La suma de todos los enteros de 1 hasta {num} es: {suma}')

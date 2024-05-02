num1=float(input('Ingrese el primer número: '))
num2=float(input('Ingrese el segundo número: '))

print('***BIENVENIDO AL MENU DE OPERACIONES MATEMATICAS BÁSICAS***')
print('***POR FAVOR ELIJA UNA DE LAS SIGUIENTES OPCIONES***')
print('OPCION 1: SUMA DE LOS DOS NUMEROS INGRESADOS')
print('OPCION 2: RESTA DE LOS NUMEROS INGRESADOS (PRIMERO - SEGUNDO)')
print('OPCION 3: MULTIPLICACIÓN DE LOS DOS NÚMEROS INGRESADOS')

op=float(input('Ingrese por favor el número de la opción de la operación a realizar: '))

if op == 1 :
    suma = num1 +num2
    print(f'La suma de ambos números es: {suma}')

elif op == 2 :
    resta = num1 - num2
    print(f'La resta de ambos números es: {resta}')

elif op == 3 :
    multi= num1 * num2
    print(f'La multiplicación de ambos números es: {multi}')

else:
    print('La opción ingresada no es correcta')
    print('***FIN***')
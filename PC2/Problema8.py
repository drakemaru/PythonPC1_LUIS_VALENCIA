def factorial (numero:int) :
    if numero == 0 :
        return 1

    calculado = 1
    while numero > 0 :
        calculado = calculado * numero
        numero -= 1

    return calculado

numero = int(input('Ingrese el número a calcular su factorial: '))
caso = factorial(numero)
print(f'El factorial de {numero} es : {caso}')


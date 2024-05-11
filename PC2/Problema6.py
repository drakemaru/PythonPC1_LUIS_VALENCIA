def serie (limite) :
    numero1 = 0
    numero2 = 1

    lista = []
    lista.append(numero1)
    lista.append(numero2)

    while numero2 < limite :
        numero3 = numero1 + numero2
        lista.append(numero3) 

        numero1 = numero2 
        numero2 = numero3

    return lista

serie_completa = serie(50)

print('La serie de Fibonacci entre 0 y 50 es: ')
print(serie_completa)


        
sh=int(input('Ingrese el número de shows músicales que ha visto en el último año: '))
if sh > 3:
    print(f'El número de show vistos es {sh}, este número es mayor que 3?')
    print(sh>3)

elif sh>=0 and sh<=3:
    print(f'El número de show vistos es {sh}, este número es mayor que 3?')
    print(sh>3 and sh>=0)

else:
    print('Ingrese un número positivo')
print('***BIENVENIDO A LA SALA DE JUEGOS***')
edad=int(input('Ingrese por favor su edad: '))

if edad >=0 and edad < 4:
    print('Usted puede ingresar de manera GRATUTITA a la Sala de Juegos')

elif edad >=4 and edad < 18:
    print('El precio de entrada tiene un coste de $5')

elif edad >= 18:
    print('El precio de entrada tiene un costo de $10')

else:
    print('Ingrese una edad real')
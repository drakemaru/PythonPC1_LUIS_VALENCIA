#Leemos datos
numero1 = int(input('Ingrese el número total de payasos vendidos: '))
numero2 = int(input('Ingrese el número total de muñecas vendidas: '))

#solución
payasos=numero1*112
munecas=numero2*75
peso_total=payasos+munecas

print(f'EL peso total de los payasos vendidos es: {payasos} gr')
print(f'El peso total de las muñecas vendidas es: {munecas} gr')
print(f'El peso total del paquete que será enviado es: {peso_total} gr ')


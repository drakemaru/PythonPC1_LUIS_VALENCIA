#Leemos datos
consumo=float(input('Ingrese el costo total del consumo: '))
porcentaje = float(input('Ingrese el porcentaje, de su costo total, que desea dejar al mesero: '))

#Solución
propina=(consumo*porcentaje)/100

print(f'La cantidad de dinero que debe usted debe dejar como propina es: {propina}')
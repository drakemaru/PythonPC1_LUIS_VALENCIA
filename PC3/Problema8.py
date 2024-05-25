import random
import modulo8

num_alea = modulo8.aleatorios()

print('Lista obtenida')

modulo8.mostrar_lista(num_alea)

num_ord = modulo8.ordenar_lista(num_alea)
print('Lista ordenada')
modulo8.mostrar_lista(num_ord)
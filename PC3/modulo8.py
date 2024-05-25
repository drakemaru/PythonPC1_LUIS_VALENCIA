import random

def aleatorios(cantidad=20, rango=(0,100)):
    return [random.randint(rango[0],rango[1]) for _ in range(cantidad)]

def mostrar_lista(lista):
    print(lista)

def ordenar_lista(lista):
    return sorted(lista)

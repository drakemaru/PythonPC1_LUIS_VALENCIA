ingreso = input('Desea ingresar un número?: ').lower()
num_par = 0
num_impar = 0
lista = []
while ingreso == "si" :
    numero = int(input('Ingrese el número: '))
    lista.append(numero)
    
    if numero%2 ==0 :
        num_par +=1
    else:
        num_impar +=1
     


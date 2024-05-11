empezar = True
num_par = 0
num_impar = 0
lista = []
while empezar :
    ingreso = input('Desea ingresar un número?: ').lower()

    if ingreso == 'no' :
        empezar == False
        print('Programa Finalizado')
        break 

    numero = int(input('Ingrese el número: '))
    lista.append(numero)
    
    if numero%2 ==0 :
        num_par +=1
    else:
        num_impar +=1

print('Los números ingresados son: ',lista)
print(f'La cantidad de números pares es: {num_par}')
print(f'La cantidad de números impares es: {num_impar}')  


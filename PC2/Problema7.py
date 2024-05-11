
def calculo_primo(a:int) :
    primo = True
    for n in range(2,a):
        if a % n == 0 :
            return primo == False

    return primo == True

numero = int(input('Ingrese el número a calcular: '))
caso = calculo_primo(numero)
print('El número es primo?')
print(caso)
    
    
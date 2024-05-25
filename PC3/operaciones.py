import math

def sumar(a:int,b:int) :
    try :
        resultado = a + b 
        print(f'El resultado de la suma es: {resultado}')

    except ValueError:
        print('El valor ingresado es incorrecto')

    finally:
        print('Programa ejecutado')
        
def resta(a:int,b:int):
    try :
        resultado = a - b 
        print(f'El resultado de la suma es: {resultado}')

    except ValueError:
        print('El valor ingresado es incorrecto')

    finally:
        print('Programa ejecutado')

def producto(a:int,b:int):
    try :
        resultado = a * b 
        print(f'El resultado de la suma es: {resultado}')

    except ValueError:
        print('El valor ingresado es incorrecto')

    finally:
        print('Programa ejecutado')
    
def division(a:int,b:int):
    try :
        resultado = a / b 
        print(f'El resultado de la suma es: {resultado}')

    except ValueError:
        print('El valor ingresado es incorrecto')

    except ZeroDivisionError :
        print('No se puede dividir entre 0')

    finally:
        print('Programa ejecutado')



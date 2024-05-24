print('Bienvenido al Programa para calcular la cantidad de combustible')
print('A continuación ingresará los números de la fracción a calcular')
def main ():

    while(True):

        try : 
            nume = int(input('Ingrese el número que irá en el numerador: '))
            deno = int(input('Ingrese el número que irá en el denominador: '))
            result = round( (nume / deno)*100 )

            if result >= 99 :
                print ('F')

            elif result >= 0 and result <1 :
                print ('E')

            else :
                print(f'{result}%')

        except ValueError :
            print('El valor ingresado es incorrecto')
            print('Vuelva a introducir los números')
        
        except ZeroDivisionError :
            print('No se puede dividir entre 0 ')
            print('Vuelva a introducir los números')

        else :
            print('Programa ejecutado de manera correcta')
            break

if __name__ == '__main__':
    main()




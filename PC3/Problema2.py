print('Bienvenido al programa de calificaciones')
print('Debera ingresar las calificaciones separadas por una ","')

def main():

    try: 

        notas_ingreso = input('Ingrese las notas:  ')
        notas_separadas = notas_ingreso.split(',')
        notas_lista = []

        for notas in notas_separadas :
            notas_nuevo = round(float(notas.strip()))
            notas_lista.append(notas_nuevo)

        print('Las notas redondeadas son: ', notas_lista)

    except ValueError :
        print('El valor ingresado es incorrecto')

if __name__ == '__main__':
    main()




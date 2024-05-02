tiempo=input('Ingrese la hora: ')
hora,minuto = tiempo.split(":")
h = float(hora)
m = float(minuto)
if h >=7 and h <8:
    if m>=0 and m<60 :
        print('Es hora de desayunar')

elif h >=12 and h < 13:
    if m>=0 and m<60 :
        print('Es hora de almorzar')

elif h >= 18 and h < 19 :
    if m>=0 and m<60 :
        print('Es hora de cenar')
else:
    print()


def delete_vocales(text):
	vocales = ['a','A','e','E','i','I','o','O','u','U']
	resto = ''

	for letra in text:
		if letra not in vocales:
			resto += letra
	return resto
lista = input('Ingrese una cadena de texto: ')
print(delete_vocales(lista))






def delete_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

print('***BIENVENIDOS AL PROGRAMA QUE ELIMINA ELEMENTOS DUPLICADOS EN LA LISTA***')
lista_original = [1, 2, 3, 4, 2, 3, 6, 7, 8, 1, 8, 9, 2, 3]
lista_sin_duplicados = delete_duplicados(lista_original)
print("La lista original es:", lista_original)
print("La lista sin duplicados es:", lista_sin_duplicados)

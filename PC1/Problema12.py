nombre=input('Ingrese por favor el nombre del archivo con su extensión correspondiente: ')
archivo, sufijo = nombre.split(".")
lista = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

if sufijo == None :
    print('application/octet-stream')

if sufijo in lista :
    base_de_datos = {

        "gif" : "image/gif",
        "jpg" : "image/jpeg",
        "jpeg" : "image/jpeg",
        "png" : "image/png",
        "pdf" : "application/pdf",
        "txt" : "text/plain",
        "zip" : "application/zip"
    }

    print(base_de_datos[sufijo])

else:
    print('application/octet-stream')







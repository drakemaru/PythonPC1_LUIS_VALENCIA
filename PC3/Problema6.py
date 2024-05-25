class Producto :
    def __init__(self, nombre, precio, year):
        self.nombre = nombre
        self.precio = precio
        self.year = year
        print('se ha agregado el producto: ',self.nombre)
        pass
    def __str__(self):
        return '{} ({})'.format(self.nombre, self.year)

class Catalogo :
    productos = []

    def __init__(self, productos = []):
        self.productos = productos
        pass
    
    def agregar(self, p):
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)

    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                break
        return producto


producto1= Producto('botella',5, 2019)
catalogo1= Catalogo([producto1])
catalogo1.mostrar()
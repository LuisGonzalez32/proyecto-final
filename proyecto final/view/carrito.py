from logic.carrito_logic import CarritoDb
from logic.view_carrito_Logic import View_carrito
from logic.productos_logic import Productos
from view.producto import Producto

productosDb = Productos()
carrito = CarritoDb()
productos = Producto()
viewCarrito = View_carrito()

class Carrito():
    def __init__(self):
        super().__init__()


    def getCarrito(self, idCliente):
        productos.getNombreProducto()  # da todos los productos dispobibles que hay ordenados por categorias
        nombreProducto = input("ponga el nombre del producto que quiere: ")
        idProducto = productosDb.getIdProducto(nombreProducto)
        while (idProducto is None):    # si el getIdProducto da None es que ese producto no esta en la base de datos
            print()
            nombreProducto = input("Error, ponga un nombre que este en la lista: ")
            idProducto = productosDb.getIdProducto(nombreProducto)
        cantidad = int(input("ponga la cantidad que quiere: "))
        costoTotal = productosDb.costoTotalProducto(cantidad, nombreProducto)
        nuevaCantidad = productosDb.verificarCantidadCarrito(cantidad, nombreProducto) # verifica si hay suficientes productos

        while nuevaCantidad < 0:
            cantidad = int(input("No hay existencias, ponga otra cantidad: "))
            costoTotal = productosDb.costoTotalProducto(cantidad, nombreProducto)
            nuevaCantidad = productosDb.getCantidadCarrito(cantidad, nombreProducto)

        carrito.agregarCarrito(idCliente, idProducto, cantidad, costoTotal)
        print("presione 1 si quiere agregar otro producto al carrito")
        print("presione cualquier otra tecla si quiere salir")
        opcion = input()
        if opcion == "1":
            self.getCarrito(idCliente)
        else:
            pass


    def deleteCarrito(self, idCliente):
        viewCarrito.verCarrito(idCliente)
        producto = input("Ponga el producto que quiere eliminar de su carrito: \n")
        idProducto = productosDb.getIdProducto(producto)
        
        while (idProducto is None):
            producto = input("Error, ponga el producto que quiere eliminar de su carrito: \n")
            idProducto = productosDb.getIdProducto(producto)
        
        carrito.deleteProductoCarrito(idCliente, idProducto)
        
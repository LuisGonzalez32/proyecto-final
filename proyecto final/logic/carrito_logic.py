from core.dx_logic import Logic
from persist_objects.carritoObj import carritoObj
from datetime import datetime
from logic.compras_logic import ComprasDb
from logic.productos_logic import Productos
from prettytable import PrettyTable

compra = ComprasDb()
productos = Productos()

class CarritoDb(Logic):
    def __init__(self):
        super().__init__("carrito")

    def getAllCarrito(self, sql):
        carritoList = super().getAllRows(self.tableName, sql)
        carritoObjList = []
        for element in carritoList:
            newCart = self.createCarritoObj(element)
            carritoObjList.append(newCart)
        return carritoObjList

    def getProductoId(self, column, value):
        rowDict = super().getRow(self.tableName, column, value)
        newCart = self.createProductoObj(rowDict)
        return newCart

    # polimorfismo
    def createCarritoObj(self, id, idCliente, idProducto, cantidad, costoTotal):
        detallesPagoObj = carritoObj(id, idCliente, idProducto, cantidad, costoTotal)
        return detallesPagoObj

    def createCarritoObj(self, carritoDict):
        carritoDict = carritoObj(
            carritoDict["id"],
            carritoDict["id_cliente"],
            carritoDict["id_producto"],
            carritoDict["cantidad"],
            carritoDict["costo_total"],
        )
        return carritoDict

    

    def verificarCarrito(self, idCliente):
        
        database = self.database
        sql = f"""select * from carrito where id_cliente = {idCliente}"""
                
        record = database.executeQueryRows(sql)

        if record:
            return record
        else:
            return None
            
        
    # agrega el producto al carrito
    def agregarCarrito(self, idCliente, idProducto, cantidad, total):
        
        database = self.database
        sql = f"""INSERT INTO carrito
        (id_cliente,id_producto,cantidad,costo_total)
         VALUES ({idCliente}, {idProducto}, {cantidad}, {total}) """
                    
        row = database.executeNonQueryBool(sql)
        print()
        if row>0:
            print("El producto fue agregado al carrito\n")
        else:
            print("El producto no pudo der agregado al carrito\n")

       

    # agarra todos los productos de la tabla carrito y los pone en la tala compras
    # (el id de la tabla Detalles_pago, el id del producto, la cantidad y el costo total por porducto)
    def pago(self, idCliente, idDetalles):
        
        
        database = self.database
        sql = f"""select * from carrito where id_cliente = {idCliente}"""
                
        record = self.getAllCarrito(sql)

        for carrito in record:
            compra.compras(idDetalles, carrito.idProducto, carrito.cantidad, carrito.costoTotal)

        print()
        print("La compra se guardo\n")


    def sumarCosto(self, idCliente):      # sumar el costo de todos los elementos del carrito
    
        database = self.database
        sql = f"""select * from carrito where id_cliente = {idCliente} """
            
        record = self.getAllCarrito(sql)

        costo_total = 0

        for carrito in record:
            costo_total = costo_total + carrito.costoTotal

        return costo_total
                
           
    # para cada producto en el carrito, cerifica la cantidad de estos que hay en la tabla productos
    # y resta la cantidad disponible menos la cantidad comprada en el metodo updateCantidad
    def restarCantidadProducto(self, idCliente):

        sql = f"""select * from carrito where id_cliente = {idCliente}"""
            
        record = self.getAllCarrito(sql)

        for carrito in record:
            cantidadDisponible = productos.getCantidadActual(carrito.idProducto)
            productos.updateCantidad(carrito.idProducto, cantidadDisponible, carrito.cantidad)

       
    # elimina el producto que pongamos del carrito
    def deleteProductoCarrito(self, idCliente, idProducto):

        database = self.database
        sql = f"DELETE FROM carrito WHERE id_cliente = '{idCliente}' and id_producto = '{idProducto}'"

        rowCount = database.executeNonQueryRows(sql)
        print()
        if rowCount > 0:
            print(rowCount, "producto eliminado del carrito")
        else: 
            print("No se pudo eliminar el porducto del carrito\n")
        
        
    # elimina todos los productos del carrito cuando hacemos la compra
    def deleteAllCarrito(self, idCliente):
        
        database = self.database
        sql = f"""DELETE FROM carrito WHERE id_cliente = {idCliente}"""
            
        row = database.executeNonQueryRows(sql)

        if not row:
            print("no se pudieron eliminar todos los elementos del carrito: ")
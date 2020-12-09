from core.dx_logic import Logic
from persist_objects.view_carritoObj import view_carritoObj
from logic.carrito_logic import CarritoDb
from datetime import datetime
from prettytable import PrettyTable

Carrito = CarritoDb()

class View_carrito(Logic):
    def __init__(self):
        super().__init__("view_carrito")

    def getAllCarrito(self, sql):
        detallesPagoList = super().getAllRows(self.tableName, sql)
        detallesPagoObjList = []
        for element in detallesPagoList:
            newCart = self.createCarritoObj(element)
            detallesPagoObjList.append(newCart)
        return detallesPagoObjList

    def getProductoId(self, column, value):
        rowDict = super().getRow(self.tableName, column, value)
        newCart = self.createProductoObj(rowDict)
        return newCart

    # polimorfismo
    def createCarritoObj(self, idCliente, nombreCliente, nombreProducto, cantidad, costoTotal):
        carritoObj = view_carritoObj(idCliente, nombreCliente, nombreProducto, cantidad, costoTotal)
        return carritoObj

    def createCarritoObj(self, carritoDict):
        carritoDict = view_carritoObj(
            carritoDict["idCliente"],
            carritoDict["nombreCliente"],
            carritoDict["nombreProducto"],
            carritoDict["cantidad"],
            carritoDict["costo_total"],
        )
        return carritoDict


    def verCarrito(self, idCliente):
       
        database = self.database
        sql = f"select * from view_carrito where idCliente = '{idCliente}'"
        
        record = self.getAllCarrito(sql) 
        x = PrettyTable(["producto", "cantidad", "total"])

        if not record:
            print("No hay ningun producto disponible\n")
            return None

        else:     
            for carrito in record:
                x.add_row([carrito.nombreProducto, carrito.cantidad, carrito.costoTotal])
            print(x)
            
            costo = Carrito.sumarCosto(idCliente)
            
            print("El costo total es ",costo,"\n")
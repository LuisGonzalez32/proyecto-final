from core.dx_logic import Logic
from persist_objects.view_comprasObj import view_comprasObj
from datetime import datetime
from prettytable import PrettyTable

class ComprasDb(Logic):
    def __init__(self):
        super().__init__("compras")

    def getAllCompras(self, sql):
        comprasList = super().getAllRows(self.tableName, sql)
        comprasObjList = []
        for element in comprasList:
            newCart = self.createComprasObj(element)
            comprasObjList.append(newCart)
        return comprasObjList

    def getProductoId(self, column, value):
        rowDict = super().getRow(self.tableName, column, value)
        newCart = self.createComprasObj(rowDict)
        return newCart

    # polimorfismo
    def createComprasObj(self, idCliente, nombreCliente, nombreProducto, cantidad, costo_total, tarjeta_credito, pais, ciudad, direccion, hora_compra):
        detallesPagoObj = view_comprasObj(idCliente, nombreCliente, nombreProducto, cantidad, costo_total, tarjeta_credito, pais, ciudad, direccion, hora_compra)
        return detallesPagoObj

    def createComprasObj(self, comprasDict):
        comprasDict = view_comprasObj(
            comprasDict["idCliente"],
            comprasDict["nombreCliente"],
            comprasDict["nombreProducto"],
            comprasDict["cantidad"],
            comprasDict["costo_total"],
            comprasDict["tarjeta_credito"],
            comprasDict["pais"],
            comprasDict["ciudad"],
            comprasDict["direccion"],
            comprasDict["hora_compra"],
        )
        return comprasDict



    def compras(self, idDetalles, idProducto, cantidad, total):
        
        database = self.database
        sql = f"""INSERT INTO compras
        (id_detalles_pago,id_producto,cantidad,costo_total)
        VALUES ({idDetalles}, {idProducto}, {cantidad}, {total}) """
            
        record = database.executeNonQueryBool(sql)

        if not record:
            print("no se pudo insertar la tabla compras")

    
    def factura(self, idDetalles, costo):
        try:
            database = self.database
            sql = f"""INSERT INTO factura
            (id_detalles_pago,total_pago)
            VALUES ({idDetalles}, {costo}) """
                
            database.executeNonQueryBool(sql)

        except Exception:
            print()
            print("No se pudo hacer em metodo factura")

        finally:
            pass

    def verCompras(self):
        
        sql = "SELECT * FROM tienda.view_compras order by hora_compra"
        
        record = self.getAllCompras(sql) # fetchall
        x = PrettyTable(["nombre", "producto", "cantidad", "costo total", "tarjeta de credito", 
                         "pais", "ciudad", "direccion", "hora de compra"])

        if not record:
            print("No hay ningun producto disponible\n")
            
        else:            
            for compras in record:
                x.add_row([compras.nombreCliente, compras.nombreProducto, compras.cantidad, 
                           compras.costo_total, compras.tarjeta_credito, compras.pais, 
                           compras.ciudad, compras.direccion, compras.hora_compra])

            print(x)


    def verComprasCliente(self, idCliente):
        
        sql = f"select * from view_compras where idCliente = {idCliente}"
        
        record = self.getAllCompras(sql) # fetchall
        x = PrettyTable(["producto", "cantidad", "costo total", "tarjeta de credito", "pais", "ciudad", 
                        "direccion", "hora de compra"])

        if not record:
            print("No hay ningun producto disponible\n")     
        else:            
            for compras in record:
                x.add_row([compras.nombreProducto, compras.cantidad, 
                           compras.costo_total, compras.tarjeta_credito, compras.pais, 
                           compras.ciudad, compras.direccion, compras.hora_compra])
            print(x)
        

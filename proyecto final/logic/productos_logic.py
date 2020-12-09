from core.dx_logic import Logic
from persist_objects.prodctos_obj import ProductosObj
from prettytable import PrettyTable
from datetime import datetime

class Productos(Logic):
    def __init__(self):
        super().__init__("productos")

    def getAllProductos(self, sql):
        productoList = super().getAllRows(self.tableName, sql)
        productoObjList = []
        for element in productoList:
            newCart = self.createProductoObj(element)
            productoObjList.append(newCart)
        return productoObjList

    #def getProductoId(self, column, value):
    #    rowDict = super().getRow(self.tableName, column, value)
    #    newCart = self.createProductoObj(rowDict)
    #    return newCart

    # polimorfismo
    def createProductoObj(self, id, nombre, categoria, descripcion, precio, cantidad, ultima_actualizacion):
        productoObj = ProductosObj(id, nombre, categoria, descripcion, precio, cantidad, ultima_actualizacion)
        return productoObj

    def createProductoObj(self, productoDict):
        productoObj = ProductosObj(
            productoDict["id"],
            productoDict["nombre"],
            productoDict["id_categoria"],
            productoDict["descripcion"],
            productoDict["precio"],
            productoDict["cantidad_disponible"],
            productoDict["ultima_actualizacion"],
        )
        return productoObj




        # inserta un nuevo producto
    def insertarProducto(self, nombre, id_categoria, descripcion, precio, cantidad):
    
        database = self.database
        current_Date = datetime.now()
        date = current_Date.strftime("%Y-%m-%d %H:%M:%S")
               
        sql = f"""INSERT INTO productos
        (nombre,id_categoria,descripcion,precio,cantidad_disponible,
        ultima_actualizacion) VALUES (
        '{nombre}',{id_categoria}, '{descripcion}', {precio}, {cantidad}, '{date}') """
   
        producto = database.executeNonQueryBool(sql)
        if producto:
            print("")
            print("El producto ha sido insertado correctamente\n")
    


    # para buscar un producto por categorias
    def getProducto(self, idCategoria):     
    
        sql = f"""select * from productos
        where id_categoria =  {idCategoria}"""      
        
        record = self.getAllProductos(sql) # fetchall
        x = PrettyTable(["productos"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for producto in record:
                if producto.cantidad > 0:
                    x.add_row([producto.nombre])
            
            print(x)
            return True

            


            
    def updateObjeto(self, campo, nombreActual, nuevoNombre):

        database = self.database
        current_Date = datetime.now()
        formatted_date = current_Date.strftime("%Y-%m-%d %H:%M:%S")

        sql = f"""UPDATE productos SET `{campo}` = '{nuevoNombre}',
        ultima_actualizacion = '{formatted_date}' WHERE nombre = '{nombreActual}';"""
            
        count = database.executeNonQueryRows(sql)

        if count > 0:
            print("El campo ha sido actualizado correctamente")
        else:
            print("No se pudo actualizar correctamente\n")


    def deleteProducto(self, nombre):

        database = self.database
        sql = f"DELETE FROM productos WHERE nombre = '{nombre}'"

        count = database.executeNonQueryRows(sql)

        if count > 0:
            print("El campo ha sido eliminado correctamente")
        else:
            print("No se pudo eliminar, ya se han hecho compras con ese producto")
        



    # obtiene el id para el carrito
    def getIdProducto(self, nombre):
        
        sql = f"""select * from productos where nombre = '{nombre}'"""
            
        record = self.getAllProductos(sql)

        if record:
            for producto in record:
                return producto.id
            else:
                return None


    # el precio del producto multiplicado por la cantidad de productos, para el carrito
    def costoTotalProducto(self, cantidad, nombreProducto):

        sql = f"""select * from productos where nombre = '{nombreProducto}'"""
        
        record = self.getAllProductos(sql)

        for producto in record:
            return cantidad * producto.precio

    

    # para verificar si la cantidad que queremos poner en el carrito esta permitida
    def verificarCantidadCarrito(self, cantidad, nombreProducto):
        
        sql = f"""select * from productos where nombre = '{nombreProducto}'"""
        
        record = self.getAllProductos(sql)

        for producto in record:
            return producto.cantidad - cantidad


    # obtener la cantidad del producto que hay en la tabla productos
    def getCantidadActual(self, idProducto):
         
        database = self.database
        sql = f"""select * from productos where id = {idProducto}"""
            
        record = database.executeQueryRows(sql)

        if record:
            for producto in record:
                return producto["cantidad_disponible"]
        else:
            print("No se pudo hacer em metodo getCantidadActual")

    def updateCantidad(self, idProducto, cantidadActual, cantidadComprada):
        
        database = self.database
        current_Date = datetime.now()
        date = current_Date.strftime("%Y-%m-%d %H:%M:%S")
        
        sql = f"""Update productos set cantidad_disponible = {cantidadActual - cantidadComprada},
        ultima_actualizacion = '{date}' where id = {idProducto}"""

        row = database.executeNonQueryRows(sql)

        if not row:
            print("No se pudo hacer en metodo updateCantidad")

    
    
    
from core.dx_logic import Logic
from persist_objects.categoria_obj import CategoriaObj
from prettytable import PrettyTable
import pymysql

class Categoria(Logic):
    def __init__(self):
        super().__init__("categorias")

    def getAllCategorias(self, sql):
        categoriaList = super().getAllRows(self.tableName, sql)
        categoriaObjList = []
        for element in categoriaList:
            newCart = self.createCategoriaObj(element)
            categoriaObjList.append(newCart)
        return categoriaObjList

    def getCategoriaById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newCart = self.createCategoriaObj(rowDict)
        return newCart

    # polimorfismo
    def createCategoriaObj(self, id, categoria):
        categoriaObj = CategoriaObj(id, categoria)
        return categoriaObj

    def createCategoriaObj(self, categoriaDict):
        categoriaObj = CategoriaObj(
            categoriaDict["id"],
            categoriaDict["categoria"],
        )
        return categoriaObj




    
   # inserta la categoria a la tabla categorias
    def insertarCategoria(self, categoria):
        
        database = self.database
        sql = f"""INSERT INTO categorias
        (categoria) VALUES ('{categoria}') """

        categoria = database.executeNonQueryBool(sql)
        if categoria == True:
            print("")
            print("La categoria ha sido insertada correctamente")

        
    # valida si, al insertar un producto la categoria esta en la tabla categorias, si esta devuelve su id, sino no devuelve nada
    def validarCategoria(self, categoria):
        
        sql = f"""select * from categorias where categoria = '{categoria}'"""
            
        record = self.getAllCategorias(sql)

        if record:
            for row in record:
                if row.id:
                    return row.id            
        else:
            return None
        


    # ver todas las categorias
    def viewAllCategorias(self):
        
        sql = "select * from categorias"
        
        record = self.getAllCategorias(sql) # fetchall
        x = PrettyTable(["categorias"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for categoria in record:
                x.add_row([categoria.categoria])

            print(x)

   

    def getCategorias(self):  # esto es para cuando el cliente escoja categoria para el carrito

                                                          # el select esta asi porque solo queremos categorias que tengan productos
            sql = """select distinct categorias.id, categorias.categoria   
            from categorias inner join productos
            on productos.id_categoria = categorias.id"""

            record = self.getAllCategorias(sql) # fetchall
            x = PrettyTable(["categorias"])

            if not record:
                print("No hay ningun producto disponible")
                return None
            else:            
                for categoria in record:
                    x.add_row([categoria.categoria])

                print(x)


    def getIdCategoria(self, categoria):    # para buscar el producto, tenemos que tener primero el id de la categoria 
    
        sql = f"""select * from categorias
        where categoria =  '{categoria}'"""
            
        record = self.getAllCategorias(sql) # fetchall

        if not record:
            print("Esa categoria no existe\n")
            return None
        else:            
            for producto in record:
                return producto.id

from core.database_x import Database_x


class Logic:
    def __init__(self, tableName=None):
        self.database = None
        self.tableName = tableName
        self.__createDatabase()

    def __createDatabase(self):
        if self.database is None:
            self.database = Database_x()



    def getAllRows(self, tableName, sql):
        database = self.database
        rowList = database.executeQueryRows(sql)
        return rowList

    #def getRow(self, tableName, column, value):
    #    database = self.database
    #    sql = f"select * from `{database.database}`.`{tableName}` where '{column}' ={value};"
    #    rowDict = database.executeQueryOneRow(sql)
    #    return rowDict

    #def deleteRowById(self, tableName, column, value):
    #    database = self.database
    #    sql = f"DELETE FROM `{database.database}`.`{tableName}` WHERE '{column}' = {value};"
    #    rows = database.executeNonQueryRows(sql)
        
    #    if rows > 0:
    #        print("el producto ha sido eliminado correctamente")
    #    else:
    #        print("el producto no ha podido ser eliminado")

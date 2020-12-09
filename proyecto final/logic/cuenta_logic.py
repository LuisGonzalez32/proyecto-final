from core.dx_logic import Logic
from persist_objects.cuenta_obj import CuentaObj

class Cuenta(Logic):
    def __init__(self):
        super().__init__("cliente")

    def getAllCuentas(self, sql):
        cuentaList = super().getAllRows(self.tableName, sql)
        cuentaObjList = []
        for element in cuentaList:
            newCart = self.createCuentaObj(element)
            cuentaObjList.append(newCart)
        return cuentaObjList

    def getCarritoById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newCart = self.createCuentaObj(rowDict)
        return newCart

    # polimorfismo
    def createCuentaObj(self, id, nombre, apellido, usuario, contrasenia, correo):
        cartObj = CuentaObj(id, nombre, apellido, usuario, contrasenia, correo)
        return cartObj

    def createCuentaObj(self, cuentaDict):
        cartObj = CuentaObj(
            cuentaDict["id"],
            cuentaDict["nombre"],
            cuentaDict["apellido"],
            cuentaDict["usuario"],
            cuentaDict["contrasenia"],
            cuentaDict["correo"],
        )
        return cartObj




    def crearCuenta(self, nombre, apellido, usuario, contrasenia, correo):

        database = self.database
        sql = f"""INSERT INTO cliente (nombre, apellido, usuario, contrasenia, correo) VALUES (
        '{nombre}', '{apellido}', '{usuario}', '{contrasenia}', '{correo}') """
      
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La cuenta fue creada correctamente\n")


    def validarCuenta(self, usuario, contrasenia):
        
        sql = f"""select * from cliente where usuario = '{usuario}'
        and contrasenia = '{contrasenia}'"""
            
        record = self.getAllCuentas(sql)

        for row in record:
            if row.id:
                print("")
                print("La cuenta es correcta, bienvenido", row.nombre, "\n")
                return (row.id)
            elif not row.id:
                return None
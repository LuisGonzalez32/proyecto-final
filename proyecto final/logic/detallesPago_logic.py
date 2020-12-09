from core.dx_logic import Logic
from persist_objects.detalles_pago_obj import DetallesPagoObj
from datetime import datetime

class DetallesPago(Logic):
    def __init__(self):
        super().__init__("detalles_pago")

    def getAllDetallesPago(self, sql):
        detallesPagoList = super().getAllRows(self.tableName, sql)
        detallesPagoObjList = []
        for element in detallesPagoList:
            newCart = self.createDetallesPagoObj(element)
            detallesPagoObjList.append(newCart)
        return detallesPagoObjList

    # polimorfismo
    def createDetallesPagoObj(self, id):
        detallesPagoObj = DetallesPagoObj(id)
        return detallesPagoObj

    def createDetallesPagoObj(self, detallesPagoDict):
        detallesPagoDict = DetallesPagoObj(
            detallesPagoDict["id"],
        )
        return detallesPagoDict



    # inserta la tabla detallesPago
    def detallesPago(self, idCliente, pais, ciudad, direccion, tarjeta):  
        
        database = self.database
        current_Date = datetime.now()
        date = current_Date.strftime("%Y-%m-%d %H:%M:%S")

        sql = f"""INSERT INTO detalles_pago
        (id, id_cliente, pais, ciudad, direccion, tarjeta_credito, hora_compra) VALUES (0,
        '{idCliente}', '{pais}', '{ciudad}', '{direccion}', {tarjeta}, '{date}') """

        record = database.executeNonQueryBool(sql)

        if not record:
            print("No se pudieron insertar los detalles del pago")

        
    # saca el ultimo id de la tabla detallesPago  
    def idDetallesPago(self):
                
        sql = "SELECT max(id) as id FROM detalles_pago"
                
        record = self.getAllDetallesPago(sql)

        for row in record:
            return row.id

        

from logic.carrito_logic import CarritoDb
from logic.detallesPago_logic import DetallesPago
from logic.compras_logic import ComprasDb

carrito = CarritoDb()
detallesPago = DetallesPago()
compras = ComprasDb()

class Comprar():
    def __init__(self):
        super().__init__()


    def comprar(self, idCliente):
        Carrito = carrito.verificarCarrito(idCliente)

        if Carrito is None:
            print("no hay productos en el carrito, no se puede hacer la compra\n")
        else:
            pais = input("Introduzca su pais: ")
            ciudad = input("Introduzca su ciudad: ")
            direccion = input("Introduzca su direccion: ")
            tarjeta = input("Introduzca su tarjeta de credito: ")
            detallesPago.detallesPago(idCliente, pais, ciudad, direccion, tarjeta)   # pone los datos en la tabla detallesPago
            idDetalles = detallesPago.idDetallesPago()   #saca el ultimo registero de la tabla detallesPago, la que acabamos de poner
            carrito.pago(idCliente, idDetalles)  #pone todos los porductos del carrito en la tabla compras, junto con el id de detallesPago
            costo = carrito.sumarCosto(idCliente)         # suma el costo total de todos los productos del carrito
            compras.factura(idDetalles, costo)            # pone en la tabla factura el idDetallesPago y el costo total del carrito
            carrito.restarCantidadProducto(idCliente)     # resta los productos comprados de la tabla productos
            carrito.deleteAllCarrito(idCliente)           # elimina todos los productos del carrito cuando ya se han comprado
    


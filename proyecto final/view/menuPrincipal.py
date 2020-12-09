from view.producto import Producto
from logic.cuenta_logic import Cuenta
from logic.carrito_logic import CarritoDb
from logic.view_carrito_Logic import View_carrito
from view.carrito import Carrito
from logic.compras_logic import ComprasDb
from view.comprar import Comprar

producto = Producto()
cuenta = Cuenta()
carritoDb = CarritoDb()
carrito = Carrito()
comprarDb = ComprasDb()
comprar = Comprar()
viewCarrito = View_carrito()

class menuPrincipal():
    def __init__(self):
        super().__init__()

    def iniciar(self):
        self.menuPrincipal()
        

    def menuPrincipal(self):
        print("Oprima 1 si es administrador")
        print("Oprima 2 si es cliente")
        opcion = input("")
        if opcion == "1":
            self.admin()
        elif opcion == "2":
            self.sesion()
        else:
            print("Error, solo se aceptan los valores mostrados")
            self.menuPrincipal()


    
    
    def admin(self):
        print("")
        print("Oprima 1 si quiere insertar un nuevo producto")
        print("Oprima 2 si quiere buscar un producto")
        print("Oprima 3 si quiere actualizar un articulo")
        print("Oprima 4 si quiere eliminar un producto")
        print("Oprima 5 si quiere ver el historial de compras")
        print("Oprima 6 si quiere regresar al menu principal")
        opcion = input("")

        if opcion == "1":
            producto.getInsertProducto()
        elif opcion == "2":
            producto.getNombreProducto()
        elif opcion == "3":
            producto.getUpdateProducto()
        elif opcion == "4":
            producto.getDeleteProducto()
        elif opcion == "5":
            comprarDb.verCompras()
        elif opcion == "6":
            self.menuPrincipal()
        else:
            print("Error, solo se aceptan los valores mostrados")
            self.admin()
        self.admin()


 #-------------------------------------------------------------------------------------------------------------------------

    #cliente

        
    def sesion(self):
        print("presione 1 para crear una cuenta")
        print("presione 2 para iniciar sesion")
        opcion = input("")

        if opcion == "1":
            nombre = input("Introduzca su nombre: ")
            apellido = input("Introduzca su apellido: ")
            usuario = input("Introduzca su nombre de usuario: ")
            contrasenia = input("Introduzca una contraseña una contraseña: ")
            correo = input("Introduzca su correo electronico: ")
            cuenta.crearCuenta(nombre, apellido, usuario, contrasenia, correo)
            self.sesion()
        elif opcion == "2":
            usuario = input("Introduzca su usuario: ")
            contrasenia = input("Introduzca su contraseña: ")
            idCliente = cuenta.validarCuenta(usuario, contrasenia)
            
            if (idCliente is not None): 
                self.cliente(idCliente)
            else:
                print("")
                print("por favor ponga una cuenta correcta")
                print("")
                self.sesion()
        else:
            print("Error, solo se aceptan los valores mostrados")
            self.sesion()

    
    def cliente(self, idCliente):
        print("presione 1 para buscar un producto")
        print("presione 2 para ir al carrito")
        print("presione 3 para comprar")
        print("presione 4 para ver sus compras")
        print("presione 5 si quiere cerrar sesion")
        print("presione 6 si quiere regresar al menu principal")
        opcion = input("")

        if opcion == "1":
            producto.getNombreProducto()
        elif opcion == "2":
            print("Presione 1 para ver su carrito")
            print("Presione 2 para agregar un producto a su carrito")
            print("presione 3 para eliminar un producto de su carrito")
            print("Presione 4 para salir")
            opcion = input("")
            if opcion == "1":
                viewCarrito.verCarrito(idCliente)
            elif opcion == "2":
                carrito.getCarrito(idCliente)
            elif opcion == "3":
                carrito.deleteCarrito(idCliente)
        elif opcion == "3":
            comprar.comprar(idCliente)
        elif opcion == "4":
            comprarDb.verComprasCliente(idCliente)
        elif opcion == "5":
            self.sesion()
        elif opcion == "6":
            self.menuPrincipal()
        else:
            print("Error, solo se aceptan los valores mostrados")
            self.cliente(idCliente)
        self.cliente(idCliente)


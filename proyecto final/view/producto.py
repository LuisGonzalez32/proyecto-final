from logic.productos_logic import Productos
from logic.categoria_logic import Categoria

productos = Productos()
categorias = Categoria()

class Producto():
    def __init__(self):
        super().__init__()


    def getInsertCategoria(self):
        categorias.viewAllCategorias()        
        categoria = input("inserte la nueva categoria: ")
        idCategoria = categorias.validarCategoria(categoria)    #verifica si esa categoria ya esta registrada
        while idCategoria is not None: 
            categoria = input("Error, esa categoria ya existe, ponga una categoria nueva: ")
            idCategoria = categorias.validarCategoria(categoria)
        categorias.insertarCategoria(categoria)            # inserta la categoria
        categorias.viewCategorias()                        
        idCategoria = categorias.validarCategoria(categoria)         # saca el id de la categoria
        while idCategoria is None:
            categoria = input("Error, inserte la nueva categoria: ")
            categorias.insertarCategoria(categoria)
            idCategoria = categorias.validarCategoria(categoria)
        nombre = input("escriba el nombre del objeto: ")
        descripcion = input("escriba una descripcion del objeto: ")
        precio = float(input("escriba el precio del objeto: "))
        cantidad = int(input("escriba la cantidad de productos: "))
        productos.insertarProducto(nombre, idCategoria, descripcion, precio, cantidad)



    def getInsertProducto(self):
        print("Presione 1 si quiere añadir una nueva categoria: ")
        print("Presione 2 si la categoria ya existe: ")
        opcion = input("")
        if opcion== "1":
            self.getInsertCategoria()
        elif opcion == "2":
            categorias.viewAllCategorias()
            print("")
            categoria = input("Escriba la categoria del producto: ")
            idCategoria = categorias.validarCategoria(categoria)

            while (idCategoria is None):
                categoria = input("Escriba una categoria que este registrada: ")
                idCategoria = categorias.validarCategoria(categoria)
    
            nombre = input("escriba el nombre del objeto: ")
            descripcion = input("escriba una descripcion del objeto: ")
            precio = input("escriba el precio del objeto: ")
            precio = float(precio)
            cantidad = int(input("escriba la cantidad de productos: "))
            productos.insertarProducto(nombre,idCategoria, descripcion, precio, cantidad)

        else:
            print("escriba un numero que este disponible")
            self.getInsertProducto()


    def getNombreProducto(self):             # ordena todos los productos por categorias
        categorias.getCategorias()
        opcion = input("seleccione una categoria: ")
        idCategoria = categorias.getIdCategoria(opcion)

        while not idCategoria:
            opcion = input("Error, seleccione una categoria: ")
            idCategoria = categorias.getIdCategoria(opcion)
        productos.getProducto(idCategoria)


    def getUpdateProducto(self):
        print("Oprima 1 si quiere cambiar el nombre del producto")
        print("Oprima 2 si quiere cambiar la descripcion del producto")
        print("Oprima 3 si quiere cambiar el precio del producto")
        print("Oprima 4 si quiere cambiar las existencias del producto")
        print("")
        opcion = input("")
        self.getNombreProducto()
        nombreActual = input("Seleccione el nombre actual: ")
        producto = productos.getIdProducto(nombreActual)
        while producto is None:
            nombreActual = input("Error, ponga el nombre del producto que quiere actualizar: ")
            producto = productos.getIdProducto(nombreActual)
            
        if opcion == "1":
            nuevoNombre = input("Ponga el nuevo nombre: ")
            productos.updateObjeto("nombre", nombreActual, nuevoNombre)
        elif opcion == "2":
            nuevaDescripcion = input("Ponga la nueva descripcion: ")
            productos.updateObjeto("descripcion", nombreActual, nuevaDescripcion)
        elif opcion == "3":
            nuevoPrecio = input("Ponga el nuevo precio: ")
            productos.updateObjeto("precio", nombreActual, nuevoPrecio)
        elif opcion == "4": 
            nuevaCantidad = input("Ponga la nueva cantidad: ")
            productos.updateObjeto("cantidad_disponible", nombreActual, nuevaCantidad)


    def getDeleteProducto(self):
        print("")
        self.getNombreProducto()
        nombre = input("ponga el nombre del producto que quiere eliminar: \n")
        producto = productos.getIdProducto(nombre)
        while producto is None:
            nombre = input("Error, ponga el nombre del producto que quiere eliminar: \n")
            producto = productos.getIdProducto(nombre)
        productos.deleteProducto(nombre)

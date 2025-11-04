"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Irene Carvajal Sánchez
Fecha: 4 noviembre 25

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, codigo,nombre, contacto):
        # TODO: definir los atributos de la clase
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        print(f"Proveedor: {self.nombre}, con contacto: {self.contacto}")


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        # TODO: definir los atributos de la clase
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor
        
    def __str__(self):
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        print(f"[{self.codigo}] {self.nombre} - {self.precio} € ({self.stock} uds.) | Proveedor: {self.proveedor})")


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        # TODO: definir los atributos e inicializar la lista de productos
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        try:
            #open("inventario.json", "r") as archivo:
            pass
        
        #Si hay un error, lo avisamos y mandamos una lista vacia
        except FileNotFoundError:
            print("Error")
            return []

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        # open 
        # for p in self.productos:
        #     datos = {"codigo":p.codigo,"nombre":p.nombre,"precio":p.precio,"stock":p.stock}
        #     json.dump(datos,"w")
        
        pass
    
    def anadir_producto(self, producto, codigo, precio=None, stock=None, prov=None):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo
        existe = False
        #Recorro la lista y compruebo si el codigo existe
        for p in self.productos:
            #Si existe avisa de que pruebe con otro y se sale del bucle
            if codigo == p.codigo:
                existe = True
                print("El codigo ya existe.Prueba con otro.")
                break
        #Si no existe lo añadimos
        if existe is False:
            nuevo = Producto(codigo,producto,precio,stock,prov)
            self.productos.append(nuevo)
            print("Producto añadido.")

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados
        for p in self.productos:
            p.__str__()

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código
        existe = False
        #Recorro la lista y compruebo si el codigo existe
        for p in self.productos:
            #Si existe lo muestro y me salgo del bucle
            if p.codigo == codigo:
                existe = True
                p.__str__()
                break
        #Si no existe le mando None
        if existe is False:
            print("None")

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        existe = False
        #Recorro la lista y compruebo si el codigo existe
        for p in self.productos:
            #Si existe modifico los datos introducidos, lo muestro y me salgo del bucle
            if p.codigo == codigo:
                existe = True
                
                if(nombre):
                    p.nombre = nombre
                if(precio):
                    p.precio = precio
                if(stock):
                    p.stock = stock
                
                print("Modificado: ")
                p.__str__()
                break
        #Si no existe avisamo al usuario
        if existe is False:
            print("Codigo del producto no encontrado.")

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        existe = False
        #Recorro la lista y compruebo si el codigo existe
        for p in self.productos:
            #Si existe lo elimino y aviso al usuario
            if p.codigo == codigo:
                existe = True
                self.productos.remove(p)
                print("Producto eliminado.")
                break
        #Si no existe aviso al usuario
        if existe is False:
            print("Producto no encontrado.")
            
    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        resultado = 0
        suma_total = 0
        #Recorro la lista y hago el calculo, despues se lo añado a la suma_total
        #Son cadenas debo pasarlo a numeros...
        for p in self.productos:
            resultado = float(p.precio) * int(p.stock)
            suma_total += resultado
        print("Valor total: ", suma_total, "€")
        
    def mostrar_por_proveedor(self, codigo_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    nombre_fichero = "gestion_inventario.py"
    inv = Inventario(nombre_fichero)
    inv.cargar()
    
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ").strip()

        # TODO: implementar las acciones correspondientes a cada opción del menú
        if opcion == "1":
            codigo = input("Codigo del producto a añadir: ")
            producto = input("Producto a añadir: ")
            precio = input("Precio del producto: ")
            stock = input("Stock del producto: ")
            prov = input("Proveedor del producto: ")
            inv.anadir_producto(producto, codigo, precio, stock, prov)
        elif opcion == "2":
            inv.mostrar()
        elif opcion == "3":
            codigo = input("Producto a buscar por codigo: ")
            inv.buscar(codigo)
        elif opcion == "4":
            codigo = input("Producto a modificar (codigo): ")
            nombre = input("Nombre nuevo: ")
            precio = input("Precio nuevo: ")
            stock = input("Stock nuevo: ")
            inv.modificar(codigo,nombre,precio,stock)
        elif opcion == "5":
            codigo = input("Producto a eliminar (codigo): ")
            inv.eliminar(codigo)
        elif opcion == "6":
            inv.valor_total()
        elif opcion == "7":
            codigo_proveedor = input("Mostrar por proveedor: ")
            inv.mostrar_por_proveedor(codigo_proveedor)
        elif opcion == "8":
            inv.guardar()
            break
        else:
            print("Opcion incorrecta. Vuelve a probar.")

if __name__ == "__main__":
    main()

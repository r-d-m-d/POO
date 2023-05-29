import json

from Lista import Lista
from Nodo import Nodo

from Vehiculo import Vehiculo
from Nuevos import Nuevos
from Usados import Usado

class Main:

    def __init__(self):
        self.__lista_vehiculos = Lista()

    def main(self):
       self.menuPrincipal() 

    def menuPrincipal(self):
        opciones =[
                'Insertar un vehículo en la colección en una posición determinada.',
                'Agregar un vehículo a la colección.',
                'Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.',
                'Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.',
                'Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.',
                'Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.',
                'Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.']
        for n, t in enumerate(opciones):
            print(f"{n+1}) {t}")
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            pass
        elif opc == "2":
            pass
        elif opc == "3":
            pass
        elif opc == "4":
            self.punto4()
        elif opc == "5":
            self.punto5()
        elif opc == "6":
            self.punto6()
        elif opc == "7":
            self.punto7()
        elif opc == "s":
            pass
        else:
            print("Opcion incorrecta")
    def crearNuevo(self):
        modelo = input("ingrese el modelo: ")
        np = int(input("ingrese el numero de puertas: "))
        color = input("Ingrese el color: ")
        precio = int(input("precio: "))
        version = input("version: ")
        return Nuevos(modelo, np, color, precio, version)

    def crearUsado(self):
        modelo = input("ingrese el modelo: ")
        np = int(input("ingrese el numero de puertas: "))
        color = input("Ingrese el color: ")
        precio = int(input("precio: "))
        marca = input("marca: ")
        patente = input("patente: ")
        anio = int(input("Año: "))
        kilom = int(input("Kilometraje: "))
        return Usado(modelo, np, color, precio, marca, patente, anio, kilom)


    def cargarJson(self, jsonFn):
        with open(jsonFn) as fp:
            data = json.load(fp)
        for vehiculo_data in data:
            modelo = vehiculo_data["modelo"]
            puertas = vehiculo_data["cantidad_puertas"]
            color = vehiculo_data["color"]
            precio = vehiculo_data["precio_base"]
            vehiculo = None
            if vehiculo_data["__class__"] == "Nuevo":
                version = vehiculo_data["version"]
                vehiculo = Nuevos(modelo, puertas, color, precio, version)
            elif vehiculo_data["__class__"] == "Usado":
                marca = vehiculo_data["marca"]
                patente = vehiculo_data["patente"]
                anio = vehiculo_data["anio"]
                kilometraje = vehiculo_data["kilometraje"]
                vehiculo = Usado(modelo, puertas, color, precio, marca,
                                 patente, anio, kilometraje)
            if vehiculo is not None:
                nodo = Nodo(vehiculo)
                self.__lista_vehiculos.agregarElemento(nodo)

    def insertarVehiculo(self):
        v = None
        pos = int(input("ingrese la posicion a insertar el vehiculo: "))
        print("1) Nuevo")
        print("2) Usado")
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            v = self.crearNuevo()
        elif opc == "2":
            v = self.crearUsado()
        if v is not None:
            nv = Nodo(v)
            self.__lista_vehiculos.insertarElemento(nv, pos)

    def agregarVehiculo(self):
        v = None
        print("1) Nuevo")
        print("2) Usado")
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            v = self.crearNuevo()
        elif opc == "2":
            v = self.crearUsado()
        if v is not None:
            self.__lista_vehiculos.agregarVehiculo(v)

    def punto3(self):
        pos = int(input("Ingrese una posicion"))
        e = self.__lista_vehiculos.obtenerElemento(pos)
        print(e.tipo())

    def punto4(self):
        pat = input("Ingrese Pantente")
        i = iter(self.__lista_vehiculos)
        v = next(i, False)
        while isinstance(v, Vehiculo):
            v = next(i, False)
        if isinstance(v, Vehiculo):
            print(v.tipo())
        else:
            print("Patente no encontrada")

    def punto5(self):
        m = self.__lista_vehiculos.obtenerElemento(0).getDato()
        for v in self.__lista_vehiculos:
            if v.importeVenta() < m.importeVenta():
                m = v
        print(f"El vehiculo mas economico: {m}")

    def punto6(self):
        for v in self.__lista_vehiculos:
            print(v)
    def punto7(self):
        for v in self.__lista_vehiculos:
            print(v.toJson())

jsonFn = "vehiculos.json"

if __name__ == "__main__":
    m = Main()
    m.cargarJson(jsonFn)
    m.main()

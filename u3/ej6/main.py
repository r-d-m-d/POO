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
        pass

    def menuPrincipal(self):
        pass

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
            puertas = vehiculo_data["puertas"]
            color = vehiculo_data["color"]
            precio = vehiculo_data["precio"]

            if vehiculo_data["__class__"] == "Nuevos":
                version = vehiculo_data["version"]
                vehiculo = Nuevos(modelo, puertas, color, precio, version)
            elif vehiculo_data["__class__"] == "Usado":
                marca = vehiculo_data["marca"]
                patente = vehiculo_data["patente"]
                anio = vehiculo_data["anio"]
                kilometraje = vehiculo_data["kilometraje"]
                vehiculo = Usado(modelo, puertas, color, precio, marca,
                                 patente, anio, kilometraje)
            nodo = Nodo(vehiculo)
            self.__lista_vehiculos.agregarElemento(nodo)

    def insertarVehiculo(self):
        v = None
        pos = int(input("ingrese la pocicion a insertar el vehiculo: "))
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

jsonFn = "vehiculos.json"

if __name__ == "__main__":
    m = Main()
    m.cargarJson(jsonFn)
    m.main()

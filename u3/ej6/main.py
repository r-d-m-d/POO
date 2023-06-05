import datetime

from Nuevos import Nuevos
from Usados import Usado
from ManejaVehiculos import ManejaVehiculos


class Main:

    def __init__(self):
        self.__mv = ManejaVehiculos()

    def cargarJson(self, fn):
        self.__mv.cargarArchivo(fn)

    def main(self):
        opc = ""
        while opc.lower() != 's':
            opc = self.menuPrincipal()

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
        print("s) Salir.")
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            self.insertarVehiculo()
        elif opc == "2":
            self.agregarVehiculo()
        elif opc == "3":
            self.punto3()
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
        return opc
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
            self.__mv.insertarVehiculo(v, pos)

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
            self.__mv.agregarVehiculo(v)

    def punto3(self):
        pos = int(input("Ingrese una posicion"))
        e = self.__mv.punto3(pos)
        print(e.getDato().tipo())

    def punto4(self):
        pat = input("Ingrese Pantente")
        v = self.__mv.buscarPatente(pat)
        if isinstance(v, Usado):
            np = int(input("Ingrese un nuevo precio: "))
            v.precio(np)
            print(f"El nuevo precio de venta: {v.importeVenta()}")
        else:
            print("Patente no encontrada")

    def punto5(self):
        m = self.__mv.vehiculoMasEconomico()
        print(f"El vehiculo mas economico: {m}")

    def punto6(self):
        print(self.__mv.listarVehiculos())

    def punto7(self):
        filename = f"vehiculos-{datetime.date.today()}.json"
        ifn = input(f"Ingrese un nombre de archivo({filename}): ")
        if ifn == "":
            ifn = filename
        self.__mv.guardarVehiculos(ifn)


jsonFn = f"vehiculos-{datetime.date.today()}.json"
if __name__ == "__main__":
    m = Main()
    j = input(f"Ingrese el nombre del json({jsonFn}): ")
    if j == "":
        j = jsonFn
    m.cargarJson(j)
    m.main()

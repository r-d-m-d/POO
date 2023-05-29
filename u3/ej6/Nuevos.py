
from Vehiculo import Vehiculo


class Nuevos(Vehiculo):

    __marca = ""

    def __init__(self, modelo, numero_puertas, color, precio, version):
        super().__init__(modelo, numero_puertas, color, precio)
        self.__version = version
        if version == "Full":
            self.__importe_venta = precio * (1+.1+.2)
        else:
            self.__importe_venta = precio * (1+.1)


    def version(self):
        return self.__version

    def importeVenta(self):
        return self.__importe_venta

    @classmethod
    def fijarMarca(cls, marca):
        cls.__marca = marca

    @classmethod
    def marca(cls):
        return cls.__marca

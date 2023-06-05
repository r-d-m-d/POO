
from Vehiculo import Vehiculo


class Nuevos(Vehiculo):

    __marca = ""

    def __init__(self, modelo, numero_puertas, color, precio, version):
        super().__init__(modelo, numero_puertas, color, precio)
        self.__version = version


    def version(self):
        return self.__version

    def importeVenta(self):
        if self.__version == "Full":
            importe_venta = self.precio() * (1+.1+.2)
        else:
            importe_venta = self.precio() * (1+.1)
        return importe_venta

    def tipo(self):
        return "Nuevos"

    def __str__(self):
        r = super().__str__()
        r += f"{self.__version} {self.importeVenta()}"
        return r

    def toJson(self):
        d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    modelo = self.modelo(),
                    numero_puertas = self.numeroPuertas(),
                    color = self.color(),
                    precio = self.precio(),
                    version = self.__version

                        )
                )
        return d

    @classmethod
    def fijarMarca(cls, marca):
        cls.__marca = marca

    @classmethod
    def marca(cls):
        return cls.__marca

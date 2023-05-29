
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

    def tipo(self):
        return "Nuevos"

    def __str__(self):
        r = super().__str__()
        r += f"{self.__version} {self.__importe_venta}"
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

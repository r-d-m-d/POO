from datetime import date

from Vehiculo import Vehiculo


class Usado(Vehiculo):

    __anio = date.today().year

    def __init__(self, modelo: str, numero_puertas: int, color: str, precio: int,
                 marca: str, patente: str, anio: int, kilometraje: int):
        super().__init__(modelo, numero_puertas, color, precio)
        self.__marca = marca
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje

    def marca(self):
        return self.__marca

    def patente(self):
        return self.__patente

    def anio(self):
        return self.__anio

    def kilometraje(self):
        return self.__kilometraje

    def importeVenta(self):
        return self.precio() * (1 - self.__descuento())

    def __descuento(self):
        descu = (Usado.__anio - self.__anio) / 100
        return descu if self.__kilometraje > 100000 else 2 * descu

    def tipo(self):
        return "Usado"

    def __str__(self):
        r = super().__str__()
        r += f"{self.__marca} {self.__patente} {self.__anio} {self.__kilometraje} {self.importeVenta()}"
        return r

    def toJson(self):
        d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    modelo = self.modelo(),
                    patente = self.patente(),
                    numero_puertas = self.numeroPuertas(),
                    color = self.color(),
                    precio = self.precio(),
                    marca = self.marca(),
                    anio = self.__anio,
                    kilometraje = self.__kilometraje
                    )
                )
        return d

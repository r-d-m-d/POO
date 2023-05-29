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
        self.__importe_venta = precio * (1 - self.__descuento())

    def marca(self):
        return self.__marca

    def patente(self):
        return self.__patente

    def anio(self):
        return self.__anio

    def kilometraje(self):
        return self.__kilometraje

    def importeVenta(self):
        return self.__importe_venta

    def __descuento(self):
        descu = (Usado.__anio - self.__anio) / 100
        return descu if self.__kilometraje > 100000 else 2 * descu

import typing


class Vehiculo:

    def __init__(self,modelo: str, numero_puertas: int, color: str, precio: int):
        self.__modelo = modelo
        self.__numero_puertas = numero_puertas
        self.__color = color
        self.__precio = precio

    def modelo(self):
        return self.__modelo

    def numeroPuertas(self):
        return self.__numero_puertas

    def color(self):
        return self.__color

    def precio(self):
        return self.__precio









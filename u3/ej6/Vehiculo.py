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

    def precio(self, nuevoPrecio=None):
        if isinstance(nuevoPrecio, int):
            self.__precio = nuevoPrecio
        return self.__precio

    def tipo(self):
        pass

    def __str__(self):
        return f"{self.__modelo} {self.__numero_puertas} {self.__color} {self.__precio}"


    def toJson(self):
        pass

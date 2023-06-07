from Vehiculo import Vehiculo


class Nodo:
    __vehiculo: Vehiculo
    __siguiente: object

    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo
        self.__sig = None

    def setSiguiente(self, nodo):
        self.__sig = nodo

    def getDato(self):
        return self.__vehiculo

    def getSiguiente(self):
        return self.__sig
    
    def toJson(self):
        return self.__vehiculo.toJson()

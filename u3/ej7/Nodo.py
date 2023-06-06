from Personal import Personal


class Nodo:
    __personal: Personal
    __siguiente: object

    def __init__(self, personal):
        self.__personal = personal
        self.__sig = None

    def setSiguiente(self, nodo):
        self.__sig = nodo

    def getDato(self):
        return self.__personal

    def getSiguiente(self):
        return self.__sig

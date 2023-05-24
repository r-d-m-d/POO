

class Taller:

    def __init__(self, idTaller, nomb, vac, mi):
        self.__idTaller = idTaller
        self.__nomb = nomb
        self.__vac = vac
        self.__montoInsc = mi

    def idTaller(self):
        return self.__idTaller

    def nomb(self):
        return self.__nomb

    def vac(self):
        return self.__vac

    def montoInsc(self):
        return self.__montoInsc

    def decVacates(self):
        self.__vac -= 1

    def __str__(self):
        return f"{self.__idTaller}) {self.__nomb}"

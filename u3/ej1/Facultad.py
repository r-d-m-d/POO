from Carrera import Carrera
class Facultad:
    __codigo = 0
    __nomb = ""
    __dire = ""
    __loc = ""
    __tel = ""
    __lCarr = []
    def __init__(self, codigo, nomb, dire, loc, tel):
        self.__codigo = codigo
        self.__nomb = nomb
        self.__dire = dire
        self.__loc = loc
        self.__tel = tel
        self.__lCarr = []

    def agregarCarrera(self, c):
        if isinstance(c,Carrera):
            self.__lCarr.append(c)
            c.setFacu(self)
    def __str__(self):
        x = f"{self.__nomb} {self.__dire} {self.__loc} {self.__tel}\n"
        for carr in self.__lCarr:
            x += f"{carr}\n"
        return x
    def __eq__(self, o):
        f = False
        if isinstance(o,int):
            f = self.__codigo == o
        elif isinstance(o,Facultad):
            f = self.__codigo == o.__codigo
        return f
    def tieneCarrera(self, nomb):
        i = 0
        while i < len(self.__lCarr) and not self.__lCarr[i].esNombre(nomb):
            i += 1
        carr = None
        if i < len(self.__lCarr) and self.__lCarr[i].esNombre(nomb):
            carr = self.__lCarr[i]
        return carr

    def strNombDir(self):
        return f"{self.__nomb} {self.__loc}"

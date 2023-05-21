

class Helado:
    __gramos = 0.0
    __precio = 0.0
    __sabores = []

    MAX_SABORES = 4
    __pesajes = [100, 150, 250, 500, 1000]
    __precios = [x*10 for x in __pesajes]

    def __init__(self, gramos, precio):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []

    def __eq__(self, o):
        rtn = False
        if isinstance(o, Helado):
            rtn = self.__gramos == o.__gramos and self.__sabores == o.__sabores
        return rtn

    def agregarSabor(self, s):
        import Sabor
        if isinstance(s, Sabor.Sabor) and len(self.__sabores) < Helado.MAX_SABORES:
            self.__sabores.append(s)
            s.agregarHelado(self)

    def obtenerPesoPorSabor(self):
        return self.__gramos / len(self.__sabores)

    def tieneGramos(self,g):
        return self.__gramos == g

    def getSabores(self):
        return self.__sabores

    def getGramosId(self):
        return Helado.__pesajes.index(self.__gramos)

    def precio(self):
        return self.__precio

    @classmethod
    def getPesajes(cls, idp=None):
        rtn = None
        if idp is None:
            rtn = cls.__pesajes.copy()
        elif isinstance(idp, int):
            rtn = cls.__pesajes[idp]
        return rtn

    @classmethod
    def getPrecios(cls, idp=None):
        rtn = None
        if idp is None:
            rtn = cls.__precios.copy()
        elif isinstance(idp, int):
            rtn = cls.__precios[idp]
        return rtn

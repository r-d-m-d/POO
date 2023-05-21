

class Sabor:
    __idSabor = 0
    __ingredientes = ""
    __nombre = ""
    __helado = []
    def __init__(self, ids, ing, nomb):
        self.__idSabor = ids
        self.__ingredientes = ing
        self.__nombre = nomb
        self.__helado = []

    def agregarHelado(self, h):
        import Helado
        if isinstance(h, Helado.Helado):
            self.__helado.append(h)

    def __str__(self):
        return self.__nombre

    def numHelados(self):
        return len(self.__helado)

    def __eq__(self, o):
        rtn = False
        if isinstance(o, Sabor):
            rtn = o.__idSabor == self.__idSabor
        return rtn

    def estimarGramosVendidos(self):
        gv = 0
        for h in self.__helado:
            gv += h.obtenerPesoPorSabor()
        return gv

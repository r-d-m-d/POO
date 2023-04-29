class Punto:
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def fijarPunto(self, x=None, y=None):
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def mover(self, dx=0, dy=0):
        self.__x += dx
        self.__y += dy

    def retornaX(self):
        return self.__x

    def retornaY(self):
        return self.__y


class Ventana:
    __titulo = ""
    __vSupIzq = None
    __vInfDer = None

    def __init__(self, titulo="", x0=0, y0=0, x1=500, y1=500):
        self.__titulo = titulo
        self.__vSupIzq = Punto(x0, y0)
        self.__vInfDer = Punto(x1, y1)

    def mostrar(self):
        espIzq = " " * self.__vSupIzq.retornaX()
        ancho = self.ancho()
        alto = self.alto()
        print(""*self.__vSupIzq.retornaY())
        print(espIzq)
        print(espIzq+"-"*ancho)
        i = 0
        while i < alto:
            print(espIzq + "|"+"·"*(ancho-2) + "|")
            i += 1
        print(espIzq+"-"*ancho)

    def moverIzquierda(self, x):
        self.__vSupIzq.mover(dx=-x)
        self.__vInfDer.mover(dx=-x)

    def moverDerecha(self, x):
        self.__vSupIzq.mover(dx=x)
        self.__vInfDer.mover(dx=x)

    def bajar(self, x=1):
        self.__vSupIzq.mover(dy=x)
        self.__vInfDer.mover(dy=x)

    def subir(self, x=1):
        self.__vSupIzq.mover(dy=-x)
        self.__vInfDer.mover(dy=-x)

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__vInfDer.retornaY() - self.__vSupIzq.retornaY()

    def ancho(self):
        return self.__vInfDer.retornaY() - self.__vSupIzq.retornaX()

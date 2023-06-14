import re

class Complejo:
    __re: float
    __img: float

    def __init__(self, re, img):
        if isinstance(re, float) or isinstance(re, int):
            self.__re = re
        else:
            raise ValueError("Parte real no numerica")
        if isinstance(img, float) or isinstance(img, int):
            self.__img = img
        else:
            raise ValueError("Parte imaginaria no numerica")

    def re(self, re=None):
        if isinstance(re, float) or isinstance(re, int):
            self.__re = re
        return self.__re

    def img(self, img=None):
        if isinstance(img, float) or isinstance(img, int):
            self.__img = img
        return self.__img

    def __add__(self, o):
        rtn = 0
        if isinstance(o, Complejo):
            rtn = Complejo(self.__re + o.__re, self.__img + o.__img)
        elif isinstance(o, int) or isinstance(o, float):
            rtn = Complejo(self.__re + o, self.__img)
        return rtn

    def __mul__(self, o):
        rtn = 0
        if isinstance(o, Complejo):
            r = self.__re * o.__re - self.__img * o.__img
            img = self.__re * o.__img + o.__re * self.__img
            rtn = Complejo(r, img)
        elif isinstance(o, int) or isinstance(o, float):
            c = Complejo(o, 0)
            rtn = self.__mul__(c)
        return rtn

    def __div__(self, o):
        rtn = 0
        if isinstance(o, Complejo):
            d = o.__re**2 + o.__img ** 2
            r = (self.__re * o.__re + self.__img * o.__img)/d
            img = (o.__re * self.__img-self.__re * o.__img)/d
            rtn = Complejo(r, img)
        return rtn

    def __sub__(self, o):
        rtn = 0
        if isinstance(o, Complejo):
            rtn = Complejo(self.__re - o.__re, self.__img - o.__img)
        elif isinstance(o, int) or isinstance(o, float):
            rtn = Complejo(o, 0)
            rtn = self.__sub__(rtn)
        return rtn

    def __str__(self):
        return f"{self.__re}{self.__img:+}i"
#        return f"{self.__re}"

    def __eq__(self, o):
        return self.__re == o.__re and self.__img == o.__img

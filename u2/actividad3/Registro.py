

class Registro:
    __tempe = 0
    __pres = 0
    __hume = 0
    def __init__(self,t,h,p):
        self.__tempe = t
        self.__pres = p
        self.__hume = h

    def __str__(self):
        return f"{self.__tempe}\t{self.__pres}\t{self.__hume}"

    def huboMasTempeQue(self, t):
        return self.__tempe > t

    def huboMasPresQue(self, p):
        return self.__pres > p

    def huboMasHumeQue(self, h):
        return self.__hume > h

    def huboMenosTempeQue(self, t):
        return self.__tempe < t

    def huboMenosPresQue(self, p):
        return self.__pres < p

    def huboMenosHumeQue(self, h):
        return self.__hume < h

    def retornaTemp(self):
        return self.__tempe

    def retornaPres(self):
        return self.__pres

    def retornaHume(self):
        return self.__hume


class ValDiaHora:
    __val = 0
    __dia = 0
    __hora = 0

    def __init__(self, val=0, dia=0, hora=0):
        self.__val = val
        self.__dia = dia
        self.__hora = hora

    def cMinVal(self, val):
        return self.__val > val

    def cMaxVal(self, val):
        return self.__val < val

    def fijarEstado(self, dia, hora, val):
        self.__val = val
        self.__hora = hora
        self.__dia = dia
    def mostrarDiaYHora(self):
        return f"dia: {self.__dia} hora:{self.__hora} val:{self.__val}"

class MaxMin:
    def __init__(self, minval, maxval):
        self.__maxVal = ValDiaHora(val=maxval)
        self.__minVal = ValDiaHora(val=minval)

    def registraMaxOMin(self, val, dia, hora):
        # Comparar los val y swichiar o no
        if self.__maxVal.cMaxVal(val):
            self.__maxVal.fijarEstado(dia, hora, val)
        elif self.__minVal.cMinVal(val):
            self.__minVal.fijarEstado(dia, hora, val)
    
    def mostrarMaximosYMinimos(self,prePrompt=""):
        print(prePrompt)
        print(f"Valor maximo: {self.__maxVal.mostrarDiaYHora()}")
        print("Valor minimo: ", self.__minVal.mostrarDiaYHora())


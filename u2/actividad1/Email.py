class Email():
    __idc = ""
    __dom = ""
    __tipo = ""
    __cont = ""
    def __init__(self, idc="", dom="", tipo="", cont="1234"):
        self.__idc = idc
        self.__dom = dom
        self.__tipo = tipo
        self.__cont = cont

    def retornaEmail(self):
        return self.__idc+"@"+self.__dom+"."+self.__tipo

    def getDominio(self):
        return self.__dom

    def crearCuenta(self, correo, cont="default"):
        sat = correo.split("@")
        self.__idc = sat[0]
        domIdx = sat[1].index('.')
        self.__dom = sat[1][0:domIdx]
        self.__tipo = sat[1][domIdx+1:]
        self.__cont = cont

    def esContrasena(self, cont):
        return self.__cont == cont

    def cambiarContrasena(self, cont):
        self.__cont=cont



class Email():
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
        atidx = correo.index("@")
        self.__idc = correo[0:atidx]
        domIdx = correo.index(".")
        self.__dom = correo[atidx+1:domIdx]
        self.__tipo = correo[domIdx+1:]
        self.__cont = cont

    def esContrasena(self, cont):
        return self.__cont == cont

    def cambiarContrasena(self, cont):
        self.__cont=cont



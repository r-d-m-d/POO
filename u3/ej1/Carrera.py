class Carrera:
    # 1,1,BioIngenieria,Bioingeniero,Once Semestres,Grado
    __idFacu = 0
    __idCarr = 0
    __nombCarr = ""
    __nombTitu = ""
    __dura = ""
    __tipo = ""

    def __init__(self,idf, idc, nc, nt, dura, tipo):
        self.__idFacu = idf
        self.__idCarr = idc
        self.__nombCarr = nc 
        self.__nombTitu = nt 
        self.__dura = dura 
        self.__tipo = tipo 
        self.__facu = None

    def __str__(self):
        return f"{self.__idCarr} {self.__nombCarr} {self.__nombTitu} {self.__dura} {self.__tipo}"

    def esNombre(self, nomb):
        return self.__nombCarr == nomb

    def codStr(self):
        return f"{self.__idFacu}{self.__idCarr}\n"

    def setFacu(self, facu):
        import Facultad
        if isinstance(facu,Facultad.Facultad):
            self.__facu = facu

    def getFacu(self):
        return self.__facu

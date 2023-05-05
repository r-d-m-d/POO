
class PlanAhorro:
    __cod: int
    __modelo = ""
    __version = ""
    __importe = 0.0
    ncuotas = 30 
    ncuotaslic = 10 

    def __init__(self, cod, modelo, version, importe):
        self.__cod = cod
        self.__modelo = modelo
        self.__version = version
        self.__importe = importe

    def valorCuota(self):
        return (self.__importe / PlanAhorro.ncuotas) + self.__importe * 0.1

    def codigo(self):
        return self.__codigo

    def modelo(self):
        return self.__modelo

    def version(self):
        return self.__version

    def importe(self, nimp=None):
        if type(nimp) is type(float):
            self.__importe = nimp
        return self.__importe

    @classmethod
    def ncuotaslic(cls, ncl=None):
        if type(ncl) is type(int):
            cls.ncuotaslic = ncl
        return cls.ncuotaslic

    def montoLic(self):
        return self.valorCuota() * PlanAhorro.ncuotaslic

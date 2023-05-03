
class PlanAhorro:
    __cod: int
    __modelo = ""
    __version = ""
    __importe = 0.0
    __ncuotas = 0.0
    __ncuotaslic = 0.0

    def __init__(self, cod, modelo, version, importe, nc, ncl):
        self.__cod = cod
        self.__modelo = modelo
        self.__version = version
        self.__importe = importe
        self.__ncuotas = nc
        self.__ncuotaslic = ncl

    def valorCuota(self):
        return (self.__importe / self.__ncuotas) + self.__importe * 0.1

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

    def ncuotaslic(self, ncl=None):
        if type(ncl) is type(int):
            self.__ncuotaslic = ncl
        return self.__ncuotaslic

    def montoLic(self):
        return self.valorCuota() * self.__ncuotaslic

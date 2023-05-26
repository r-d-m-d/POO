import typing
import csv

from Contratado import Contratado


class ManejaContratados:
    __lcont: typing.List[Contratado]

    def __init__(self):
        self.__lcont: typing.List[Contratado.Contratado] = []

    def cargaContratados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                horas = int(line[6])
                vh = int(line[7])
                cont = Contratado(line[0], line[1], line[2], line[3],
                                  line[4], line[5], horas, vh)
                self.__lcont.append(cont)

    def agregarHoras(self, dni: str, horas: int):
        i = 0
        while i < len(self.__lcont) and not self.__lcont[i].tieneDni(dni):
            i += 1
        emp = False
        if i < len(self.__lcont) and self.__lcont[i].tieneDni(dni):
            self.__lcont[i].agregarHoras(horas)
            emp = True
        return emp



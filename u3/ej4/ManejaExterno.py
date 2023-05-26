import typing
import csv

import Externo.Externo


class ManejaExterno:
    __lext: typing.List[Externo]

    def __init__(self):
        self.__lext: typing.List[Externo] = []

    def cargaContratados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                mviatico = int(line[6])
                costoObra = int(line[7])
                montoSDV = int(line[8])
                ext = Externo(line[0], line[1], line[2], line[3],
                              line[4], line[5], mviatico, costoObra, montoSDV)
                self.__lext.append(ext)

    def totalTarea(self, tarea: str):
        i = 0
        while i < len(self.__lext) and (self.__lext[i].tareaFinalizada()\
                or not self.__lext[i].tieneTarea(tarea)):
            i += 1

        ext = None
        if i < len(self.__lext) and not self.__lext[i].tareaFinalizada()\
                and self.__lext[i].tieneTarea(tarea):
            ext = self.__lext[i]
        return ext




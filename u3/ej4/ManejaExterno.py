import typing
import csv

import Externo.Externo


class ManejaExterno:
    __lcont: typing.List[Externo]

    def __init__(self):
        self.__lcont: typing.List[Externo] = []

    def cargaContratados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                mviatico = int(line[6])
                costoObra = int(line[7])
                montoSDV = int(line[8])
                ext = Externo(line[0], line[1], line[2], line[3],
                              line[4], line[5], mviatico, costoObra, montoSDV)
                self.__lcont.append(ext)



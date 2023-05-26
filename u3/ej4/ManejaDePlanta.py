import typing
import csv

from DePlanta import DePlanta


class ManejaDePlanta:
    __lcont: typing.List[DePlanta]

    def __init__(self):
        self.__lcont: typing.List[DePlanta] = []

    def cargaContratados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                sueldo = int(line[5])
                antig = int(line[6])
                ext = DePlanta(line[0], line[1], line[2], line[3],
                               sueldo, antig)
                self.__lcont.append(ext)


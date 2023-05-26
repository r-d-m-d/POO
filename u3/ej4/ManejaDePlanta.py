import typing
import csv

from DePlanta import DePlanta
from Empleado import Empleado


class ManejaDePlanta:
    __lcont: typing.List[DePlanta]

    def __init__(self):
        self.__lcont: typing.List[DePlanta] = []

    def cargarEmpleados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                sueldo = int(line[4])
                antig = int(line[5])
                ext = DePlanta(line[0], line[1], line[2], line[3],
                               sueldo, antig)
                self.__lcont.append(ext)

    def cobranMenosDe(self, sueldo: int) -> typing.List[Empleado]:
        return [emp for emp in self.__lcont if emp.sueldo() < sueldo]

    def mostrarSueldo(self):
        return [f"{e.nomb()} {e.tel()} {e.sueldo()}" for e in self.__lcont]

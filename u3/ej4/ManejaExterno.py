import typing
import csv

from Externo import Externo
from Empleado import Empleado


class ManejaExterno:
    __lext: typing.List[Externo]

    def __init__(self):
        self.__lext: typing.List[Externo] = []

    def cargarEmpleados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                print(line)
                mviatico = int(line[7])
                costoObra = int(line[8])
                montoSDV = int(line[9])
                ext = Externo(line[0], line[1], line[2], line[3],
                              line[4], line[5],line[6], mviatico, costoObra, montoSDV)
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

    def cobranMenosDe(self, sueldo: int) -> typing.List[Empleado]:
        return [emp for emp in self.__lext if emp.sueldo() < sueldo]

    def mostrarSueldo(self):
        return [f"{e.nomb()} {e.tel()} {e.sueldo()}" for e in self.__lext]

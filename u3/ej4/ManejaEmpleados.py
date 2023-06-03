from csv import csv
import numpy as np

from Empleado import Empleado
from Contratado import Contratado
from DePlanta import DePlanta
from Externo import Externo


class ManejaEmpleados:

    def __init__(self, tam=3, inc = 3):
        self.__tam = tam
        self.__num = 0
        self.__inc = inc
        self.__arr = np.zeros(tam, dtype = Empleado)

    def cargarContratados(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                horas = int(line[6])
                vh = int(line[7])
                cont = Contratado(line[0], line[1], line[2], line[3],
                                  line[4], line[5], horas, vh)
                self.agregarEmpleado(cont)

    def cargarDePlanta(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                sueldo = int(line[4])
                antig = int(line[5])
                ext = DePlanta(line[0], line[1], line[2], line[3],
                               sueldo, antig)
            self.agregarEmpleado(ext)

    def cargarExternos(self, fn):
        with open(fn) as fp:
            reader = csv.reader(fp)
            for line in reader:
                print(len(line))
                mviatico = int(line[7])
                costoObra = int(line[8])
                montoSDV = int(line[9])
                ext = Externo(line[0], line[1], line[2], line[3],
                              line[4], line[5],line[6], mviatico, costoObra, montoSDV)
                self.agregarEmpleado(ext)

    def agregarEmpleado(self, e):
        if isinstance(e, Empleado):
            if self.__num >= self.__tam:
                self.__tam += self.__inc
                self.__arr = self.__arr.resize(self.__tam)
            self.__arr[self.__num] = e
            self.__num += 1

    def obtenerEmpleadoIdx(self, idx):
        if idx < len(self.__arr):
            return self.__arr[idx]

    def totalTarea(self, tarea):
        i = 0
        while i <len(self, self.__arr) and isinstance(self.__arr[i], Externo)\
                and (self.__arr[i].tareaFinalizada()\
                or not self.__lext[i].tieneTarea(tarea)):
                    i +=1
        ext = None
        if i < len(self.__arr) and isinstance(self.__arr[i])\
                and not self.__arr[i].tareaFinalizada()\
                and self.__arr[i].tieneTarea(tarea):
            ext = self.__arr[i]
        return ext

    def cobranMenosDe(self, sueldo):
        return [emp for emp in self.__arr if isinstance(emp, Empleado)
                and emp.sueldo < sueldo]

    def mostrarSueldo(self):
        return [f"{e.nomb()} {e.tel()} {e.sueldo()}" for e in self.__arr
                if isinstance(e, Empleado)]

    def agregarHoras(self, dni: str, horas: int):
        i = 0
        while i < len(self.__arr) and isinstance(self.__arr[i])\
                and not self.__lcont[i].tieneDni(dni):
            i += 1
        emp = False
        if i < len(self.__lcont) and self.__lcont[i].tieneDni(dni):
            self.__lcont[i].agregarHoras(horas)
            emp = True
        return emp

    

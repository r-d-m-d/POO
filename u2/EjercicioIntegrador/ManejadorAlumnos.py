import numpy as np
import csv

from Alumno import Alumno


class ManejadorAlumnos:

    def __init__(self,dim=3,inc=3):
        self.__incremento = inc
        self.__dimension = dim
        self.__cantidad = 0
        self.__alumnos = np.empty(dim,dtype=Alumno)
    
    def cargarAlumnos(self,filename):
        with open(filename,encoding="8859") as fp:
            fp.readline()
            reader = csv.reader(fp,delimiter=";")
            for line in reader:
                self.agregarAlumno(Alumno(*line))

    def agregarAlumno(self, alu):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad] = alu
        self.__cantidad += 1

    def retornaAlumnosOrdenados(self):
        alus = self.__alumnos[:self.__cantidad]
        alus.sort()
        return alus

    def obtenerAlumno(self,dni):
        i = 0
        alu = None
        while i < len(self.__alumnos) and self.__alumnos[i].tieneDni(dni):
            i += 1

        if i < len(self.__alumnos):
            alu = self.__alumnos[i]
        return alu

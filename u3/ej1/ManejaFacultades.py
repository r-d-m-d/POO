import csv

from Facultad import Facultad
from Carrera import Carrera
class ManejaFacultades:
    __facu = []

    def __init__(self):
        self.__facu =[]

    def cargarCsv(self, csvFileName):
        with open(csvFileName) as fp:
            reader = csv.reader(fp)
            i = -1
            for line in reader:
                # si linea formateada como facultad
                if line[1].isdigit():
                    idf = int(line[0])
                    idc = int(line[1])
                #   crear carrera
                    car = Carrera(idf,idc,line[2],line[3],line[4],line[5])
                #   agregar carreras a la ultima facultad
                    self.__facu[i].agregarCarrera(car)
                # si linea formateada como facultad
                else :
                    idf = int(line[0])
                #   crear el objeto Facultad
                    f = Facultad(idf, line[1], line[2], line[3],line[5])
                #   agregar la facultad a la lista
                    self.__facu.append(f) 
                    i += 1

    def __str__(self):
        x = ""
        for facu in self.__facu:
            x += f"{facu}\n"
        return x

    def getFacu(self,cod):
        facu = None
        i = self.__facu.index(cod)
        if i >= 0:
            facu = self.__facu[i]
        return facu

    def bucarCarrera(self, nomb):
        i = 0
        while i < len(self.__facu) and (self.__facu[i].tieneCarrera(nomb) is None):
            i += 1
        carr = None
        if i < len(self.__facu) and (self.__facu[i].tieneCarrera(nomb) is not None):
            carr = self.__facu[i].tieneCarrera(nomb)
        return carr

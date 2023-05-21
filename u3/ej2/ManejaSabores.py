import csv

import Sabor

class ManejaSabores:

    def __init__(self):
        self.__ls = []

    def cargarSabores(self,fn):
        with open(fn) as fp:
            fp.readline()
            reader = csv.reader(fp,delimiter=";")
            for fila in reader:
                ids = int(fila[0])
                s = Sabor.Sabor(ids,fila[1],fila[2])
                self.__ls.append(s)

    def getSabores(self):
        return self.__ls.copy()

    def saboresMasVendidos(self):
        sabores = self.__ls.copy()
        masVendidos = []
        for i in range(0, 5):
            h = max(sabores, key=lambda x: x.numHelados())
            sabores.remove(h)
            masVendidos.append(h)
        return masVendidos

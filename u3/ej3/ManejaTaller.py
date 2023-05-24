import csv
import numpy as np

import Taller
class ManejaTaller:


    def __init__(self):
        self.__aTaller = None
        self.__nt = None

    def cargarArchivo(self, narch):
        with open(narch) as fp:
            n = fp.readline()
            idx = 0
            if n.isdigit():
                ntalleres = int(n)
                self.__aTaller = np.array(ntalleres, dtype=Taller.Taller)
                reader = csv.reader(fp)
                for line in reader:
                    idt = int(line[0])
                    vac = int(line[2])
                    monto = int(line[3])
                    self.__aTaller[idx] = Taller.Taller(idt, line[1],
                                                        vac, monto)
                    idx += 1
                self.__nt = idx

    def mostrarTalleres(self):
        for t in self.__aTaller:
            print(f"{t}")


import numpy as np
import csv

class ManejaInscipciones(np.ndarray):

    def __new__(subtype, shape, dtype=float, buffer=None, offset=0,
                strides=None, order=None, info=None):
        obj = super().__new__(subtype, shape, dtype,
                              buffer, offset, strides, order)
        obj.info = info
        return obj

    def __init__(self,shape,dtype=float ):
        super().__init__()
        self.__size = shape
        self.reshape((shape,))


    def mostrarInscripcionesTaller(self, tid):
        for insc in self:
            if insc.taller().idTaller() == tid:
                print(insc.persona())

    def guardarInscripciones(self,fn):
        with open(fn,"w") as fp:
            writer = csv.writer(fp)
            for insc in self:
                dni = insc.persona().dni()
                idt = insc.taller().idTaller()
                fecha = insc.fecha()
                pago = insc.pago()
                writer.writerow([dni, idt, fecha, pago])

    def append(self, el):
        print(self.__size)
        self.__size += 1
        print(self.__size)
        self = self.reshape(self.__size)
        self[self.__size-1] = el

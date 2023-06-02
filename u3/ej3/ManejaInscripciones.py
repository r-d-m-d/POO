import numpy as np
import csv

from Inscripcion import Inscripcion

class ManejaInscipciones():

    def __init__(self, size=3, inc=3):
        self.__dimension = size
        self.__cantidad = 0
        self.__incremento = inc
        self.__inscArr = np.ndarray(size, dtype=Inscripcion)

    def agregarInscripcion(self, inscr):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscArr.resize(self.__dimension)
        self.__inscArr[self.__cantidad] = inscr
        self.__cantidad += 1

    def mostrarInscripcionesTaller(self, tid):
        for insc in self.__inscArr:
            if insc.taller().idTaller() == tid:
                print(insc.persona())

    def guardarInscripciones(self, fn):
        with open(fn, "w") as fp:
            writer = csv.writer(fp)
            for insc in self.__inscArr:
                if isinstance(insc, Inscripcion):
                    dni = insc.persona().dni()
                    idt = insc.taller().idTaller()
                    fecha = insc.fechaInsc()
                    pago = insc.pago()
                    writer.writerow([dni, idt, fecha, pago])

    def buscarInscripcionPorDni(self, dni):
        i = 0
        while i < len(self.__inscArr)\
                and isinstance(self.__inscArr[i], Inscripcion)\
                and self.__inscArr[i].persona().dni() != dni:
            i += 1
        p = None
        if i < len(self.__inscArr)\
                and isinstance(self.__inscArr[i], Inscripcion)\
                and self.__inscArr[i].persona().dni() == dni:
            p = self.__inscArr[i]
        return p

    def consultarInscripcion(self, dni):
        s = "No se encontro ningun inscripto"
        inscr = self.buscarInscripcionPorDni(dni)
        if isinstance(inscr, Inscripcion):
            s = f"{inscr.persona().nom()}"
            if inscr.pago():
                s += f"\nTaller Pago"
            else:
                s += f"\n{inscr.taller().montoInsc()}"

    def consultarInscriptos(self, idt):
        s = ""
        for insc in self.__inscArr:
            if isinstance(insc, Inscripcion)  and insc.taller().idTaller() == idt:
                s += str(insc.persona()) + "\n"

    def registrarPago(self, dni):
        p = self.buscarInscripcionPorDni(dni)
        if isinstance(p, Inscripcion):
            p.registrarPago()


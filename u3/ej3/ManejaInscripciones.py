import numpy as np
import csv

class ManejaInscipciones(np.ndarray):


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

import csv
from typing import List
import ViajeroFrecuente


class ControladorViajeroFrecuente():
    __listaViajeros: List[ViajeroFrecuente.ViajeroFrecuente]

    def __init__(self):
        self.__listaViajeros = []

    def cargarViajeros(self, filename):
        fp = open(filename)
        csvReader = csv.reader(fp)
        for line in csvReader:
            num = int(line[0])
            millas = int(line[4])
            v = ViajeroFrecuente.ViajeroFrecuente(num, line[1], line[2],
                                                  line[3], millas)
            self.__listaViajeros.append(v)
        fp.close()

    def buscarViajeroPorNumero(self, num):
        return [v for v in self.__listaViajeros if v.tieneNumero(num)]

    def consultarMillas(self, num_viajero):
        millas = None
        v = self.buscarViajeroPorNumero(num_viajero)
        if v != []:
            millas = v[0].cantidadTotalDeMillas()
        return millas

    def acumularMillas(self, num_viajero, millas):
        if millas < 0:
            millas = None
        else:
            v = self.buscarViajeroPorNumero(num_viajero)
            if v != []:
                vi: ViajeroFrecuente.ViajeroFrecuente = v[0]
                millas = vi.acumularMillas(millas)
        return millas

    def canjearMillas(self, num, millas):
        if millas < 0:
            millas = None
        else:
            v = self.buscarViajeroPorNumero(num)
            if v != []:
                millas = v[0].canjearMillas(millas)
            else:
                millas = None
        return millas

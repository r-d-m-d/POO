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
        v = None
        i = 0
        while i < len(self.__listaViajeros) and not self.__listaViajeros[i].tieneNumero(num) :
            i += 1
        if i < len(self.__listaViajeros):
            v = self.__listaViajeros[i]
        return v

    def consultarMillas(self, num_viajero):
        millas = None
        v = self.buscarViajeroPorNumero(num_viajero)
        if v is not None:
            millas = v.cantidadTotalDeMillas()
        return millas

    def acumularMillas(self, num_viajero, millas):
        if millas < 0:
            millas = None
        else:
            v = self.buscarViajeroPorNumero(num_viajero)
            if v is not None:
                vi: ViajeroFrecuente.ViajeroFrecuente = v
                millas = vi.acumularMillas(millas)
        return millas

    def canjearMillas(self, num, millas):
        if millas < 0:
            millas = None
        else:
            v = self.buscarViajeroPorNumero(num)
            if v is not None:
                millas = v[0].canjearMillas(millas)
            else:
                millas = None
        return millas

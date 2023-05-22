from Taller import Taller
from Persona import Persona

class Inscripcion:


    def __init__(self,fechaInsc, persona, taller):
        self.__fechaInsc = fechaInsc
        self.__pago = False
        self.__persona = persona
        self.__taller = taller
        taller.decVacantes()

    def fechaInsc(self):
        return self.__fechaInsc

    def pago(self):
        return self.__pago

    def persona(self):
        return self.__persona

    def taller(self):
        return self.__taller

    def registrarPago(self):
        self.__pago = True

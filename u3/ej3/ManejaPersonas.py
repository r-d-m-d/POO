from Persona import Persona

class ManejaPersona():

    def __init__(self):
        self.__lp = []

    def agregarPersona(self, p):
        if isinstance(p, Persona):
            self.__lp.append(p)

from Personal import Personal

class Investigador(Personal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__area = kwargs['area']
        self.__tipo = kwargs['tipo']

    def area(self):
        return self.__area

    def tipo(self):
        return self.__tipo

    def sueldo(self):
        return self.sueldo_basico() + self.bono_por_antiguedad()


class Personal:
    def __init__(self, **kwargs):
        self.__cuil = kwargs['cuil']
        self.__apellido = kwargs['apellido']
        self.__nombre = kwargs['nombre']
        self.__sueldo_basico = kwargs['sueldo_basico']
        self.__antiguedad = kwargs['antiguedad']

    def cuil(self):
        return self.__cuil

    def apellido(self):
        return self.__apellido

    def nombre(self):
        return self.__nombre

    def sueldo_basico(self):
        return self.__sueldo_basico

    def antiguedad(self):
        return self.__antiguedad

    def bono_por_antiguedad(self):
        return self.__sueldo_basico * (self.__antiguedad / 100)

    def sueldo(self):
        pass


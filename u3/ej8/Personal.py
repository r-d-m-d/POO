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

    def sueldo_basico(self, sueldo_basico=None):
        if isinstance(sueldo_basico, int):
            self.__sueldo_basico = sueldo_basico
        return self.__sueldo_basico


    def antiguedad(self):
        return self.__antiguedad

    def bono_por_antiguedad(self):
        return self.__sueldo_basico * (self.__antiguedad / 100)

    def sueldo(self):
        pass

    def __lt__(self, o):
        return self.__apellido < o.__apellido

    def __str__(self):
        return f"{self.apellido()} {self.nombre()}"

    def toJson(self):
        d ={"__class__":self.__class__.__name__,
            "__atributos__":{
                "cuil": self.cuil(),
                "apellido": self.apellido(),
                "nombre": self.nombre(),
                "sueldo_basico": self.sueldo_basico(),
                "antiguedad": self.antiguedad(),

                }}
        return d

    def tipo(self):
        pass

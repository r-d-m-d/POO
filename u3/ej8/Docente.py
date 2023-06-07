from Personal import Personal


class Docente(Personal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__carrera = kwargs['carrera']
        self.__cargo = kwargs['cargo']
        self.__catedra = kwargs['catedra']

    def carrera(self):
        return self.__carrera

    def cargo(self, cargo=None):
        if cargo in ['simple', 'semiexclusivo', 'exclusivo']:
            self.__cargo = cargo
        return self.__cargo

    def catedra(self):
        return self.__catedra
# Consulta como setear el porcentaje por cargo
    def bono_por_cargo(self):
        p = 0
        if self.__cargo == 'simple':
            p = 0.1
        elif self.__cargo == 'semiexclusivo':
            p = 0.2
        elif self.__cargo == 'exclusivo':
            p = 0.5
        return self.sueldo_basico() * p

    def sueldo(self):
        return self.sueldo_basico() + self.bono_por_cargo() + self.bono_por_antiguedad()

    def toJson(self):
        d = Personal.toJson(self)
        d['__atributos__'].update({
                     "carrera": self.__carrera,
                     "cargo": self.__cargo,
                     "catedra": self.__catedra
                     })
        d['__class__'] = self.__class__.__name__
        return d

    def tipo(self):
        return "Docente"


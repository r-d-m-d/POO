from Investigador import Investigador
from Docente import Docente


class DocenteInvestigador(Docente, Investigador):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__categoria_investigacion = kwargs['categoria_investigacion']
        self.__importe_extra = kwargs['importe_extra']

    def categoria_investigacion(self):
        return self.__categoria_investigacion

    def importe_extra(self):
        return self.__importe_extra

    def sueldo(self):
        return super().sueldo() + self.importe_extra()


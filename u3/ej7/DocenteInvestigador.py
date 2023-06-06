from Personal import Personal
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

    def toJson(self):
        inv = Investigador.toJson(self)
        doc = Docente.toJson(self)
        inv['__atributos__'].update(doc['__atributos__'])
        inv['__atributos__'].update({
                    "categoria_investigacion": self.__categoria_investigacion,
                    "importe_extra": self.__importe_extra
                    })
        return inv

    def tipo(self):
        return "DocenteInvestigador"

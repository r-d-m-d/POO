from Personal import Personal

class Investigador(Personal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__area = kwargs['area']
        self.__tipo = kwargs['tipo']

    def area(self):
        return self.__area

    def tipo_investigacion(self):
        return self.__tipo

    def sueldo(self):
        return self.sueldo_basico() + self.bono_por_antiguedad()

    def toJson(self):
        d = Personal.toJson(self)
        d["__atributos__"].update({
                     "area": self.__area,
                     "tipo": self.__tipo,
                     })
        d["__class__"] = self.__class__.__name__
        return d

    def tipo(self):
        return "Investigador"

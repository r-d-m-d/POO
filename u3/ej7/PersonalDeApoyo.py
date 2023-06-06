from Personal import Personal


class PersonalDeApoyo(Personal):


    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__categoria = kwargs['categoria']

    def categoria(self):
        return self.__categoria

    def bono_por_categoria(self):
        p = 0
        if 1 <= self.__categoria <= 10:
            p = 0.1
        elif 11 <= self.__categoria <=20:
            p = 0.2
        elif 21 <= self.__categoria <=22:
            p = 0.3
        return self.sueldo_basico() * p

    def sueldo(self):
        return self.sueldo_basico() + self.bono_por_categoria() + self.bono_por_antiguedad()

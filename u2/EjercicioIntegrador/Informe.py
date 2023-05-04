
class Informe:
    def __init__(self,dni,nya,fecha,nota,anio):
        self.__dni = dni
        self.__nya = nya
        self.__fecha = fecha
        self.__nota = nota
        self.__anio = anio
    
    def __str__(self):
        return f"{self.__dni:^10}\t{self.__nya:^18}\t{self.__fecha:^12}\t{self.__nota:^3}\t{self.__anio:^3}"


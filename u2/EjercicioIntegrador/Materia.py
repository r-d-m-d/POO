

class Materia:
    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota if isinstance(nota,int) else int(nota)
        self.__aprobacion = aprobacion
    
    def  nota(self):
        return self.__nota
    def dni(self):
        return self.__dni

    def tieneNombre(self, nMateria):
        return self.__nombreMateria == nMateria
   
    def tieneAprobacion(self,ap):
        return self.__aprobacion == ap

    def tieneNota(self, nt):
        return self.__nota == nt

    def fecha(self):
        return self.__fecha
    def nombre(self):
        return self.__nombreMateria



class Alumno:

    def __init__(self,dni="",apellido="",nombre="",carrera="",anio=""):
        self.__dni = dni 
        self.__apellido = apellido 
        self.__nombre = nombre 
        self.__carrera = carrera 
        self.__anio = anio 

    def tieneDni(self,dni):
        return self.__dni == dni
    def nya(self):
        return self.__nombre+" "+self.__apellido
    def __lt__(self, o):
        rtn = False
        if isinstance(o, Alumno):
            if self.__anio != o.__anio:
                rtn = self.__anio < o.__anio
            elif self.__apellido != o.__apellido :
               rtn = (self.__apellido < o.__apellido)
            else:
                rtn = (self.__nombre < o.__nombre)
        elif isinstance(o, int):
            rtn = self.__anio < o
        return rtn   
    def __str__(self):
        return f"{self.__anio} {self.__apellido}  {self.__nombre}  {self.__carrera}  {self.__dni}"
    def anio(self):
        return self.__anio

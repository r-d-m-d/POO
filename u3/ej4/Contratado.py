

import Empleado


class Contratado(Empleado.Empleado):

    def __init__(self, dni: str, nomb: str, dire: str, tel: str,
                 inicio: str, fin: str, horas: int, vh: int) -> None:
        super().__init__(dni, nomb, dire, tel)
        self.__inicio = inicio
        self.__fin = fin
        self.__horas = horas
        self.__vh = vh
        self.__sueldo = horas * vh

    def inicio(self) -> str:
        return self.__inicio

    def fin(self) -> str:
        return self.__fin

    def horas(self) -> int:
        return self.__horas

    def vh(self) -> int:
        return self.__vh

    def sueldo(self) -> int:
        return self.__sueldo

    def tieneDni(self, dni: str):
        return super.dni() == dni

    def agregarHoras(self, horas: int):
        self.__horas += horas

import Empleado


class DePlanta(Empleado.Empleado):


    def __init__(self, dni: str, nomb: str, dire: str, tel: str,
                 sueldo: int, antig: int) -> None:
        super().__init__(dni, nomb, dire, tel)
        self.__sueldo = sueldo
        self.__antig = antig

    def sueldo(self) -> int:
        return self.__sueldo + (0.01*self.__antig)

    def antig(self) -> int:
        return self.__antig


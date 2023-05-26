import Empleado


class Externo(Empleado.Empleado):

    def __init__(self, dni: str, nomb: str, dire: str, tel: str,
                 tarea: str, fi: str, ff: str, mviatico: int, costoObra: int,
                 montoSDV: int) -> None:
        super().init(dni, nomb, dire, tel)
        self.__tarea = tarea
        self.__fi = fi
        self.__ff = ff
        self.__mviatico = mviatico
        self.__costoObra = costoObra
        self.__montoSDV = montoSDV
        self.__sueldo = costoObra - mviatico - montoSDV

    def tarea(self) -> str:
        return self.__tarea

    def fi(self) -> str:
        return self.__fi

    def ff(self) -> str:
        return self.__ff

    def mviatico(self) -> int:
        return self.__mviatico

    def costoObra(self) -> int:
        return self.__costoObra

    def montoSDV(self) -> int:
        return self.__montoSDV

    def sueldo(self) -> int:
        return self.__sueldo










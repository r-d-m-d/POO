import typing


class Empleado:
    
    def __init__(self, dni: str, nomb: str, dire: str, tel: str) -> None:
        self.__dni = dni
        self.__nomb = nomb
        self.__dire = dire
        self.__tel = tel

    def dni(self) -> str:
        return self.__dni

    def nomb(self) -> str:
        return self.__nomb

    def dire(self) -> str:
        return self.__dire

    def tel(self) -> str:
        return self.__tel

    def __str__(self) -> str:
        return f"{self.__nomb} {self.__dire} {self.__dni}"



class Persona:

    def __init__(self,nom,dire,dni):
        self.__nom = nom
        self.__dire = dire
        self.__dni = dni

    def nom(self):
        return self.__nom

    def dire(self):
        return self.__dire

    def dni(self):
        return self.__dni

    def __str__(self):
        return f"{self.__nom} {self.__dire} {self.__dni}"

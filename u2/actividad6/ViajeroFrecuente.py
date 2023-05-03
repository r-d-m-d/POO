class ViajeroFrecuente():
    __num_viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0

    def __init__(self, numv, dni, nombre, apellido, millas):
        self.__num_viajero = numv
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def cantidadTotalDeMillas(self):
        return self.__millas_acum

    def acumularMillas(self, mill):
        self.__millas_acum += mill
        return self.__millas_acum

    def puedeCanjear(self, millas):
        return self.__millas_acum >= millas

    def canjearMillas(self, millas_canje):
        if self.puedeCanjear(millas_canje):
            self.__millas_acum -= millas_canje
        return self.__millas_acum

    def tieneNumero(self, numero):
        return numero == self.__num_viajero

    def __gt__(self, otro):
        return self.__millas_acum > otro.__millas_acum

    def __add__(self, millas):
        if type(millas) == int:
            self.acumularMillas(millas)
        return self

    def __sub__(self, millas):
        if type(millas) == int:
            self.canjearMillas(millas)
        return self

    def __str__(self):
        return f"{self.__num_viajero}   {self.__dni}   {self.__nombre}   {self.__apellido}   {self.__millas_acum}"

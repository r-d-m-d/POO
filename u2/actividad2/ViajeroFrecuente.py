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
        return self.__millas_acum+mill

    def puedeCanjear(self, millas):
        return self.__millas_acum >= millas

    def canjearMillas(self, millas_canje):
        if self.puedeCanjear(millas_canje):
            self.__millas_acum -= millas_canje
        return self.__millas_acum

    def tieneNumero(self, numero):
        return numero == self.__num_viajero

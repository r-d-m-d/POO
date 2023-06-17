import json

from peliculas import Pelicula

class Genero:

    def __init__(self, idg, nombre):
        self.__idg = idg
        self.__nombre = nombre

    def tieneId(self, idg):
        return self.__idg == idg

    def __str__(self):
        return f'{self.__nombre}'

    def __eq__(self, o):
        return o.__idg == self.__idg

    def __lt__(self, o):
        rtn = False
        if isinstance(o, int):
            rtn = self.__idg < o
        elif isinstance(o, Genero):
            rtn = self.__idg < o.__idg
        return rtn

    def generoIdCmp(self, idg):
        return 0 if self.__idg == idg else ( -1 if self.__idg < idg else 1  )

class AlmacenGeneros:

    def __init__(self):
        self.__lg = []
        with open("generos.json") as fp:
            d = json.load(fp)
            for g in d['genres']:
                idg = g['id']
                nombre = g['name']
                genero = Genero(idg, nombre)
                self.__lg.append(genero)
        self.__lg.sort()

    def buscaGeneroPorId(self, idg):
        ini = 0
        fin = len(self.__lg)
        med = fin // 2
        while ini < fin and not self.__lg[med].tieneId(idg):
            idcmp = self.__lg[med].generoIdCmp(idg)
            if idcmp == -1:
                ini = med
            elif idcmp == 1:
                fin = med
            med = (ini+fin) // 2
        return self.__lg[med] if self.__lg[med].tieneId(idg) else None

    def obtenerGenerosStr(self, ids_generos: list):
        s = ""
        for idg in ids_generos:
            sg = self.buscaGeneroPorId(idg)
            if sg is not None:
                s += f"{sg}, "
        if s.endswith(', '):
            s = s[:len(s)-2]
        return s


if __name__ == "__main__":
    ag = AlmacenGeneros()
    i = int(input("Ingrese un genero: "))
    print(ag.buscaGeneroPorId(i))

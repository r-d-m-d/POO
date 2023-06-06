from Personal import Personal
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from Lista import Lista

class ManejaPersonal:

    def __init__(self):
        self.__lp = Lista()

    def insertarPersonal(self, p, pos):
        self.__lp.insertar_personal(p, pos)

    def agregarPersonal(self, p):
        self.__lp.agregar_personal(p)

    def obtenerElemento(self, n):
        return self.__lp.obtenerElemento(n)

    def listarDocenteInvestigadores(self):
        s = ""
        for d in self.__lp:
            if isinstance(d, DocenteInvestigador):
                s += f"{d}"

    def contarAgentesPorAreaDeInvestigacion(self):
        d = {}
        for i in self.__lp:
            if isinstance(i, Investigador):
                area = i.areas()
                if area in d.keys():
                    d[area] += 1
                else:
                    d[area] = 1
        return d

    def agentesOrdenadosPorApellido(self):
        pass

    def docentesInvestigadoresPorCategoria(self):
        pass

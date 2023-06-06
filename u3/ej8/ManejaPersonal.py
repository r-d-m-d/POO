import json

from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from PersonalDeApoyo import PersonalDeApoyo
from DocenteInvestigador import DocenteInvestigador
from Nodo import Nodo
from Lista import Lista


filename = "personal.json"


class ManejaPersonal:

    def __init__(self):
        self.__lp = Lista()

    def cargarArchivo(self, fn="personal.json"):
        with open(fn, "r", encoding="utf-8") as fp:
            vl = json.load(fp)
        for v in vl:
            self.__lp.agregar_personal(self.decodificarObjeto(v))

    def decodificarObjeto(self, d):
        obj = None
        try:
            nombre_clase = d['__class__']
            class_ = eval(nombre_clase)
            atributos = d['__atributos__']
            obj = class_(**atributos)
        except KeyError as err:
            print("Key Error: Archivo json mal formateado")
            print(nombre_clase," ",atributos)
            raise err
        except NameError as err:
            print("Clase de objeto no encontrado")
            print(nombre_clase)
        except TypeError as err:
            print("type Error: Archiv mal formateado")
            print(nombre_clase," ",atributos)
        except Exception as e:
            print("KBOOOOM")
            print(nombre_clase)
            raise e
        finally:
            pass
        return obj


    def insertarPersonal(self, p, pos):
        self.__lp.insertar_personal(p, pos)

    def agregarPersonal(self, p):
        self.__lp.agregar_personal(p)

    def obtenerElemento(self, n):
        e = self.__lp.obtenerElemento(n)
        d = e.getDato if isinstance(e, Nodo) else None
        return d
    def listarDocenteInvestigadoresPorCarrera(self):
        dipc = {}
        for pers in self.__lp:
            if isinstance(pers, DocenteInvestigador):
                carre = pers.carrera()
                if carre in dipc.keys():
                    dipc[carre] += [f"{pers}"]
                else:
                    dipc[carre] = [f"{pers}"]
        return dipc

    def contarAgentesPorAreaDeInvestigacion(self):
        d = {}
        for i in self.__lp:
            if isinstance(i, Investigador):
                area = i.area()
                if area in d.keys():
                    d[area] += 1
                else:
                    d[area] = 1
        return d

    def agentesOrdenadosPorApellido(self):
        return sorted(self.__lp)
    
    def docentesInvestigadoresPorCategoria(self):
        d = {}
        for i in self.__lp:
            if isinstance(i, DocenteInvestigador):
                categoria = i.categoria_investigacion()
                if categoria in d.keys():
                    d[categoria] += 1
                else:
                    d[categoria] = 1
        return d

    def guardar(self):
        with open(filename, "w", encoding="utf-8") as fp:
            json.dump(self.__lp.toJson(), fp, indent=4)
#        for x in self.__lp.toJson():
#            print(x)


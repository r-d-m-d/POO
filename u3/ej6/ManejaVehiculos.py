import json
import datetime

from Vehiculo import Vehiculo
from Usados import Usado
from Nuevos import Nuevos
from Lista import Lista
from Nodo import Nodo


class ManejaVehiculos:
    __lv: Lista

    def __init__(self):
        self.__lv = Lista()

    def cargarArchivo(self,fn=f"vehiculos-{datetime.date.today()}.json"):
        with open(fn) as fp:
            vl = json.load(fp)
        for v in vl:
            self.__lv.agregarVehiculo(self.decodificarObjeto(v))

    def decodificarObjeto(self, d):
        obj = None
        try:
            nombre_clase = d['__class__']
            class_ = eval(nombre_clase)
            atributos = d['__atributos__']
            obj = class_(**atributos)
        except KeyError as err:
            print("Archivo json mal formateado")
        except NameError as err:
            print("Clase de objeto no encontrado")
        except TypeError as err:
            print("Archiv mal formateado")
        except Exception as e:
            print("KBOOOOM")
            print(nombre_clase)
            raise e
        finally:
            pass
        return obj

    def insertarVehiculo(self, v, pos):
        nv = Nodo(v)
        self.__lv.insertarElemento(nv, pos)

    def agregarVehiculo(self, v):
        self.__lv.agregarVehiculo(v)

    def punto3(self, pos):
        return self.__lv.obtenerElemento(pos)

    def buscarPatente(self, pat):
        i = iter(self.__lv)
        v = next(i, False)
        while not isinstance(v, Usado) or v.patente() != pat:
            v = next(i, False)
        print(v.patente())
        if isinstance(v, Usado) and v.patente() != pat :
            v = None
        elif not isinstance(v, Usado):
            v = None
        return v

    def vehiculoMasEconomico(self):
        m = self.__lv.obtenerElemento(0).getDato()
        for v in self.__lv:
            # busca el minimo en la lista
            if v.importeVenta() < m.importeVenta():
                m = v
        return m

    def listarVehiculos(self):
        s = ""
        for v in self.__lv:
            s += f"{v}\n"
        return s

    def guardarVehiculos(self, filename):
        with open(filename, "w") as fp:
            json.dump(self.__lv.toJson(), fp, indent=4)


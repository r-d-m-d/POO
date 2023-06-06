from zope.interface import implementer

from Nodo import Nodo
from iColeccion import iColeccion

@implementer(iColeccion)
class Lista:
    __inicio: Nodo
    __fin: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self, nodo=None):
        self.__inicio = nodo
        self.__fin = nodo
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def agregarElemento(self, v: Nodo) -> None:
        if self.__fin is not None:
            self.__fin.setSiguiente(v)
            self.__fin = v
        else:
            self.__inicio = v
            self.__fin = v
            self.__actual = v
        self.__tope += 1

    def obtenerElemento(self, n):
        i = 0
        c = self.__inicio
        while c is not None and i < n:
            i += 1
            c = c.getSiguiente()
        elem = None
        if i == n and c is not None:
            elem = c
        return elem

    def insertarElemento(self, elem, pos):
        if self.__inicio is None:  # La lista esta vacia
            self.agregarElemento(elem)
        elif pos == 0:
            elem.setSiguiente(self.__inicio)
            self.__inicio = elem
            self.__actual = elem
        elif self.__inicio is not None:
            # buscamos el anterior a la posicion pos
            r = self.obtenerElemento(pos - 1)
            # Llegamos al final de la lista, r es el ultimo elemento
            if r.getSiguiente() is None:
                r.setSiguiente(elem)
                self.__fin = elem
            # la posicion es a la mistad de la lista
            else:
                #r es el elemento en la posicion anterior a pos
                s = r.getSiguiente()
                r.setSiguiente(elem)
                elem.setSiguiente(s)
            self.__tope += 1
            self.__actual = elem

    def mostrarElemento(self, elem):
        print(elem)

    def __iter__(self):
        self.__actual = self.__inicio
        self.__indice = 0
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__inicio
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregar_personal(self, v):
        n = Nodo(v)
        self.agregarElemento(n)

    def contiene_elemento(self, v):
        c = self.__inicio
        while c is not None and c.getDato() != v:
            c = c.getSiguiente()
        return c.getDato() == v if c is not None else False

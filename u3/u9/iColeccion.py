
from zope.interface import Interface
from zope.interface import implementer


class iColeccion(Interface):

    def insertarElemento(elem, pos):
        pass

    def agregarElemento(elem):
        pass

    def mostrarElemento(elem):
        pass

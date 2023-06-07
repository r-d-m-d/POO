from zope.interface import Interface


class IDirector(Interface):

    def modificarBasico(dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(dni, nuevoCargo):
        pass

    def modificarPorcentajeporcategoría(dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(dni, nuevoImporteExtra):
        pass

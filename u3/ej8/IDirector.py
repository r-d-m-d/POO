from zope.interface import Interface


class IDirector(Interface):

    def modificarBasico(self,dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(self,dni, nuevoCargo):
        pass

    def modificarPorcentajeporcategoría(self,dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(self,dni, nuevoImporteExtra):
        pass

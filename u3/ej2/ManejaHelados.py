import Helado


class ManejaHelados:

    def __init__(self):
        self.__lh = []

    def agregaHelados(self,h):
        if isinstance(h,Helado.Helado):
            self.__lh.append(h)

    def registrarHeladoVendido(self, gramosId, sabores):
        h = Helado.Helado(Helado.Helado.getPesajes(idp=gramosId),
                          Helado.Helado.getPrecios(idp=gramosId))
        for s in sabores:
            h.agregarSabor(s)
        self.agregaHelados(h)

    def obtenerHeladosDePesaje(self,gramosId):
        gr = Helado.Helado.getPesajes(gramosId)
        lhp = [h for h in self.__lh if h.tieneGramos(gr)]
        return lhp

    def informe(self):
        gr = Helado.Helado.getPesajes()
        ganancias = [0] * len(gr)
        for h in self.__lh:
            pesajeId = h.getGramosId()
            ganancias[pesajeId] += h.precio()
        for peso, g in zip(gr, ganancias):
            print(f"Para el tipo {peso} se gano {g}")

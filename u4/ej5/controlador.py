from vistaPeliculas import PeliculaView
from generos import AlmacenGeneros
from peliculas import ManejaPelicula



class controlador:
    
    def __init__(self):
        self.ag = AlmacenGeneros()
        self.pv = PeliculaView()
        self.mp = ManejaPelicula()

    # fija los titulos en el list box
        self.mp.enlistartTitulos(self.pv.agregarPelicula)
    # pasa una callback, al seleccionar un item ejecuta la funcion lambda
        self.pv.seleccionarPelicula(
            lambda x:
                self.pv.verPeliculaEnForm(*self.mp.obtenerDescripcion(x,self.ag))
        )

        self.pv.mainloop()
# El controlador seria el que relaciona los modelos, manejadores y vistas¿?


if __name__ == "__main__":
    controlador()



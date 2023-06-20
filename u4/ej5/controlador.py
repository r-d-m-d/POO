import requests
import json

from vistaPeliculas import PeliculaView
from generos import AlmacenGeneros
from peliculas import ManejaPelicula

class controlador:

    def __init__(self):
        self.ag = AlmacenGeneros()
        self.pv = PeliculaView()
        #-- Configurar Manejador de peliculas
        #- obtener la informacion de la api 
        resp = requests.get('https://api.themoviedb.org/3/discover/movie?page=1&api_key=51e0b298932d9b54c1521992a7dd529e')
        if isinstance(resp, requests.models.Response) and resp.status_code == 200:
            page = resp.json()
        else:
            with open('peliculas.json') as fp:
                page = json.load(fp)
        results = page['results']
        self.mp = ManejaPelicula(results)
        del (resp)
        del (page)
        del (results)
    # -- Configurar el view
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



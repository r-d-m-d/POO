import requests
import time


class APIDeDolar:
    __url: str
    __datos: float
    __interprete: object
    __reintentos: int
    __espera: int

    def __init__(self, url, interprete):
        self.__url = url
        self.__interprete = interprete
        self.__reintentos = 3
        self.__espera = 1  # Tiempo de espera inicial
        self.__datos = None
        self.obtenerDatos()

    def obtenerDatos(self):
        reintentos = self.__reintentos
        espera = self.__espera
        response = None
        while reintentos > 0:
            try:
                response = requests.get(self.__url)
                response.raise_for_status()  # Levantar un error http
            except requests.RequestException as e:
                print(f"Request failed: {e}")
                if reintentos > 0:
                    print(f"Retrying in {espera} seconds...")
                    time.sleep(espera)
                    espera *= 2  # Tiempo de espera exponecial
                else:
                    print("Max retries exceeded. Exiting.")
                    self.__datos = None
            else:
                self.__datos = self.__interprete(response)
                reintentos = 0
            reintentos -= 1

    @property
    def datos(self):
        return self.__datos

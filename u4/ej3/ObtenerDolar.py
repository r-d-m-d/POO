import requests

class APIDeDolar:
    __url: str
    __precio: float

    def __init__(self, url):
        self.__url = url
        self.__precio = self.obtenerDolar()

    def obtenerDolar(self):
        respose = requests.get(self.__url)
        jd = respose.json() if respose and respose.status_code == 200 else None
        tam = len(jd)
        i = 0
        precio_venta = 0
        while i < tam and jd[i]['casa']['nombre'] != 'Oficial':
            i += 1

        if i < tam and jd[i]['casa']['nombre'] == 'Oficial':
            precio_venta = float(jd[i]['casa']['venta'].replace(',', '.'))
        return precio_venta

    def precio(self):
        return self.__precio

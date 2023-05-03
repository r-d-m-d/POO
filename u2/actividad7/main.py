from ViajeroFrecuente import ViajeroFrecuente


if __name__ == "__main__":
    lv = [
            ViajeroFrecuente(1, 3214, "Medio", "Millas", 1234),
            ViajeroFrecuente(2, 54321, "Minimo", "Millas", 123),
            ViajeroFrecuente(0, 1234, "Maximo", "Millas", 1000000)
            ]
# 1- Comparar las cantidad de millas acumuladas de un viajero frecuente con un
# valor entero a través de la sobrecarga del operador igual (== o __eq__). Por
# ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible
# realizar tanto v ==  100 como 100 == v.
    assert lv[0] == 1234
    assert 1234 == lv[0]
# 2- Acumular millas se pueda resolver de la siguiente forma: sea v una instancia
# de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.
    100 + lv[0]
    assert lv[0] == 1334
# 3- Canjear millas se pueda resolver de la siguiente forma: sea v una instancia
# de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.
    100 - lv[0]
    assert 1234 == lv[0]

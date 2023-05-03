from ViajeroFrecuente import ViajeroFrecuente


if __name__ == "__main__":
    lv = [
            ViajeroFrecuente(1, 3214, "Medio", "Millas", 1234),
            ViajeroFrecuente(2, 54321, "Minimo", "Millas", 123),
            ViajeroFrecuente(0, 1234, "Maximo", "Millas", 1000000)
            ]
# 1- Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para
# distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de
# millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en
# python).
    print(max(lv))
# 2- Acumular millas usando la sobrecarga del operador binario suma(+),
# obteniendo como resultado de la suma una instancia de la clase
# ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase
# ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente
# forma v = v + 100.
    print("Acumulando millas")
    print(f"minimo antes: {lv[1]}")
    minimo = lv[1] + 200  # agrego 200 millas
    print(f"Minimo luego: {minimo}")
# 3- Canjear millas usando la sobrecarga del operador binario
# resta(-),obteniendo como resultado de la resta una instancia de la clase
# ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase
# ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente
# forma v = v - 100.
    print("Canjeando millas")
    print(f"minimo antes: {lv[1]}")
    minimo = lv[1] - 123  # canjeo millas
    print(f"Minimo luego: {minimo}")

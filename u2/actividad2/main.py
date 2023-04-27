import ViajeroFrecuente
import ControladorViajeroFrecuente

if __name__ == "__main__":
    cvf = ControladorViajeroFrecuente.ControladorViajeroFrecuente()
    cvf.cargarViajeros("viajerosFrecuentes.csv")
    vid = int(input("ingrese un id de viajero frecuente: "))
    viajeros = cvf.buscarViajeroPorNumero(vid)
    if viajeros is not None:
        viajero: ViajeroFrecuente.ViajeroFrecuente = viajeros
        del cvf
        del viajeros
        print("a- Consultar cantidad de millas")
        print("b- Acumular Millas")
        print("c- Canjear Millas")
        opc = input("ingrese opcion: ")
        if opc == "a":
            millas = viajero.cantidadTotalDeMillas()
            print("Las millas acumuladas son: ", millas)
        elif opc == "b":
            millas = int(input("Ingrese las millas a acumular: "))
            if millas < 0:
                print("Millas negativas")
            else:
                millas = viajero.acumularMillas(vid, millas)
                print("Las nuevas millas acumuladas son: ", millas)
        elif opc == "c":
            canje = int(input("Ingrese las millas a canjear: "))
            if canje < 0:
                print("Millas negativas")
            elif viajero.puedeCanjear(canje):
                millas = viajero.canjearMillas(canje)
                print("Las nuevas millas acumuladas son: ", canje)
            else:
                print("No se realizo el canje por falta de millas")
        else:
            print("opcion incorrecta")
    else:
        print("Viajero no encontrado")

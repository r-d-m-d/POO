from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados
from Helado import Helado
SABORESCSV = "sabores.csv"


class Main:

    def __init__(self):
        self.__ms = ManejaSabores()
        self.__mh = ManejaHelados()
        ms.cargarSabores(SABORESCSV)
        self.__opcPrin = ["Registrar Helado Vendido",
                          "Mostrar 5 sabores mas vendidos",
                          "Dado un sabor, estimar total de gramos vendidos",
                          "Mostrar sabores vendidos en ese tama",
                          "Determinar el importe total recaudado por la" +
                          " Heladeria, por cada tipo de helado"]

    def mostrarOpciones(self, listaOpciones):
        for n, s in enumerate(listaOpciones):
            print(f"{n+1}) {s}")

    def menuPrincipal(self):
        self.mostrarOpciones(self.__opcPrin)
        print("s) Salir")
        opc = input("Ingrese una opcion: ")
        print(f"Selecciona {opc}")
        return opc

    def menuPesajes(self):
        pesajes = Helado.getPesajes()
        opt = None
        while opt is None:
            print("Menu pesajes")
            self.mostrarOpciones(pesajes)
            opc = input("Ingrese una opcion: ")
            if opc.isdigit():
                opt = int(opc) - 1
            if (opt < 0 or opt >= len(pesajes)) or not opc.isdigit():
                print(f"Opcion invalida: {opc}")
                opt = None
        print(f"Selecciona {opc}")
        return opt

if __name__ == "__main__":
    ms = ManejaSabores()
    mh = ManejaHelados()
    ms.cargarSabores(SABORESCSV)
    main = Main()
    opc = main.menuPrincipal()
    while opc.lower() != "s":
        if opc == "1":
            print("Registrando venta")
            gramosId = main.menuPesajes()
            sabores = []
            saboresDisponibles = ms.getSabores()
            while opc.lower() != "s" and len(sabores) < Helado.MAX_SABORES:
                print("Menu Sabores")
                main.mostrarOpciones(saboresDisponibles)
                print("s) no agregar mas sabores")
                opc = input("Seleccione el sabor: ")
                print(f"Selecciona {opc}")
                if opc.isdigit():
                    opt = int(opc) - 1
                    if opt >= 0 and opt < len(saboresDisponibles):
                        sabores.append(saboresDisponibles.pop(opt))
                elif opc != "s":
                    print("Opcion invalida {opc}")
            mh.registrarHeladoVendido(gramosId, sabores)
        elif opc == "2":
            print("Cinco sabores más vendidos")
            mv = ms.saboresMasVendidos()
            for s in mv:
                print(s, " ", s.numHelados())
        elif opc == "3":
            print("Estimar gramos vendidos de un sabor")
            print("elija un sabor")
            sd = ms.getSabores()
            main.mostrarOpciones(sd)
            opc = int(input("Elija una opcion: "))
            sabor = sd[opc]
            gv = sabor.estimarGramosVendidos()
            print(f"Gramos vendidos de {sabor}: {gv}")
        elif opc == "4":
            print("Sabores vendidos en un tamaño")
            gramosId = main.menuPesajes()
            lhp = mh.obtenerHeladosDePesaje(gramosId)
            lsp = []
            for h in lhp:
                for s in h.getSabores():
                    if not (s in lsp):
                        lsp.append(s)
            for h in lsp:
                print(h)
        elif opc == "5":
            print("Importe recaudado por cada tipo de helado")
            mh.informe()
        else:
            print(f"Opcion Invalida {opc}")

        opc = main.menuPrincipal()

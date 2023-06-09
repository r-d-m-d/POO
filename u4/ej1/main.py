from tkinter import Tk, Entry, Label, Button, StringVar


class CalculadoraIpc:
    opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}

    def __init__(self):
        self.__v = Tk()
        self.__v.title("Calculadora IPC")
# Labels
        self.__litem = Label(self.__v, text="Item")
        self.__litem.grid(row=0, column=0, **CalculadoraIpc.opts)

        self.__lcant = Label(self.__v, text="Cantidad")
        self.__lcant.grid(row=0, column=1, **CalculadoraIpc.opts)

        self.__lpab = Label(self.__v, text="Precio Año Base")
        self.__lpab.grid(row=0, column=2, **CalculadoraIpc.opts)
        self.__lpaa = Label(self.__v, text="Percio Año Actual")
        self.__lpaa.grid(row=0, column=3, **CalculadoraIpc.opts)

        self.__lvest = Label(self.__v, text="Vestimenta")
        self.__lvest.grid(row=1, column=0, **CalculadoraIpc.opts)
        self.__lalim = Label(self.__v, text="Alimentos")
        self.__lalim.grid(row=2, column=0, **CalculadoraIpc.opts)
        self.__leduc = Label(self.__v, text="Educacion")
        self.__leduc.grid(row=3, column=0, **CalculadoraIpc.opts)

        self.__ipcVar = StringVar()
        self.__ipcVar.set("IPC % XX.XX %")
        self.__lipc = Label(self.__v, textvariable=self.__ipcVar)
        self.__lipc.grid(row=4, column=1, columnspan=2, **CalculadoraIpc.opts)
# Datos
        self.__datos = [[StringVar() for x in range(3)] for y in range(3)]
        self.__CANTIDAD = 0
        self.__PAÑOBASE = 1
        self.__PAÑOACTUAL = 2
        self.__dataEntrys = [[Entry(self.__v, width=4, textvariable=x)
                              for x in fila] for fila in self.__datos]
        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        for row, fila in enumerate(self.__dataEntrys):
            for col, entry in enumerate(fila):
                entry.grid(row=row+1, column=col+1, sticky="ew")
# Botones
        self.__bSalir = Button(self.__v, text="Salir", command=self.__v.destroy)
        self.__bSalir.grid(row=5, column=3, **opts)
        self.__bCalcular = Button(self.__v, text="Calcular IPC", command=self.calcularIpc)
        self.__bCalcular.grid(row=4, column=0, **opts)
# fin __init__

    def calcularIpc(self):
        ipc = 0
        try:
            for fila in self.__datos:
                cant = int(fila[self.__CANTIDAD].get())
                precioAñoBase = int(fila[self.__PAÑOBASE].get())
                precioAñoActual = int(fila[self.__PAÑOACTUAL].get())
                ipc += cant * precioAñoActual / precioAñoBase
            ipc = round(ipc) / 100
            self.__ipcVar.set(f"IPC % {ipc}")
        except Exception as e:
            print(e)

    def mainloop(self):
        self.__v.mainloop()

if __name__ == "__main__":
    c = CalculadoraIpc()
    c.mainloop()

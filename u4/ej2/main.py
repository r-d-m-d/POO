import tkinter as tk
from tkinter import Tk, Label, Entry, Radiobutton, Button, ttk
from functools import partial



class CalculoIva:
    __iva: float

    def __init__(self, precio_base, grabado):
        self.__precio_base = precio_base
        self.__iva = precio_base * grabado / 100.0

    def obtenerIva(self):
        return self.__iva

    def precioFinal(self):
        return self.__precio_base + self.obtenerIva()


class Gui:
    __iva: float

    def __init__(self):
        self.__iva = 10.5
        self.__v = Tk()
        self.__v.title("Calculo de Iva")
        self.__v.config(padx=5, pady=5)

        self.__lprecioSinIva = Label(self.__v, text="Precio sin Iva")

        opts = {"ipadx": 10, "ipady": 10, "fill": tk.BOTH}

        self.__lprecioSinIva.grid(row=0, column=0)
        self.__vPrecio = tk.StringVar()
        self.__ePrecio = Entry(self.__v, textvariable=self.__vPrecio)
        self.__ePrecio.grid(row=0, column=1)

        self.__lfIva = tk.LabelFrame(self.__v, text="", borderwidth=2)
        self.__lfIva.grid(row=1, column=0, columnspan=2, sticky="nswe")
        self.__vIva = tk.BooleanVar()
        self.__rIva21 = ttk.Radiobutton(self.__lfIva, text="IVA 21%", value=1,
                                        variable=self.__vIva
                                        ,command=partial(self.iva, 21.0))
        self.__rIva10 = ttk.Radiobutton(self.__lfIva, text="IVA 10%", value=0,
                                        variable=self.__vIva,
                                        command=partial(self.iva, 10))
        self.__rIva21.pack(side=tk.TOP, **opts)
        self.__rIva10.pack(side=tk.TOP, **opts)

        self.__lIva = Label(self.__v, text="IVA")
        self.__lIva.grid(row=2, column=0)
        self.__vIvaMonto = tk.StringVar()
        self.__eIva = Entry(self.__v, textvariable=self.__vIvaMonto)
        self.__eIva.grid(row=2, column=1, pady=3)

        self.__lPrecioConIva = Label(self.__v, text="Precio con IVA")
        self.__lPrecioConIva.grid(row=3, column=0)
        self.__vPrecioConIva = tk.StringVar()
        self.__ePrecioConIva = Entry(self.__v, textvariable=self.__vPrecioConIva)
        self.__ePrecioConIva.grid(row=3, column=1)

        self.__bCalcular = Button(self.__v, text="Calcular", command=self.calcular)
        self.__bCalcular.grid(row=4, column=0, sticky=tk.W)

        self.__bSalir = Button(self.__v, text="Salir", command=self.__v.destroy)
        self.__bSalir.grid(row=4, column=1, sticky=tk.E)
        self.__v.mainloop()

    def iva(self, iva):
        self.__iva = iva

    def calcular(self):
        try:
            pb = float(self.__vPrecio.get())
        except Exception as e:
            print(e)
        else:
            c = CalculoIva(pb, self.__iva)
            self.__vIvaMonto.set(c.obtenerIva())
            self.__vPrecioConIva.set(c.precioFinal())


g = Gui()

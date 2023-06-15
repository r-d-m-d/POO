# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 23:03:53 2020

@author: morte
"""

from tkinter import *
from tkinter import ttk
from functools import partial
import re
from Complejo import Complejo
from EnvoltorioDeFuncion import EnvoltorioDeFuncion


class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        self.__cmdSuma = EnvoltorioDeFuncion(partial(self.ponerNUMERO, '+'))
        self.__cmdResta = EnvoltorioDeFuncion(partial(self.ponerNUMERO, '-'))
        operatorEntry=ttk.Label(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled', background="white", borderwidth=2, relief="groove")
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Label(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled', background="white", borderwidth=2, relief="groove")
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=self.__cmdSuma).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=self.__cmdResta).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='i', command=self.poneri).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='<=', command=self.borrarCaracter).grid(column=1, row=8, sticky=W)
        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()
        
    def borrarCaracter(self):
        valor = self.__panel.get()
        valor = valor[:len(valor)-1]
        self.__panel.set(valor)

    def poneri(self):
        sval = self.__panel.get()
        sval = sval + 'i' if not sval.endswith('i') else sval
        self.__panel.set(sval)

    def ponerNUMERO(self, numero):
        valor = self.__panel.get()
        if self.__operadorAux is None:
            self.__panel.set(valor+numero)
        else:
            self.__operadorAux = None
            self.__primerOperando = self.obtenerComplejo(valor)
            self.__panel.set(numero)
        if numero in ['+', '-']:
            self.__cmdSuma.fn(partial(self.ponerOPERADOR, '+'))
            self.__cmdResta.fn(partial(self.ponerOPERADOR, '-'))


    def borrarPanel(self):
        self.__panel.set('0')
        
    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        elif operacion=='-':
            resultado=operando1-operando2
        elif operacion=='*':
            resultado=operando1*operando2
        elif operacion=='/':
            resultado=operando1.__div__(operando2)
        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        operacion = self.__operador.get()
        if op == '=':
            self.__segundoOperando = self.obtenerComplejo(self.__panel.get())
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
        else:
            if operacion == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                self.__segundoOperando = self.obtenerComplejo(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op
        if 'i' in self.__panel.get():
            self.__cmdSuma.fn(partial(self.ponerNUMERO, '+'))
            self.__cmdResta.fn(partial(self.ponerNUMERO, '-'))


    def obtenerComplejo(self, sVal):
        crx = re.compile(r'(-?\d+(.\d+)?)([+-]\d+(.\d+)?)i')
        mc = crx.match(sVal)
        real, _, img, _ = mc.groups() if mc is not None else (0,0,0,0)
        return Complejo(float(real), float(img))

def main():
    calculadora=Calculadora()
    
if __name__=='__main__':
    main()




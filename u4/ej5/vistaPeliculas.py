import tkinter as tk
from tkinter import messagebox, StringVar
# Temporales
import json
from generos import AlmacenGeneros
# Temporales

from peliculas import Pelicula, ManejaPelicula

class PeliculaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, titulo: str, index=tk.END):
        # Quizas deberia agregar el director ¡?
        self.lb.insert(index, titulo)

    def bind_doble_click(self, callback):
        self.lb.bind("<Double-Button-1>",
                     lambda _: callback(self.lb.curselection()[0]))

    def bind_lb_select(self, cb):
        self.lb.bind('<<ListboxSelect>>',
                     lambda _: cb(self.lb.curselection()[0]))


class PeliculaForm(tk.LabelFrame):
    fields = ("Titulo", "Lenguaje Original", "Fecha de lanzamiento",
              "Generos")
# , "Resumen"
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Pelicula", padx=10, pady=10, **kwargs)
        self.labelVars = {}
        self.frame = tk.Frame(self)
        self.comentarios = tk.Text(self.frame,
                                   background="white", state=tk.DISABLED)
        self.comentarios.grid(row=len(self.fields)+1, columnspan=2, column=0, pady=5)

        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        v = StringVar()
        label = tk.Label(self.frame, text=text, justify=tk.LEFT)
        entry = tk.Label(self.frame, background="white",
                         textvariable=v, justify=tk.LEFT)
        self.labelVars.update({text: v})
        label.grid(row=position, column=0, pady=5, sticky="w")
        entry.grid(row=position, column=1, pady=1, sticky="we")
        return entry

    def mostrarEstadoPeliculaEnFormulario(self,titulo, lo, fl, gen, overview):
        # a partir de un Pelicula, obtiene el estado
        # y establece en los valores en el formulario de entrada
        self.labelVars['Titulo'].set(titulo)
        self.labelVars['Lenguaje Original'].set(lo)
        self.labelVars['Fecha de lanzamiento'].set(fl)
        self.labelVars['Generos'].set(gen)

        self.comentarios.configure(state=tk.NORMAL)
        self.comentarios.delete("1.0", tk.END)
        self.comentarios.insert(tk.END, overview)
        self.comentarios.configure(state=tk.DISABLED)

# Se puede reciclar como siguiente pagina
class NewPelicula(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.pelicula = None
        self.form = PeliculaForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.pelicula = self.form.crearPelicula()
        if self.pelicula:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.pelicula

    def crearPelicula(arg):
        pass


class UpdatePeliculaForm(PeliculaForm):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Siguiente Pelicula")
        self.btn_delete = tk.Button(self, text="Borrar")
#        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        # self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

class PeliculaView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lista de Peliculas")
        self.list = PeliculaList(self, width=30)
        self.form = UpdatePeliculaForm(self)
        self.list.pack(side=tk.LEFT, fill=tk.BOTH, padx=1, pady=1)
        self.form.pack(side=tk.LEFT, fill=tk.BOTH,padx=1, pady=1)

    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPelicula)
        self.list.bind_doble_click(ctrl.seleccionarPelicula)
        self.form.bind_save(ctrl.modificarPelicula)
        self.form.bind_delete(ctrl.borrarPelicula)

    def seleccionarPelicula(self, f):
        self.list.bind_doble_click(f)
        self.list.bind_lb_select(f)

    def agregarPelicula(self, titulo):
        self.list.insertar(titulo)

    #obtiene los valores del formulario y crea un nuevo contacto
    def obtenerDetalles(self):
        return self.form.crearPeliculaDesdeFormulario()

    #Ver estado de Contacto en formulario de contactos
    def verPeliculaEnForm(self, titulo, lo, fl, gen, overview):
        self.form.mostrarEstadoPeliculaEnFormulario(titulo, lo, fl, gen, overview)

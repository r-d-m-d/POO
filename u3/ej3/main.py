import numpy as np
import csv

import Taller
import Persona
import Inscripcion
import ManejaTaller
import ManejaInscripciones
FN = "talleres.csv"
if __name__ == "__main__":
#1) Cargar los datos de los talleres en la clase TallerCapacitacion 
# a partir del archivo
    mt = ManejaTaller.ManejaTaller()
# maneja taller > cargar archivo
    mt.cargarArchivo(FN)
# fin 1)
    lp = []
    mi = ManejaInscripciones.ManejaInscipciones()
# 2) Inscirbir una persona en un taller. Se registra la inscripcion (sin pagar)
#y la candtidad de vacantes en el taller debe ser actualizada
    nombre = input("Ingrese el nombre de la persona: ")
    dire = input("Ingrese la direccion: ")
    dni = input("Ingrese el dni: ")
    p = Persona.Persona(nombre, dire, dni)
    lp.append(p)
    # maneja taller > mostrar talleres
    mt.mostrarTalleres()
    tid = int(input("Ingrese el id de un taller: "))
    # maneja taller > buscaTallerPorId
    i = 0
    taller = mt.buscaTallerPorId(tid)
    if taller is not None:
        # FIXME: fecha python
        inscr = Inscripcion.Inscripcion("0", p, taller)
        mi.agregarInscripcion(inscr)

# 3) Consultar inscripcion: Ingresar DNI de una persona, si esta inscripta 
# mostrar el nombre del taller en el que se inscribio y el monto que adeuda
    dni = input("Ingrese el dni: ")
    # maneja inscripciones > busca dni (dni)
    print(mi.consultarInscripcion(dni))
# 5) Consultar inscriptos. Ingresar el identificador de un taler y listar los 
# datos de los alumnos que se inscribieron en el
    mt.mostrarTalleres()
    tid = input("Ingrese el id de un taller: ")
#  FIXME: INEFICIENTE: hay menos talleres que inscripciones
    # controla inscripciones > mostrar inscripciones de taller(tid)
    mi.consultarInscriptos(tid)
# 6) Registrar pago: Ingresar el DNI de una persona y registrar el pago
    dni = input("Ingrese el dni para registrar pago: ")
    i = 0
    # maneja inscripciones > mostrarInscripcionesTaller
    mi.registrarPago(dni)
# 7) Guardar inscripciones: generar un nuevo archivo que contenga los 
# siguientes datos de las inscripciones: DNI,idTaller, fechaInscripcion y pago
    # Guardar inscripciones
    mi.guardarInscripciones("inscripciones.csv")

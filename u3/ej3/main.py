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
    li = ManejaInscripciones.ManejaInscipciones(shape=1,
                                                dtype = Inscripcion.Inscripcion)
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
        li.append(inscr)

# 3) Consultar inscripcion: Ingresar DNI de una persona, si esta inscripta 
# mostrar el nombre del taller en el que se inscribio y el monto que adeuda
    dni = input("Ingrese el dni: ")
    # maneja inscripciones > busca dni (dni)
    i = 0
    while i < len(li) and li[i].persona().dni() != dni:
        i += 1
    if i < len(li) and li[i].persona().dni() == dni:
        print(li[i].taller().nomb())
        print(li[i].taller().montoInsc())

# 5) Consultar inscriptos. Ingresar el identificador de un taler y listar los 
# datos de los alumnos que se inscribieron en el
    mt.mostrarTalleres()
    tid = input("Ingrese el id de un taller: ")
    i = 0
#  FIXME: INEFICIENTE: hay menos talleres que inscripciones
    # controla inscripciones > mostrar inscripciones de taller(tid)
    for insc in li:
        if insc.taller().idTaller() == tid:
            print(insc.persona())

# 6) Registrar pago: Ingresar el DNI de una persona y registrar el pago
    dni = input("Ingrese el dni para registrar pago: ")
    i = 0
    # maneja inscripciones > mostrarInscripcionesTaller
    while i < len(li) and li[i].persona().dni() != dni:
        i += 1
    if i < len(li) and li[i].persona().dni() == dni:
        li[i].registrarPago()
# 7) Guardar inscripciones: generar un nuevo archivo que contenga los 
# siguientes datos de las inscripciones: DNI,idTaller, fechaInscripcion y pago
    # Guardar inscripciones
    with open("inscripciones.csv", "w") as fp:
        writer = csv.writer(fp)
        for insc in li:
            dni = insc.persona().dni()
            idt = insc.taller().idTaller()
            fecha = insc.fechaInsc()
            pago = insc.pago()
            writer.writerow([dni, idt, fecha, pago])

import numpy as np
import csv

import Taller
import Persona
import Inscripcion

FN = "Talleres.csv"
if __name__ == "__main__":
#1) Cargar los datos de los talleres en la clase TallerCapacitacion 
# a partir del archivo
    lTalleres = None
    idx = 0
    with open(FN) as fp:
        n = fp.readline()
        if n.isdigit():
            ntalleres = int(n)
            lTalleres = np.array(n, dtype=Taller.Taller)
            reader = csv.reader(fp)
            for line in reader:
                idt = int(line[0])
                vac = int(line[2])
                monto = int(line[3])
                lTalleres[idx] = Taller.Taller(idt, line[1], vac, monto)
                idx += 1
# fin 1)
    lp = []
    li = []
# Inscirbir una persona en un taller. Se registra la inscripcion (sin pagar) 
#y la candtidad de vacantes en el taller debe ser actualizada
    nombre = input("Ingrese el nombre de la persona: ")
    dire = input("Ingrese la direccion: ")
    dni = input("Ingrese el dni: ")
    p = Persona.Persona(nombre, dire, dni)
    lp.append(p)
    for t in lTalleres:
        print(f"{t}")
    tid = input("Ingrese el id de un taller: ")
    i = 0
    while i < len(lTalleres) and lTalleres[i].idTaller() != tid:
        i += 1

    if i < len(lTalleres) and lTalleres[i].idTaller() == tid:
        inscr = Inscripcion.Inscripcion("0", p, lTalleres[i])
        li.append(inscr)

# Consultar inscripcion: Ingresar DNI de una persona, si esta inscripta 
# mostrar el nombre del taller en el que se inscribio y el monto que adeuda
    dni = input("Ingrese el dni: ")
    i = 0
    while i < len(li) and li[i].persona().dni() != dni:
        i += 1
    if i < len(li) and li[i].persona().dni() == dni:
        print(li[i].taller().nomb())
        print(li[i].taller().montoInsc())

# Consultar inscriptos. Ingresar el identificador de un taler y listar los 
# datos de los alumnos que se inscribieron en el
    for t in lTalleres:
        print(f"{t}")
    tid = input("Ingrese el id de un taller: ")
    i = 0
#  FIXME: INEFICIENTE: hay menos talleres que inscripciones
    for insc in li: 
        if insc.taller().idTaller() == tid:
            print(insc.persona())

# Registrar pago: Ingresar el DNI de una persona y registrar el pago
    dni = input("Ingrese el dni para registrar pago: ")
    i = 0
    while i < len(li) and li[i].persona().dni() != dni:
        i += 1
    if i < len(li) and li[i].persona().dni() == dni:
        li[i].registrarPago()
# Guardar inscripciones: generar un nuevo archivo que contenga los siguientes
# datos de las inscripciones: DNI,idTaller,fechaInscripcion y pago
    with open("inscripciones.csv", "w") as fp:
        writer = csv.writer(fp)
        for insc in li:
            dni = insc.persona().dni()
            idt = insc.taller().idTaller()
            fecha = insc.fecha()
            pago = insc.pago()
            writer.weiterow(dni, idt, fecha, pago)

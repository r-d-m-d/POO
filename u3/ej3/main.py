from datetime import date

import Taller
import Persona
import Inscripcion
import ManejaTaller
import ManejaInscripciones
import ManejaPersonas
FN = "talleres.csv"
if __name__ == "__main__":
#1) Cargar los datos de los talleres en la clase TallerCapacitacion 
# a partir del archivo
    mp = ManejaPersonas.ManejaPersona()
    mt = ManejaTaller.ManejaTaller()
    mt.cargarArchivo(FN)
    mi = ManejaInscripciones.ManejaInscipciones()
# fin 1)
# A) Crear un menu
    print("1)Inscribir una persona en un taller")
    print("2)Consultar inscripcion")
    print("3)Consultar inscriptos")
    print("4)Registrar pago")
    print("5)Guardar inscripciones")
    print("S) Salir")
    opc = input("Ingrese una opcion")
    while opc.strip().lower() != 's':
        if opc == '1':
# 2) Inscirbir una persona en un taller. Se registra la inscripcion (sin pagar)
#y la candtidad de vacantes en el taller debe ser actualizada
            nombre = input("Ingrese el nombre de la persona: ").strip()
            dire = input("Ingrese la direccion: ").strip()
            dni = input("Ingrese el dni: ").strip()
            p = Persona.Persona(nombre, dire, dni)
            mp.agregarPersona(p)
            # maneja taller > mostrar talleres
            mt.mostrarTalleres()
            tid = int(input("Ingrese el id de un taller: "))
            # maneja taller > buscaTallerPorId
            i = 0
            taller = mt.buscaTallerPorId(tid)
            if isinstance(taller, Taller.Taller):
                # FIXME: fecha python
                inscr = Inscripcion.Inscripcion(date.today(), p, taller)
                mi.agregarInscripcion(inscr)
            else:
                print("Taller invalido")
        elif opc == '2':
# 3) Consultar inscripcion: Ingresar DNI de una persona, si esta inscripta 
# mostrar el nombre del taller en el que se inscribio y el monto que adeuda
            dni = input("Ingrese el dni: ").strip()
            # maneja inscripciones > busca dni (dni)
            x = mi.consultarInscripcion(dni)
            if isinstance(x, str):
                print(x)
            else:
                print("Dni no encontrado")
        elif opc == '3':
# 5) Consultar inscriptos. Ingresar el identificador de un taler y listar los 
# datos de los alumnos que se inscribieron en el
            mt.mostrarTalleres()
            tid = input("Ingrese el id de un taller: ").strip()
#  FIXME: INEFICIENTE: hay menos talleres que inscripciones
            # controla inscripciones > mostrar inscripciones de taller(tid)
            mi.consultarInscriptos(tid)

        elif opc == '4':
# 6) Registrar pago: Ingresar el DNI de una persona y registrar el pago
            dni = input("Ingrese el dni para registrar pago: ").strip()
            # maneja inscripciones > mostrarInscripcionesTaller
            mi.registrarPago(dni)
        elif opc == '5':
# 7) Guardar inscripciones: generar un nuevo archivo que contenga los 
# siguientes datos de las inscripciones: DNI,idTaller, fechaInscripcion y pago
            # Guardar inscripciones
            mi.guardarInscripciones("inscripciones.csv")
        elif opc.lower() == 's':
            print("Adios")
        else:
            print("Opcion Invalida")
        print("1)Inscribir una persona en un taller")
        print("2)Consultar inscripcion")
        print("3)Consultar inscriptos")
        print("4)Registrar pago")
        print("5)Guardar inscripciones")
        opc = input("Ingrese una opcion")




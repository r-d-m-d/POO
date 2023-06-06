import json

from Docente import Docente
from Investigador import Investigador
from PersonalDeApoyo import PersonalDeApoyo
from DocenteInvestigador import DocenteInvestigador

filename = "personal.json"


class Main:
    def __crearPersona(self):
        #  SOLO creara un diccionario con los atributos
        d = {}
        # Personal
        d['cuil'] = input("Ingrese el cuil: ")
        d['apellido'] = input("Ingrese el apellido: ")
        d['nombre'] = input("Ingrese el nombre: ")
        d['sueldo_basico'] = int(input("Ingrese el sueldo basico: "))
        return d

    def crearDocente(self):
        d = self.__crearPersona()
        # Docente
        d['carrera'] = input("Ingrese la carrera: ")
        d['cargo'] = input("Ingrese el cargo: ")
        d['catedra'] = input("Ingrese una catedra: ")
        return d

    def crearInvestigador(self):
        d = self.__crearPersona()
        # Investigador
        d['area'] = input("Ingrese el area: ")
        d['tipo'] = input("Ingrese el tipo")
        return d

    def crearPersonalDeApoyo(self):
        d = self.__crearPersona()
        d['categoria'] = input("Ingrese la categoria: ")
        return d

    def crearDocenteInvestigador(self):
        d = self.crearDocente()
        d['area'] = input("Ingrese el area: ")
        d['tipo'] = input("Ingrese el tipo")
        d['categoria_investigacion'] = input("Ingrese la categoria_investigacion: ")
        d['importe_extra'] = input("Ingrese el importe_extra: ")
        return d


if __name__ == "__main__":
    m = Main()
    print("1) Insertar agentes a la colección")
    print("2) Agregar agentes a la colección")
    print("3) Mostrar tipo de agente en una posición")
    print("4) Listado de docentes investigadores por carrera")
    print("5) Contar agentes por área de investigación")
    print("6) Listado de agentes ordenado por apellido")
    print("7) Listado de docentes investigadores por categoría")
    print("0) Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    while opcion != '0':
        if opcion == '1':
            # Tarea: Insertar agentes a la colección
            print("1)Docente")
            print("2)Investigador")
            print("3)Personal de apoyo")
            print("4)Docente Investigador")
            an = input("Ingrese una opcion")
            if an == "1":
                d = m.crearDocente()
                doc = Docente(d)
            elif an == "2":
                d = m.crearInvestigador()
                inv = Investigador(d)
            elif an == "3":
                d = m.crearPersonalDeApoyo()
                pp = PersonalDeApoyo(d)
            elif an == "4":
                d = m.crearDocenteInvestigador()
                di = DocenteInvestigador(d)
        elif opcion == '2':
            # Tarea: Agregar agentes a la colección
            pass
        elif opcion == '3':
            # Tarea: Mostrar tipo de agente en una posición
            pass
        elif opcion == '4':
            # Tarea: Listado de docentes investigadores por carrera
            pass
        elif opcion == '5':
            # Tarea: Contar agentes por área de investigación
            pass
        elif opcion == '6':
            # Tarea: Listado de agentes ordenado por apellido
            pass
        elif opcion == '7':
            # Tarea: Listado de docentes investigadores por categoría
            pass
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
        print("1) Insertar agentes a la colección")
        print("2) Agregar agentes a la colección")
        print("3) Mostrar tipo de agente en una posición")
        print("4) Listado de docentes investigadores por carrera")
        print("5) Contar agentes por área de investigación")
        print("6) Listado de agentes ordenado por apellido")
        print("7) Listado de docentes investigadores por categoría")
        print("0) Salir")
        opcion = input("Ingrese el número de la opción deseada: ")


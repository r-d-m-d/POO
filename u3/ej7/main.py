from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from PersonalDeApoyo import PersonalDeApoyo
from DocenteInvestigador import DocenteInvestigador
from ManejaPersonal import ManejaPersonal



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

    def crearPersonal(self):
        print("1)Docente")
        print("2)Investigador")
        print("3)Personal de apoyo")
        print("4)Docente Investigador")
        an = input("Ingrese una opcion")
        pers = None
        if an == "1":
            d = m.crearDocente()
            pers = Docente(d)
        elif an == "2":
            d = m.crearInvestigador()
            pers = Investigador(d)
        elif an == "3":
            d = m.crearPersonalDeApoyo()
            pers = PersonalDeApoyo(d)
        elif an == "4":
            d = m.crearDocenteInvestigador()
            pers = DocenteInvestigador(d)
        return pers


if __name__ == "__main__":
    m = Main()
    mp = ManejaPersonal()
    mp.cargarArchivo()  # utilizo el parametro por defecto
    print("1) Insertar agentes a la colección")
    print("2) Agregar agentes a la colección")
    print("3) Mostrar tipo de agente en una posición")
    print("4) Listado de docentes investigadores por carrera")
    print("5) Contar agentes por área de investigación")
    print("6) Listado de agentes ordenado por apellido")
    print("7) Listado de docentes investigadores por categoría")
    print("8) Guardar")
    print("0) Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    while opcion != '0':
        if opcion == '1':
            # Tarea: Insertar agentes a la colección
            pers = m.crearPersonal()
            pos = int(input("Ingrese la posicion: "))
            mp.insertar(pers, pos)
        elif opcion == '2':
            # Tarea: Agregar agentes a la colección
            pers = m.crearPersonal()
            mp.agregarPersonal(pers)
        elif opcion == '3':
            # Tarea: Mostrar tipo de agente en una posición
            pos = int(input("Ingrese una posicion: "))
            pers = mp.obtenerElemento(pos)
            if isinstance(pers, Personal):
                print(pers.tipo())
            else:
                print("Elemento no encontrado")
        elif opcion == '4':
            # Tarea: Listado de docentes investigadores por carrera
            d = mp.listarDocenteInvestigadoresPorCarrera()
            for k in d.keys():
                for e in d[k]:
                    print(f'{k}: {e}')
        elif opcion == '5':
            # Tarea: Contar agentes por área de investigación
            dcont = mp.contarAgentesPorAreaDeInvestigacion()
            for area in dcont.keys():
                print(f"{area}: {dcont[area]}")
        elif opcion == '6':
            # Tarea: Listado de agentes ordenado por apellido
            lpersonal = mp.agentesOrdenadosPorApellido()
            for personal in lpersonal:
                print(personal)
        elif opcion == '7':
            # Tarea: Listado de docentes investigadores por categoría
            dipc = mp.docentesInvestigadoresPorCategoria()
            for categoria in dipc.keys():
                print(f"{categoria} {dipc[categoria]}")
        elif opcion == '8':
            # Tarea: Guardar en archivo personal.json
            mp.guardar()
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
        print("1) Insertar agentes a la colección")
        print("2) Agregar agentes a la colección")
        print("3) Mostrar tipo de agente en una posición")
        print("4) Listado de docentes investigadores por carrera")
        print("5) Contar agentes por área de investigación")
        print("6) Listado de agentes ordenado por apellido")
        print("7) Listado de docentes investigadores por categoría")
        print("8) Guardar")
        print("0) Salir")
        opcion = input("Ingrese el número de la opción deseada: ")


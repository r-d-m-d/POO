from hashlib import sha512

from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from PersonalDeApoyo import PersonalDeApoyo
from DocenteInvestigador import DocenteInvestigador
from ITesorero import ITesorero
from IDirector import IDirector
from ManejaPersonal import ManejaPersonal


class Main:
    
    def __init__(self):
        self.__tesorero = False
        self.__director = False

    def ingresarTesorero(self):
        HASH = "7f7b41e2cdede12daf8671b00f81386621e2f4b145dbb44d48a88ff7d3dcaa45079599f53bc784e5c1305733636fa31fcef138e96e351f8cce199ebbb948b123"
        usuario = input("Ingrese el usuario: ")
        passwd = input("Ingrese la contraseña: ")
        upHash = sha512(usuario.encode())
        upHash.update(passwd.encode())
        self.__tesorero = upHash.hexdigest() == HASH
        return upHash.hexdigest() == HASH

    def menuTesorero(self, mt: ITesorero):
        if self.__tesorero:
            dni = input("Ingrese dni o s para salir")
            while dni.lower() != 's':
                sueldo = mt.gastosSueldoPorEmpleado(dni)
                print("El gasto es: ", sueldo)
                dni = input("Ingrese dni o s para salir")
            self.__tesorero = False

    def ingresarDirector(self):
        HASH = "dd0373f733f79c983e922cea2dba737b03980f731f995828d32b4d78fd64c604ea050551e06d2494ffcf7849fba49036994a0bbc545580ee9a780dd211b6fa30"
        u = input("Ingrese el usuario:  ")
        p = input("Ingrese la contraseña: ")
        uph = sha512(u.encode())
        uph.update(p.encode())
        self.__director = uph.hexdigest() == HASH
        return self.__director

    def menuDirector(self, md: IDirector):
        dni = ""
        if self.__director:
            print("1) modificar basico")
            print("2) modificar porcentaje por cargo")
            print("3) modificar porcentaje por categoria")
            print("4) modficar importe extra")
            print("s) salir")
            opc = input("Ingrese una opcion")
            while opc.lower() != 's':
                dni = input("Ingrese el dni")
                if opc == "1":
                    b = input("Ingrese el nuevo basico: ")
                    md.modificarBasico(dni, b)
                elif opc == "2":
                    p = input("Ingrese el nuevo cargo ")
                    md.modificarPorcentajeporcargo(dni, p)
                elif opc == "3":
                    c = int(input("Ingrese categoria[1;22]: "))
                    md.modificarPorcentajeporcategoría(dni, c)
                elif opc == "4":
                    ie = int(input("Ingrese importe extra: "))
                    md.modificarImporteExtra(dni, ie)
                elif opc.lower() != 's':
                    print("Ingrese una opcion valida")
                print("1) modificar basico")
                print("2) modificar porcentaje por cargo")
                print("3) modificar porcentaje por categoria")
                print("4) modficar importe extra")
                print("s) salir")
                opc = input("Ingrese una opcion")
            self.__director = False

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
    print("D) Ingresar como director")
    print("T) Ingresar como tesorero")
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
        elif opcion.lower() == 'd':
            ingreso = m.ingresarDirector()
            if ingreso:
                m.menuDirector(mp)
        elif opcion.lower() == 't':
            ingreso = m.ingresarTesorero()
            if ingreso:
                m.menuTesorero(mp)
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
        print("D) Ingresar como director")
        print("T) Ingresar como tesorero")
        print("0) Salir")
        opcion = input("Ingrese el número de la opción deseada: ")


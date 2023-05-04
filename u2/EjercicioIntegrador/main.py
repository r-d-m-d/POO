import csv

from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMaterias import ManejadorMateria
from ManejadorInformes import ManejadorInforme

ALUMNOS_FILE = "alumnos.csv"
MATERIAS_FILE = "materiasAprobadas.csv"
def test():
    pass
if __name__ == "__main__":
    mmat = ManejadorMateria()
    mmat.cargarMaterias(MATERIAS_FILE)
    malu = ManejadorAlumnos()
    malu.cargarAlumnos(ALUMNOS_FILE)
    minfo = ManejadorInforme(mmat,malu)
    print("a) Informe de promedio.")
    print("b) Informe de materia.")
    print("c) Listar alumnos")

    opc=input("Ingrese una opcion: ")

    if opc == "a":
        dni = input("Ingrese el dni del alumno: ")
        print("Promedio con aplazos: ",mmat.promedioConAplazos(dni))
        print("Promedio sin aplazos: ",mmat.promedioSinAplazos(dni))
    elif opc == "b":
        nmat = input("Ingrese el nombre de una materia: ")
        informes =  minfo.hacerInformesDe(nmat)
        print("{:10}\t{:18}\t{:12}\t{:7}\t{:5}".format("DNI", "Apellido y Nombre", "Fecha", "Nota", "Año"))
        for x in informes:
            print(x)
        
    elif opc == "c":
        aluarr = malu.retornaAlumnosOrdenados()
        for alu in aluarr:
            print(alu)
    else:
        print("Opcion invalida.")

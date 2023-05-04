from Informe import Informe
from ManejadorMaterias import ManejadorMateria
from ManejadorAlumnos import ManejadorAlumnos

class ManejadorInforme:
    def __init__(self,manejadorMateria,manejadorAlumno):
        self.__mmat = manejadorMateria
        self.__malu = manejadorAlumno
        self.__informes = []

    def hacerInformesDe(self,materia):
        mats = self.__mmat.promocionalesDe(materia) 
        print("ManejadorInforme -> HacerInformesDe")
        for x in mats:
            print(f"{x.dni()} {x.nota()} {x.nombre()}")
        for m in mats:
            alu = self.__malu.obtenerAlumno(m.dni())
            print(f"{alu.nya()}")
            if alu is not None:
                informe = Informe(m.dni(),alu.nya(),m.fecha(),m.nota(),alu.anio())
                self.__informes.append(informe)
        return self.__informes


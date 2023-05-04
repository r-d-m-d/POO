import csv

from Materia import Materia


class ManejadorMateria:

    def __init__(self):
        self.__materias = []
        self.__cargadas = False

    def cargarMaterias(self,filename):
        with open(filename,encoding="8859") as fp:
            fp.readline()
            reader = csv.reader(fp,delimiter=";")
            for line in reader:
                self.__materias.append(Materia(*line))
        self.__cargadas = True

    def promedioConAplazos(self,dni):
        notasAplazos = [m.nota() for m in self.__materias if m.dni() == dni]
        if len(notasAplazos) > 0:
            promAplazos = sum(notasAplazos) / len(notasAplazos)
        else:
            promAplazos = -1
        return promAplazos

    def promedioSinAplazos(self,dni):
        notasSinAplazos = [n.nota() for n in self.__materias 
                           if n.dni() == dni  and n.nota() >= 4]
        if len(notasSinAplazos) > 0:
            promSinAplazos = sum(notasSinAplazos) / len(notasSinAplazos)
        else:
            promSinAplazos = -1
        return promSinAplazos

        return promSinAplazos
    
    def promocionalesDe(self,materia):
        return [m for m in self.__materias 
                if m.tieneNombre(materia) and m.tieneAprobacion('P') and m.nota() >= 7]

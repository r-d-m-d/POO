import typing
import csv

import Empleado
from Contratado import Contratado
from DePlanta import DePlanta
from Externo import Externo

from ManejaExterno import ManejaExterno
from ManejaDePlanta import ManejaDePlanta
from ManejaContratados import ManejaContratados

CONTFN = "contratados.csv"
DEPLFN = "planta.csv"
EXTEFN = "externos.csv"

if __name__ == "__main__":

from ManejaExterno import ManejaExterno
from ManejaDePlanta import ManejaDePlanta
from ManejaContratados import ManejaContratados

from ManejaEmpleados import ManejaEmpleados
CONTFN = "contratados.csv"
DEPLFN = "planta.csv"
EXTEFN = "externos.csv"

if __name__ == "__main__":
    me = ManejaEmpleados()
    me.cargarContratados(CONTFN)
    me.cargarDePlanta(DEPLFN)
    me.cargarExternos(EXTEFN)

    dni = input("ingrese dni: ")
    horas = int(input("ingrese horas trabajadas: "))
    me.agregarHoras(dni, horas)

    tarea = input("\nIngrese una tarea: ")
    ext = me.totalTarea(tarea)
    if ext is not None:
        print(f"{ext.tarea()} {ext.costoObra()}\n")
    else:
        print("Tarea no encontrada")

    print("Empleados ayuda economica.")
    for emp in me.cobranMenosDe(150000):
        print(emp)

    print("Calculo de sueldo")
    for e in me.mostrarSueldo():
        print(e)


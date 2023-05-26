from ManejaExterno import ManejaExterno
from ManejaDePlanta import ManejaDePlanta
from ManejaContratados import ManejaContratados

CONTFN = "contratados.csv"
DEPLFN = "planta.csv"
EXTEFN = "externos.csv"

if __name__ == "__main__":
    mc = ManejaContratados()
    mc.cargarEmpleados(CONTFN)
    mdp = ManejaDePlanta()
    mdp.cargarEmpleados(DEPLFN)
    mext = ManejaExterno()
    mext.cargarEmpleados(EXTEFN)

    dni = input("ingrese dni: ")
    horas = int(input("ingrese horas trabajadas: "))
    mc.agregarHoras(dni, horas)

    tarea = input("\nIngrese una tarea: ")
    ext = mext.totalTarea(tarea)
    if ext is not None:
        print(f"{ext.tarea()} {ext.costoObra()}\n")
    else:
        print("Tarea no encontrada")

    print("Empleados ayuda economica.")
    for emp in mc.cobranMenosDe(150000):
        print(emp)
    for emp in mdp.cobranMenosDe(150000):
        print(emp)
    for emp in mext.cobranMenosDe(150000):
        print(emp)

    print("Calculo de sueldo")
    for e in mc.mostrarSueldo():
        print(e)
    for e in mdp.mostrarSueldo():
        print(e)
    for e in mext.mostrarSueldo():
        print(e)

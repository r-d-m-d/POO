import csv
import PlanAhorro
FILENAME = "planes.csv"
def test():
    pa = PlanAhorro(1,"Toyota"," final",70987431)
if __name__ == "__main__":
# 1-Lea desde un archivo separado con “;” los datos de los planes y genere
# una lista que almacene instancias de la clase “PlanAhorro”.
    test()
    listaPlanes = []
    with open(FILENAME) as fp:
        reader = csv.reader(fp, delimiter=";")
        for fila in reader:
            cod = int(fila[0])
            importe = float(fila[3])
            nc = int(fila[4])
            ncl = int(fila[5])
            listaPlanes.append(
                    PlanAhorro.PlanAhorro(cod, fila[1], fila[2],
                                          importe))
# 2-Presente un menú de opciones permita:
    print("a)Actualizar valor del vehiculo de cada plan")
    print("b)Mostrar vehiculos por debajo de un valor")
    print("c)Mostrar monto licitacion")
    print("d)Modificar cantidad de cuotas para licitacion")
    opc = input("Ingrese una opcion: ")
# a.Actualizar el valor del vehículo de cada plan. Para esto se muestra el
# código del plan, el modelo y versión del vehículo, luego se ingresa el valor
# actual del vehículo y se modifica el atributo correspondiente.
    if opc == "a":
        for plan in listaPlanes:
            importe = input(f"{plan.codigo()} {plan.modelo()} {plan.version}")
            plan.importe(nimp=importe)
# b. Dado un valor, mostrar código del plan, modelo y versión del vehículo
# cuyo valor de la cuota sea inferior al valor dado.
    elif opc == "b":
        importe = input("Ingrese un importe: ")
        for plan in listaPlanes:
            if plan.importe < importe:
                print(f"{plan.codigo()} {plan.modelo()} {plan.version}")
# c. Mostrar el monto que se debe haber pagado para licitar el vehículo
# (cantidad de cuotas para licitar * importe de la cuota).
    elif opc == "c":
        pass # Consultar: cual vehiculo ? ingreso un codigo? muestro todos?
# d.Dado el código de un plan, modificar la cantidad cuotas que debe tener
# pagas para licitar. #### modificarlo para todos ####
    elif opc == "d":
        nc = int(input("ingrese la nueva cantidad de cuotas para licitar: "))
        PlanAhorro.ncuotaslic(ncl=nc)
    else:
        print(f"Opcion {opc} invalida.")

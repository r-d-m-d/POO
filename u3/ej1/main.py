import ManejaFacultades

filename = "facultadCarrera.csv"
if __name__ == "__main__":
    m = ManejaFacultades.ManejaFacultades()
    m.cargarCsv(filename)
    print("1)Mostrar carreras y facultades")
    print("2)Mostrar donde se dicta una carrera")
    opc = input("Ingrese una opcion: ")
    if opc == "1":
        cod = int(input("Ingrese el codigo de una facultad: "))
        facu = m.getFacu(cod)
        print(facu)
    elif opc == "2":
        nomb = input("Ingrese el nombre de una carrera: ")
        nomb = nomb.strip()
        carr = m.bucarCarrera(nomb)
        if carr is not None:
            print("Codigo de carrera: ",carr.codStr())
            facu = carr.getFacu()
            print(facu.strNombDir())
        else:
            print("Carrera no encontrada")
    else:
        print("Opcion invalida")

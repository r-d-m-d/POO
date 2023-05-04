import csv
import Registro

FILENAME = "varmet.csv"

def test():
    r = Registro.Registro(1,2,3)
    mm = Resgistro.MaxMin(1,2)
    vdh = Registro.ValDiaHora()
if __name__ == "__main__":
    test()
    dia = []
    horas = []
    with open(FILENAME) as fp:
        reader = csv.reader(fp)
        mes = []
        linea = next(reader, False)
        while linea is not False:
            diaIdx = int(linea[0]) - 1
            horaIdx = int(linea[1])
            dia = []
            while linea is not False and diaIdx == int(linea[0]) - 1:
                reg = Registro.Registro(int(linea[2]), int(linea[3]),
                                        int(linea[4]))
                dia.append(reg)
                linea = next(reader, False)
            mes.append(dia)
    print("1) maximos y minimos por humedad temperatura y presion.")
    print("2)Temperatura promedio mensual por cada hora")
    print("3) Listar los valores de las tres variables segun un dia")
    opc = input("ingrese una opcion: ")
    if opc == "1":
        maxMinTemp = Registro.MaxMin(mes[0][0].retornaTemp(),
                                     mes[0][0].retornaTemp())
        maxMinPres = Registro.MaxMin(mes[0][0].retornaPres(),
                                     mes[0][0].retornaPres())
        maxMinHume = Registro.MaxMin(mes[0][0].retornaHume(),
                                     mes[0][0].retornaHume())
        for cd, dia in enumerate(mes):
            for ch, hora in enumerate(dia):
                maxMinTemp.registraMaxOMin(hora.retornaTemp(), cd+1, ch)
                maxMinPres.registraMaxOMin(hora.retornaPres(), cd+1, ch)
                maxMinHume.registraMaxOMin(hora.retornaHume(), cd+1, ch)
        maxMinHume.mostrarMaximosYMinimos(prePrompt="Humedad")
        maxMinTemp.mostrarMaximosYMinimos(prePrompt="Teperatura")
        maxMinPres.mostrarMaximosYMinimos(prePrompt="Presion")
    elif opc == "2":
        proms = []
        for iHora in range(len(mes[0])):
            acum = 0
            for iDia in range(len(mes)):
                acum += mes[iDia][iHora].retornaTemp()
            proms.append(acum // len(mes))
        for hora, prom in enumerate(proms):
            print(f"hora: {hora} promedio: {prom}")
    elif opc == "3":
        dia = int(input("Ingrese un dia: "))
        print("{:^5}{:^12}{:^8}{:^8}".format("Hora", "Temperatura", "Humedad",
                                             "Presión"))
        if dia < len(mes):
            for cd, reg in enumerate(mes[dia]):
                print("{:^5}{:^12}{:^8}{:^8}".format(cd, reg.retornaTemp(),
                                                     reg.retornaHume(),
                                                     reg.retornaPres()))
    else:
        print("Opcion invalida")

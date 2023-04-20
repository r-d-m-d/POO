import csv
import re
import Email


class ControladorEmail():
    email_rgx = re.compile(
            r"[\w.-]+@[a-zA-Z0-9][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}(\.[a-zA-Z])*")

    def __init__(self):
        self.__emails = []

    def cargarArchivo(self, nombArchivo, invalidos=[]):
        emailFile = open(nombArchivo)
        emailReader = csv.reader(emailFile, delimiter=";")
        for fila in emailReader:
            email_s = ControladorEmail.email_rgx.match(fila[0])
            if email_s is None:
                invalidos.append(fila[0])
            else:
                email = Email.Email(cont=fila[1])
                email.crearCuenta(email_s.group())
                self.__emails.append(email)
        emailFile.close()

    def buscaDom(self, dom):
        return [e.retornaEmail() for e in self.__emails
                if e.getDominio() == dom]

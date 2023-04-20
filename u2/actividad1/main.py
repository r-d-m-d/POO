import Email
import ControladorEmail


def test():
    email=Email.Email("informatica","gmail","com","4a$afij123jklqj$54")
    email2=Email.Email()
    email2.crearCuenta("info@gmail.com","1nf0")
    email2.getDominio()
    cm=ControladorEmail.ControladorEmail()
    invalidos=[]
    cm.cargarArchivo("emails.csv",invalidos)
    cm.buscaDom("gmail")

if __name__ == "__main__":
    print("1)punto 1")
    print("2)punto 2")
    print("3)punto 3")
    print("4)punto 4")
    opc = int(input("ingrese una opcion: "))

    # 1)
    if opc == 1:
        nombre = input("ingrese su nombre: ")
        correo = input("ingrese su correo: ")
        cont = input("Ingrese la ontraseña: ")
        email = Email.Email()
        email.crearCuenta(correo, cont)
        print("Estimado {} te enviaremos tus mensajes a {}".
              format(nombre, email.retornaEmail()))
    # 2)
    elif opc == 2:
        print("Modificar contraseña")
        email = Email.Email()
        email.crearCuenta("user@example.com", "1234")
        c = input("Ingrese la contraseña: ")
        if email.esContrasena(c):
            cont = input("Ingrese la nueva contraseña: ")
            email.cambiarContrasena(cont)
        else:
            print("La contraseña ingresada es incorrecta: ")
    # 3)
    elif opc == 3:
        emails_str =input("Ingrese un email: ") 
        p=input("ingrese la contraseña: ")
        e = Email.Email()
        e.crearCuenta(emails_str, p)
    elif opc == 4:
        # 4)
        # a)
        contEmail = ControladorEmail.ControladorEmail()
        invalidos = []
        contEmail.cargarArchivo("emails.csv", invalidos)
        for email in invalidos:
            print("email invalido: {}".format(email))
        opc = input("Desea buscar por dominio: s/n: ")
        if opc == 's':
            # 4b)
            d = input("ingrese un dominio: ")
            for e in contEmail.buscaDom(d):
                print(e)

import Email
import ControladorEmail

print("1)punto 1")
print("2)punto 2")
print("3)punto 3")
print("4)punto 4 a")
print("5)punto 4 b")
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
    c = input("Ingrese la contraseña: ")
    if email.esContrasena(c):
        cont = input("Ingrese la nueva contraseña: ")
        email.cambiarContrasena(cont)
    else:
        print("La contraseña ingresada es incorrecta: ")
# 3)
elif opc == 3:
    emails_str = ["informatica.fcefn@gmail.com", "wicc2023@unsj-cuim.edu",
                  "juanLiendro1957@yahoo.com"]
    emails = []
    for s in emails_str:
        e = Email.Email()
        e.crearCuenta(s)
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

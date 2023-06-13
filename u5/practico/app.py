from flask import Flask, render_template, request, redirect, session
from hashlib import md5


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.from_pyfile("config.py")

from models import db
from models import Preceptor, Padre

def check_password_hash(clave_hasheada, clave_formulario):
    hash_clave_formulario = md5(clave_formulario.encode()).hexdigest()
    return clave_hasheada == hash_clave_formulario


@app.route('/', methods=['post', 'get'])
def login():
    if request.method == 'POST':
        if request.form['Usuario'] and request.form['contrasena']\
                and request.form['usuario-tipo']:
            # comprobar usuario y contrasena
            verif = False
            if request.form['usuario-tipo'] == 'preceptor':
                usuario = Preceptor.query.filter_by(correo=request.form['Usuario']).first()
                if isinstance(usuario, Preceptor):
                    verif = check_password_hash(usuario.clave,
                                                request.form['contrasena'])
            elif request.form['usuario-tipo'] == "padre":
                usuario = Padre.query.filter_by(correo=request.form['Usuario']).first()
                if isinstance(usuario, Padre):
                    verif = check_password_hash(usuario.clave,
                                                request.form['contrasena'])
            # devolver un template de bienvenida como panel.html o algo asi
            if verif:
                session['name'] = usuario.nombre
                return redirect(f'/panel/preceptor/{usuario.nombre}')
            else:
                return render_template('login.html', verif=False)
        else:
            return render_template('login.html', verif=True)
    elif request.method == 'GET':
        return render_template('login.html', verif=True)


@app.route('/panel', methods=['post', 'get'])
@app.route('/panel/<string:tipo_usuario>/<string:nombre>')
def panel(tipo_usuario=None, nombre=None):
    if session['name'] and session['name'] == nombre:
        return render_template('panel.html', tipo_usuario=tipo_usuario, nombre=nombre)
    return redirect('/')


if __name__ == "__main__":
    app.run()

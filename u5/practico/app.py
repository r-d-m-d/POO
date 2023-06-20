from datetime import datetime
from flask import Flask, render_template, request, redirect, session
from hashlib import md5


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.from_pyfile("config.py")

from models import db
from models import Preceptor,  Curso, Estudiante, Padre, Asistencia

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
                session['tipo'] = request.form['usuario-tipo']
                session['id'] = usuario.id
                print(session['id'])
                return redirect(f'/panel/{usuario.__class__.__name__}/{usuario.nombre}')
            else:
                return render_template('login.html', verif=False)
        else:
            return render_template('login.html', verif=True)
    elif request.method == 'GET':
        return render_template('login.html', verif=True)


@app.route('/panel', methods=['post', 'get'])
@app.route('/panel/<string:tipo_usuario>/<string:nombre>')
def panel(tipo_usuario=None, nombre=None):
    if session['name'] and session['name'] == nombre \
         and tipo_usuario in ['Preceptor', 'Padre']:
        return render_template('panel.html', tipo_usuario=tipo_usuario,
                               nombre=nombre)
    elif (tipo_usuario is None or nombre is None) and (
            session['name'] and session['tipo'] and session['id']):
        tipo_usuario = session.get('tipo', '')
        nombre_usuario = session.get('name', '')
        return redirect(f'/panel/{tipo_usuario}/{nombre_usuario}')
    return redirect('/')

@app.route('/seleccionar-curso', methods=['post','get'])
def seleccionar_curso():
    if session['tipo'] and session['tipo'] == "preceptor":
        # mostrar formulario de los cursos a cargo del Preceptor
        cursos = Curso.query.filter_by(idpreceptor=session['id']).all()
        print(cursos)
        return render_template('seleccionar-curso.html', cursos=cursos)
        # 
    return redirect('/login')

@app.route('/registrar-asistencia', methods=['POST'])
def registrarAsistencia():
    if request.method == 'POST':
        if request.form['curso']:
            curso_id = request.form['curso']
            # Pedir alumnos del cursoj
            estudiantes = Estudiante.query.filter_by(idcurso=curso_id).order_by(Estudiante.apellido).all()
            return render_template('registrar-asistencia.html', eds=estudiantes)
        else:
            print(type(request.form['estudiante']))
            return render_template('registrar-asistencia.html')
    return redirect('/')


@app.route('/guardar-asistencia', methods=['post'])
def guardar_asistencia():
    error = None
    if request.method == 'POST':
        for id_estudiante in request.form.keys():
        # verificar que el estudiante esta en el curso a cargo del preceptor
            estudiante = Estudiante.query.filter_by(id=id_estudiante).limit(1).first()
            if isinstance(estudiante, Estudiante):
                prec_id = session.get('id', -1)
                if estudiante.curso.idpreceptor == prec_id:
                    # Mal, deberia darle nombre a cada atributo
                    # sino depende del orden del formulario
                    presente, tipo_clase, fecha, justificacion = request.form.getlist(id_estudiante)
                    dAsistencia = {'fecha': datetime.strptime(fecha,
                                   "%Y-%m-%d").date(),
                                   'codigoclase': tipo_clase,
                                   'asistio': presente,
                                   'justificacion': justificacion,
                                   'idestudiante': id_estudiante}
                    asistencia = Asistencia(**dAsistencia)
                    db.session.add(asistencia)
                    db.session.commit()
                else: # supongamos que no es un padre 
                    prec_name = session.get('name', '')
                    error += f'El preceptor {prec_name} no esta acargo del estudiante {estudiante.nombre}'
        # guardar asistencia en la base de datos
        ## asistencia = (id, fecha, codigo-clase, asistio, justificacion, idestudiante)

    return render_template('guardar-asistencia.html', error = error)
    # Las inasistencias se registran para cualquier dia

@app.route('/informe-detallado', methods=['get', 'post'])
def informeDetallado():
    # seleccionar curso
    # mostrar tabla de asistencias por alumno
    return "hoal"

if __name__ == "__main__":
    app.run()
    

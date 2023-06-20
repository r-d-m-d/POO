from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Preceptor(db.Model):
    __tablename__ = 'preceptor'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable = False)
    correo = db.Column(db.String(120), nullable=False, unique=True)
    clave = db.Column(db.String(120),nullable=False)

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    anio = db.Column(db.String(80), nullable=False)
    division = db.Column(db.String(80), nullable=False)
    idpreceptor = db.Column(db.Integer, db.ForeignKey('preceptor.id'))
    
    preceptor = db.relationship('Preceptor',
                                backref=db.backref('curso', lazy=True))


class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable = False)
    dni = db.Column(db.String(10), nullable=False)
    idcurso = db.Column(db.Integer, db.ForeignKey('curso.id'))
    idpadre = db.Column(db.Integer, db.ForeignKey('padre.id'))

    curso = db.relationship('Curso',
                            backref=db.backref('estudiante',lazy=True))
    padre = db.relationship('Padre',
                            backref=db.backref('estudiante', lazy=True))

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    codigoclase = db.Column(db.Integer)
    asistio = db.Column(db.Text)
    justificacion = db.Column(db.String(100))
    idestudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id'),
                             nullable=False)

    estudiante = db.relationship('Estudiante',
                                 backref=db.backref('estudiante',lazy=True))

class Padre(db.Model):
    __tablename__ = 'padre'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable = False)
    correo = db.Column(db.String(120), nullable=False, unique=True)
    clave = db.Column(db.String(120),nullable=False)


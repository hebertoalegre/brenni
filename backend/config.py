from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

UPLOAD_FOLDER = os.path.abspath(r'backend\uploads')
ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__, template_folder=os.path.abspath('templates'))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] =SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///imports.db'
app.config['SQLALCHEMY_BINDS']={
    'exports':'sqlite:///exports.db', 
    'diccionarios': 'sqlite:///diccionarios.db'
    }

db = SQLAlchemy(app)

class ImportsdDB(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    regimen = db.Column(db.String(70), nullable = False)
    ano = db.Column(db.Integer, nullable = False)
    mes = db.Column(db.String(30), nullable = False)
    pais = db.Column(db.String(60), nullable = False)
    cuode = db.Column(db.String(100), nullable = False)
    sac = db.Column(db.Float, nullable = False)
    cif = db.Column(db.Float, nullable = False)
    vol = db.Column(db.Float, nullable = False)
    unidades = db.Column(db.String(50), nullable = False)
    dai = db.Column(db.Float, nullable = False)
    sac_descriptor = db.Column(db.String(100), nullable = False)

    
class ExportsDB(db.Model):
    __bind_key__='exports'
    id = db.Column(db.Integer, primary_key=True)
    regimen = db.Column(db.String(70), nullable = False)
    ano = db.Column(db.Integer, nullable = False)
    mes = db.Column(db.String(30), nullable = False)
    pais = db.Column(db.String(60), nullable = False)
    sac = db.Column(db.Float, nullable = False)
    fob = db.Column(db.Float, nullable = False)
    vol = db.Column(db.Float, nullable = False)
    unidades = db.Column(db.String(50), nullable = False)
    sac_descriptor = db.Column(db.String(100), nullable = False)

class Diccionarios(db.Model):
    __bind_key__ ='diccionarios'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
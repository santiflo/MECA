from flask import Flask, make_response, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import config

#Inicializadores
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Models
from app.Models import Users
from app.Models import Documentaries
from app.Models import Multimedia
from app.Models import Type

#Controllers
from app.Controllers import Controller_Users

"""
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/string/')
def return_string():
    return 'Hello, world!'	

@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world!', 200,headers)	

@app.route('/tuple/')
def return_tuple():
    return 'Hello, world!', 200, {'Content-Type':'text/plain'}

@app.route('/login')
def login():
	abort(401)
	# Esta línea no se ejecuta

@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada...', 404
"""
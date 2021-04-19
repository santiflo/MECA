from flask import Flask, make_response, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app import config

#Inicializadores
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


#Models
from app.Models import Model_Users
from app.Models import Model_Documentaries
from app.Models import Model_Multimedia
from app.Models import Model_Types
from app.Models import Model_Categories

#Controllers
from app.Controllers import Controller_Users
from app.Controllers import Controller_Types
from app.Controllers import Controller_Documentaries
#from app.Controllers import Controller_Multimedia

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
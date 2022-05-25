from flask import Flask, make_response, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app import config

#Inicializadores
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app, resources={r"/*": {"origins": "*"}})

#Models
from app.Models import Model_Users
from app.Models import Model_Virtual_Expositions
from app.Models import Model_Multimedia
from app.Models import Model_Types
from app.Models import Model_Comments
from app.Models import Model_Questions
from app.Models import Model_Answers

#Controllers
from app.Controllers import Controller_Users
from app.Controllers import Controller_Login
from app.Controllers import Controller_Sign_In
#from app.Controllers import Controller_errors

#from app.Controllers import Controller_Types
#from app.Controllers import Controller_Documentaries
#from app.Controllers import Controller_Categories
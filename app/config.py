import os

DEBUG = False
SQLALCHEMY_DATABASE_URI = "mysql://admin:password@admmeca.c0edulkmjniv.us-east-1.rds.amazonaws.com/ADMMECA"
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.join(os.getcwd(),'Images')
MAX_CONTENT_LENGTH = 4 * 1000 * 1000
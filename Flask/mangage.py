from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.app import app, db

manager = Manager(app)

app.config['DEBUG'] = True # Ensure debugger will load.

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

""" Comandos"""
"""
py mangage.py migrate db init 	-> Inicia la migracion
py mangage.py db migrate 		-> Migra el modelo a la base de datos 
py mangage.py db upgrade		-> Ejecuta la migracion
"""
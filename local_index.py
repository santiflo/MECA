import os
from app.app import app, db
from app.Models.Model_Users import Schema_Users

db.create_all()

def create_admin_user():
	admin_data = {
	'name': 'administrador', 
	'last_name_1': '', 
	'last_name_2': '', 
	'email': 'proyecto.meca.cali@gmail.com', 
	'password_hash': 'Hola1234!', 
	'admin': 1, 
	'born_date': None, 
	'describe': 'Administrador de la aplicacion', 
	'verify_email': True, 
	'picture': 'https://cdn-icons-png.flaticon.com/512/2942/2942813.png'}
	User = Schema_Users().load(admin_data)
	db.session.add(User)
	db.session.commit()
	print('created')

#create_admin_user()

#app.run(debug=True , host="0.0.0.0", port = int(port))
# Para local
app.run(debug=True , host="0.0.0.0")
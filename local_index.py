from app.app import app, db
from app.Models.Model_Users import Schema_Users
from app.Models.Model_Types import Schema_Types

db.create_all()

def inser():
	#Usuario administrador
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

	# Tipos de datos
	# Subtitle
	subtitle_type = {
	'name' : 'Subtitle',
	'description' : 'Campo de texto que permite crear un subtitulo'
	}
	Type = Schema_Types().load(subtitle_type)
	db.session.commit()
	# Video
	video_type = {
	'name' : 'Video',
	'description' : 'Campo de texto que permite cargar la ruta de un video'
	}
	Type = Schema_Types().load(video_type)
	db.session.commit()
	# Images
	image_type = {
	'name' : 'Image',
	'description' : 'Campo de texto que permite cargar la ruta de una imagen'
	}
	Type = Schema_Types().load(image_type)
	db.session.commit()
	print('created')

#insert()

app.run(debug=True , host="0.0.0.0")
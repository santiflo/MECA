import os
import json
from app.app import app, db, ma
from flask import request, jsonify, url_for, send_from_directory, flash
from app.Models.Model_Multimedia import Model_Multimedia, Schema_Multimedia
from app.Models.Model_Types import Model_Types
from werkzeug.utils import secure_filename

url = 'https://proyecto-meca-cali.herokuapp.com/'

@app.route('/Multimedia/Create', methods = ["POST"])
def create_Multimedia():
	json = request.get_json(force=True)
	print(json)
	Multimedia = Schema_Multimedia().load(request.get_json())
	db.session.add(Multimedia)
	db.session.commit()
	return "Creado", 201

@app.route('/Multimedia/<virtual_exposition_id>/<type_name>', methods = ["GET"])
def getUserExpositionText(virtual_exposition_id, type_name):
	Type = Model_Types.query.filter(Model_Types.name.ilike('%'+type_name+'%')).first()
	type_id = Type.id
	print(type_name, type_id)
	Multimedia = Model_Multimedia.query.filter(
		Model_Multimedia.virtual_exposition_id == virtual_exposition_id, 
		Model_Multimedia.type_id == type_id
		)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Multimedia/Delete/<multimedia_id>', methods = ["DELETE"])
def Delete_Multimedia(multimedia_id):
	Multimedia = Model_Multimedia.query.get(multimedia_id)
	db.session.delete(Multimedia)
	db.session.commit()
	return "OK", 200

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/Multimedia/Upload/Image/<virtual_exposition_id>/<user_id>/<text>', methods=['POST'])
def upload_file(virtual_exposition_id, user_id, text):
	# check if the post request has the file part
	if 'file' not in request.files:
		print('archivo vacio')
		flash('No file part')
		return "No existe ninguna imagen en la peticion", 204
	file = request.files['file']
	# If the user does not select a file, the browser submits an
	# empty file without a filename.
	if file.filename == '':
		flash('No selected file')
		print('Archivo sin nombre')
		return "El archivo no cuenta con ningun nombre", 204
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = {
			'path' : str('https://proyecto-meca-cali.herokuapp.com'+url_for('download_file', name=filename)),
			'text' : text
			'virtual_exposition_id' : int(virtual_exposition_id),
			'user_id' : int(user_id)
			'type_id' : 3
		}
		#json['path'] = str('https://proyecto-meca-cali.herokuapp.com'+url_for('download_file', name=filename))
		#Multimedia = Schema_Multimedia().load(json)
		#db.session.add(Multimedia)
		#db.session.commit()
		print('Existoso')
		return "Proceso exitoso", 201
	print('error general')
	return "Error a la hora de subir la imgen", 204

@app.route('/Images/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)
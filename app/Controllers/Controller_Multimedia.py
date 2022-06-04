from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Multimedia import Model_Multimedia, Schema_Multimedia
from app.Models.Model_Types import Model_Types

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
"""
@app.route('/Multimedia/<virtual_exposition_id>/<type>', methods = ["GET"])
def getUserExpositionSubtitle(virtual_exposition_id):
	type_id = 2
	Multimedia = Model_Multimedia.query.filter(
		Model_Multimedia.virtual_exposition_id == virtual_exposition_id, 
		Model_Multimedia.type_id == type_id
		)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Multimedia/<virtual_exposition_id>/Video', methods = ["GET"])
def getUserExpositionVideo(virtual_exposition_id):
	type_id = 3
	Multimedia = Model_Multimedia.query.filter(
		Model_Multimedia.virtual_exposition_id == virtual_exposition_id, 
		Model_Multimedia.type_id == type_id
		)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Multimedia/<virtual_exposition_id>/Images', methods = ["GET"])
def getUserExpositionImage(virtual_exposition_id):
	type_id = 5
	Multimedia = Model_Multimedia.query.filter(
		Model_Multimedia.virtual_exposition_id == virtual_exposition_id, 
		Model_Multimedia.type_id == type_id
		)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200
"""
@app.route('/Multimedia/Delete/<multimedia_id>', methods = ["DELETE"])
def Delete_Multimedia(multimedia_id):
	Multimedia = Model_Multimedia.query.get(multimedia_id)
	db.session.delete(Multimedia)
	db.session.commit()
	return "OK", 200
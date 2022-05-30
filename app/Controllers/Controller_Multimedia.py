from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Multimedia import Model_Multimedia, Schema_Multimedia

@app.route('/Multimedia/Create', methods = ["POST"])
def create_Multimedia():
	json = request.get_json(force=True)
	print(json)
	Multimedia = Schema_Multimedia().load(request.get_json())
	db.session.add(Multimedia)
	db.session.commit()
	return "Creado", 201

@app.route('/Multimedia/<virtual_exposition_id>/Text', methods = ["GET"])
def getUserExpositionText(virtual_exposition_id):
	type_id = 4
	Multimedia = Model_Multimedia.query.filter(
		(
			Model_Multimedia.virtual_exposition_id == virtual_exposition_id, 
			Model_Multimedia.type_id == type_id
			)
		)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Multimedia/<virtual_exposition_id>/Subtitle', methods = ["GET"])
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
		and_(
			Model_Multimedia.virtual_exposition_id.ilike(virtual_exposition_id), 
			Model_Multimedia.type_id.ilike(type_id)
			)
		)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Multimedia/<exposition_id>/Images', methods = ["GET"])
def getUserExpositionImage(virtual_exposition_id):
	type_id = 5
	Multimedia = Model_Multimedia.query.filter(
		and_(
			Model_Multimedia.virtual_exposition_id.ilike(virtual_exposition_id), 
			Model_Multimedia.type_id.ilike(type_id)
			)
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
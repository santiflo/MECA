from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Virtual_Expositions import Model_Virtual_Expositions, Schema_Virtual_Expositions

@app.route('/VirtualExpositions/Create', methods = ["POST"])
def create_Expositions():
	json = request.get_json(force=True)
	print(json)
	Exposition = Schema_Virtual_Expositions().load(request.get_json())
	db.session.add(Exposition)
	db.session.commit()
	return "Exposicion creada", 201

@app.route('/VirtualExpositions', methods = ["GET"])
def all_Expositions():
	Exposition = Model_Virtual_Expositions.query.all()
	json = Schema_Virtual_Expositions(many = True).dump(Exposition)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/VirtualExpositions/Search/title/<exposition_title>', methods = ["GET"])
def search_Exposition_name(exposition_title):
	Exposition = Model_Virtual_Expositions.query.filter(Model_Virtual_Expositions.name.ilike('%'+exposition_title+'%')).all()
	json = Schema_Virtual_Expositions(many = True).dump(Exposition)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/VirtualExpositions/Search/id/<exposition_id>', methods = ["GET"])
def search_Exposition_id(exposition_id):
	Exposition = Model_Virtual_Expositions.query.get(exposition_id).first()
	json = Schema_Virtual_Expositions().dump(Exposition)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/VirtualExpositions/Update', methods = ["PUT"])
def update_Exposition():
	json = request.get_json(force=True)
	id = json['id']
	title = json['title']
	description = json['description']
	picture = json['picture']
	background = json['background']
	estructure = json['structure']
	bibliography = json['bibliography']
	Exposition = Model_Virtual_Expositions.query.get(id)
	if Exposition.user_id == json['user_id']:
		if title != '' : Exposition.title = title
		if description != '' : Exposition.description = description
		if picture != '' : Exposition.picture = picture
		if background != '': Exposition.background = background
		if estructure  != '': Exposition.estructure = estructure
		if bibliography != '': Exposition.bibliography = bibliography
		db.session.commit()
		return "OK", 202 
	else: return "No es propietario de la exposicion", 204

@app.route('/VirtualExpositions/Delete/<exposition_id>', methods = ["DELETE"])
def delete_Exposition(exposition_id):
	Exposition = Model_Virtual_Expositions.query.get(exposition_id)
	db.session.delete(Exposition)
	db.session.commit()
	return "OK", 200

@app.route('/VirtualExpositions/Menu', methods = ["GET"])
def VirtualExpositionsMenu():
	Expositions = Model_Virtual_Expositions.query.with_entities(
		Model_Virtual_Expositions.id,
		Model_Virtual_Expositions.title,
		Model_Virtual_Expositions.picture
	).all()
	json = Schema_Virtual_Expositions(many = True).dump(Expositions)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200
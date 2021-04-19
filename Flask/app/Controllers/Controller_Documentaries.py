from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Documentaries import Model_Documentaries, Schema_Documentaries

@app.route('/Documentaries/Create', methods = ["POST"])
def create_Documentry():
	documentary = Schema_Documentaries().load(request.get_json())
	db.session.add(documentary)
	db.session.commit()
	return "OK", 201

@app.route('/Documentaries', methods = ["GET"])
def all_Documentaries():
	Documentaries = Model_Documentaries.query.all()
	json = Schema_Documentaries(many = True).dump(Documentaries)
	return jsonify(json), 200

@app.route('/Documentaries/Search/name/<documentary_name>', methods = ["GET"])
def search_Documentaries_name(documentary_name):
	Documentaries = Model_Documentaries.query.filter(Model_Documentaries.name.ilike('%'+documentary_name+'%')).all()
	json = Schema_Documentaries(many = True).dump(Documentaries)
	return jsonify(json), 200

@app.route('/Documentaries/Search/id/<documentary_id>', methods = ["GET"])
def search_Documentary_id(documentary_id):
	Documentary = Model_Documentaries.query.get(documentary_id)
	json = Schema_Documentaries().dump(Documentary)
	return jsonify(json), 200

@app.route('/Documentaries/Update', methods = ["PUT"])
def update_Documentary():
	json = request.get_json()
	id = json['id']
	name = json['name']
	description = json['description']
	documentary = Model_Documentaries.query.get(id)
	if name != '' : documentary.name = name
	if description != '' : documentary.description = description
	db.session.commit()
	return "OK", 202 

@app.route('/Documentaries/Delete/<documentary_id>', methods = ["DELETE"])
def delete_Documentary(documentary_id):
	documentary = Model_Documentaries.query.get(documentary_id)
	db.session.delete(documentary)
	db.session.commit()
	return "OK", 200
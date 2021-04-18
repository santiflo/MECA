from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Types import Model_Types, Schema_Types

@app.route('/Types/Create',  methods = ["POST"])
def create_Type():
	req_data = Schema_Types().load(request.get_json())
	db.session.add(req_data)
	db.session.commit()
	return "OK", 201

@app.route('/Types', methods = ["GET"])
def all_Types():
	Types = Model_Types.query.all()
	json = Schema_Types(many=True).dump(Types)
	return jsonify(json),200

@app.route('/Types/Search/name/<type_name>', methods = ["GET"])
def search_Type_name(type_name):
	Types = Model_Types.query.filter(Model_Types.name.ilike('%'+type_name+'%')).all()
	json = Schema_Types(many=True).dump(Types)
	return jsonify(json),200

@app.route('/Types/Search/id/<type_id>', methods = ["GET"])
def search_Type_id(type_id):
	Type = Model_Types.query.get(type_id)
	json = Schema_Types().dump(Type)
	return jsonify(json),200

@app.route('/Types/Update', methods = ["PUT"])
def update_Type():
	req_data = request.get_json()
	id = req_data['id']
	name = req_data['name']
	description = req_data['description']
	Type = Model_Types.query.get(id)
	if Type.name != '' : Type.name = name
	if Type.description != '' : Type.description = description
	db.session.commit()
	return "OK",202

@app.route('/Types/Delete/<type_id>',  methods = ["DELETE"])
def delete_Type(type_id):
	Type = Model_Types.query.get(type_id)
	db.session.delete(Type)
	db.session.commit()
	return "OK", 200
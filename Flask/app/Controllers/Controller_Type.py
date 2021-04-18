from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Type import Model_Type, Schema_Type

@app.route('/Type/Create',  methods = ["POST"])
def create_Type():
	req_data = Schema_Type().load(request.get_json())
    db.session.add(req_data)
    db.session.commit()
    return "OK", 201

@app.route('/Type/Delete/<type_id>',  methods = ["DELETE"])
def delete_Type(type_id):
	Type = Model_Type.query.get(type_id)
    db.session.delete(Type)
    db.session.commit()
    return "OK", 200

@app.route('/Type', methods = ["GET"])
def all_Types():
	Types = Model_Type.query.all()
    json = Schema_Type(many=True).dump(Types)
    return jsonify(json),200

@app.route('/Type/Search/<type_name>', methods=["GET"])
def search_Type(type_name):
	Types = Model_Type.query.filter(Model_Type.name='%type_name%').all()
	json = Schema_Type(many=True).dump(Types)
	return jsonify(json),200

@app.route('/Type/Update', methods=["PUT"])
def search_Type(type_id):
	req_data = request.get_json()
	id = req_data['id']
	name = req_data['name']
	update = Model_Type.query.filter_by(id = id).first()
	update.name = name
	db.session.commit()
	return "OK",202
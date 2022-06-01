from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Comments import Model_Comments, Schema_Comments

@app.route('/Comments/Create', methods = ["POST"])
def create_Comments():
	json = request.get_json(force=True)
	print(json)
	Comment = Schema_Virtual_Expositions().load(json)
	db.session.add(Comment)
	db.session.commit()
	return "Exposicion creada", 201

@app.route('/Comments', methods = ["GET"])
def all_Comments():
	Comments = Model_Comments.query.all()
	json = Schema_Users(many = True).dump(Comments)
	return jsonify(json), 200

@app.route('Comments/VirtualExposition/<virtual_exposition_id>', methods = ["GET"])
def Comments_by_virtual_exposition():
	Comments = Model_Comments.query.filter(Model_Comments.virtual_exposition_id == virtual_exposition_id)
	json = Schema_Multimedia(many = True).dump(Multimedia)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('Comments/Update', methods = ["PUT"])
def update_comment():
	json = request.get_json(force=True)
	id = json['id']
	comment = json['comment']
	Comment = Model_Comments.query.get(id)
	if comment != '' : Comment.comment = comment
	db.session.commit()
	return "OK", 200
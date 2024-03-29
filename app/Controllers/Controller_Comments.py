from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Comments import Model_Comments, Schema_Comments

@app.route('/Comments/Create', methods = ["POST"])
def create_Comments():
	json = request.get_json(force=True)
	print(json)
	Comment = Schema_Comments().load(json)
	db.session.add(Comment)
	db.session.commit()
	return "Comentario creado creada", 201

@app.route('/Comments', methods = ["GET"])
def all_Comments():
	Comments = Model_Comments.query.all()
	json = Schema_Comments(many = True).dump(Comments)
	return jsonify(json), 200

@app.route('/Comments/VirtualExposition/<virtual_exposition_id>', methods = ["GET"])
def Comments_by_virtual_exposition(virtual_exposition_id):
	Comments = Model_Comments.query.filter(Model_Comments.virtual_exposition_id == virtual_exposition_id)
	json = Schema_Comments(many = True).dump(Comments)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Comments/Update', methods = ["PUT"])
def update_comment():
	json = request.get_json(force=True)
	id = json['id']
	comment = json['comment']
	Comment = Model_Comments.query.get(id)
	if comment != '' : Comment.comment = comment
	db.session.commit()
	return "OK", 200

@app.route('/Comments/Delete/<Comment_id>',  methods = ["DELETE"])
def delete_Comment(Comment_id):
	Comment = Model_Comments.query.get(Comment_id)
	db.session.delete(Comment)
	db.session.commit()
	return "OK", 200
from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Questions import Model_Questions, Schema_Questions

@app.route('/Questions/Create', methods = ["POST"])
def create_Question():
	json = request.get_json(force=True)
	print(json)
	Question = Schema_Questions().load(request.get_json())
	db.session.add(Question)
	db.session.commit()
	return "Pregunta creada", 201

@app.route('/Questions', methods = ["GET"])
def all_Questions():
	Questions = Model_Questions.query.all()
	json = Schema_Questions(many = True).dump(Questions)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/Questions/Update', methods = ["PUT"])
def update_Question():
	json = request.get_json(force = True)
	id = json['id']
	name = json['name']
	description = json['description']
	answer = json['answer']
	question = Model_Questions.query.get(id)
	if question != None:
		if name != '' : question.name = name
		if description != '' : question.description = description
		if answer != '' : question.answer = answer
		db.session.commit()
	else:
		return "La pregunta no existe", 204

@app.route('/Questions/Delete/<Question_id>', methods = ["DELETE"])
def delete_Question(Question_id):
	Question = Model_Questions.query.get(Question_id)
	db.session.delete(Question)
	db.commit()
	return "OK", 200
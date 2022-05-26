from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Users import Model_Users, Schema_Users

@app.route('/Users/Registrar',  methods = ["POST"])
def create_User():
	User = Schema_Users().load(request.get_json())
	db.session.add(User)
	db.session.commit()
	return "OK", 201

@app.route('/Users', methods = ["GET"])
def all_Users():
	Users = Model_Users.query.all()
	json = Schema_Users(many = True).dump(Users)
	return jsonify(json), 200

@app.route('/User', methods = ["GET"])
def search_User_name(user_name):
	Users = Model_Users.query.filter(Model_Users.username.ilike('%'+user_name+'%')).all()
	json = Schema_Users(many = True).dump(Users)
	return jsonify(json), 200

@app.route('/Users/Search/id/<user_id>', methods = ["GET"])
def search_User_id(user_id):
	User = Model_Users.query.get(user_id)
	json = Schema_Users().dump(User)
	return jsonify(json), 200

@app.route('/Users/Actualizar', methods = ["PUT"])
def update_User():
	json = request.get_json()
	id = json['id']
	name = json['name']
	last_name_1 = json['last_name_1']
	last_name_2 = json['last_name_2']
	email = json['email']
	born_date = json['born_date']
	describe = json['describe']
	User = Model_Users.query.get(id)
	if name != '': User.name = name
	if last_name_1 != '': User.last_name_1 = last_name_1
	if last_name_2 != '': User.last_name_2 = last_name_2
	if email != '': User.email = email
	if born_date != '': User.born_date = born_date
	if describe != '': User.describe = describe
	db.session.commit()
	return "OK", 200

@app.route('/Users/Update/password', methods = ["PUT"])
def update_User_password():
	json = request.get_json()
	id = json['id']
	username = json['username']
	password = json['password']
	User = Model_Users.query.get(id)
	if User.username == username and User.password != password: User.password = password
	return "OK", 200


@app.route('/Users/Delete/<user_id>', methods = ["DELETE"])
def delte_User(user_id):
	User = Model_Users.query.get(user_id)
	db.session.delete(User)
	db.session.commit()
	return "OK", 200

@app.route('/MenuBar/<user_id>', methods = ["GET"])
def MenuBar(user_id):
	User = Model_Users.query.get(user_id)
	if User is None:
		return "El usuario no existe", 204
	else:
		response = jsonify(
			nombre = User.name,
			picture = User.picture)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 200
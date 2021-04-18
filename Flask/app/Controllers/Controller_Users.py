from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Users import Model_Users, Schema_Users

@app.route('/Users/Create',  methods = ["POST"])
def create_User():
	req_data = Schema_Users().load(request.get_json())
	print('prueba', req_data)
	db.session(req_data)
	#db.session.commit()
	return "OK", 201

@app.route('/Users', methods = ["GET"])
def all_Users():
	Users = Model_Users.query.all()
	json = Schema_Users(many = True).dump(Types)
	return jsonify(json), 200

@app.route('/Users/Search/name/<user_name>', methods = ["GET"])
def search_User_name(user_name):
	Users = Model_Users.query.filter(Model_Users.name.ilike('%'+user_name+'%')).all()
	json = Schema_Users(many = True).dump(Users)
	return jsonify(json), 200

@app.route('/Users/Search/id/<user_id>', methods = ["GET"])
def search_User_id(user_id):
	User = Model_Users.query.get(user_id)
	json = Schema_Users().dump(User)
	return jsonify(json), 200

@app.route('/Users/Update', methods = ["PUT"])
def update_User():
	req_data = request.get_json()
	id = req_data['id']
	name = req_data['name']
	email = req_data['email']
	User = Model_Users.query.get(id)
	if name != '': User.name = name
	if email != '': User.email = email
	db.session.commit()
	return "OK", 200

@app.route('/Users/Update/password', methods = ["PUT"])
def update_User_password():
	req_data = request.get_json()
	id = req_data['id']
	username = req_data['username']
	password = req_data['password']
	User = Model_Users.query.get(id)
	if User.username == username and User.password != password: User.password = password
	return "OK", 200


@app.route('/Users/Delete/<user_id>', methods = ["DELETE"])
def delte_User(user_id):
	User = Model_Users.query.get(user_id)
	db.session.delete(User)
	db.session.commit()
	return "OK", 200
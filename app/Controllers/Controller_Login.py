from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Users import Model_Users, Schema_Users

@app.route('/Login', methods = ["POST"])
def login_User():
	json = request.get_json(force=True)
	print(json['email'],json['password_hash'])
	User = Model_Users.query.filter_by(email = json['email']).first()
	if User.password_hash == json['password_hash']:
		response = jsonify(
			id = User.id,
			admin = User.admin
			)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 202
	else: return "Bad user or password", 204
	#return "Bad user or password", 204

@app.route('/', methods = ["GET"])
def index():
	return "En la buena manito", 201


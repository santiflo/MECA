from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Users import Model_Users, Schema_Users

@app.route('/Sign_in', methods = ["POST"])
def Sign_In_User():
	json = request.get_json()
	print(
		json['name'], '\n',
		json['last_name_1'], '\n',
		json['last_name_2'], '\n',
		json['email'], '\n',
		json['password_hash'], '\n',
		json['username'], '\n',
		json['admin'], '\n',
		json['born_date'], '\n',
		json['describe']
	)
	User = Schema_Users().load(request.get_json())
	db.session.add(User)
	db.session.commit()
	return "Creado", 201
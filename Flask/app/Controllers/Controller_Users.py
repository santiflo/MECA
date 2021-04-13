from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Users import Users, Users_Schema

@app.route('/createUser',  methods = ["POST"])
def create_User():
	"""
	req_data = CategoriaSchema().load(request.get_json())
	db.session.add(req_data)
	db.session.commit()
	return "OK", 201
	"""
	return 'Crear usuario'

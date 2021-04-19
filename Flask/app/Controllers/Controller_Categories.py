from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Categories import Model_Categories, Schema_Categories

@app.route('/Categories/Create', methods = ["POST"])
def create_Category():
	Category = Schema_Categories().load(request.get_json())
	db.session.add(Category)
	db.session.commit()
	return "OK", 201

@app.route('/Categories', methods = ["GET"])
def all_Categories():
	Categories = Model_Categories.query.all()
	json = Schema_Categories(many = True).dump(Categories)
	return jsonify(json), 200

@app.route('/Categories/Search/name/<category_name>', methods = ["GET"])
def search_Category_name(category_name):
	Categories = Model_Categories.query.filter(Model_Categories.name.ilike('%'+category_name+'%'))
	json = Schema_Categories(many = True).dump(Categories)
	return jsonify(json), 200

@app.route('/Categories/Search/id/<category_id>', methods = ["GET"])
def search_Category_id(category_id):
	Category = Model_Categories.query.get(category_id)
	json = Schema_Categories().dump(Category)
	return jsonify(json), 200

@app.route('/Category/Update', methods = ["PUT"])
def update_Category():
	json = request.get_json()
	id = json['id']
	name = json['name']
	Category = Model_Categories.query.get(id)
	if name != '': Category.name = name
	db.session.commit()
	return "OK", 200

@app.route('/Category/Delete/<user_id>', methods = ["DELETE"])
def delete_Category(user_id):
	Category = Model_Categories.query.get(category_id)
	db.session.delete(Category)
	db.session.commit()
	return "OK", 200
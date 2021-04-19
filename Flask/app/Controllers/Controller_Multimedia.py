from app.app import app, db, ma
from flask import request, jsonify
from app.Models.Model_Multimedia import Model_Multimedia, Schema_Multimedia

@app.route('/Multimedia/Create', methods = ["POST"])
def create_Multimedia():
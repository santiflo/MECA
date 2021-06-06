from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from app.app import db, ma
from marshmallow import post_load
from app.Models.Model_File import Model_File

class Model_File_Types(db.Model):
	#Atributos
	__tablename__ = 'TBL_FILE_TYPES'
	id = 			Column(Integer, primary_key = True)
	name = 			Column(String(50), nullable = False, unique = True)
	description = 	Column(String(255), nullable = False, unique = True, default = 'blank')
	#Foraneos
	#Relaciones
	file = relationship('Model_File', backref = 'Type', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_File_Types(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_File_Types

    @post_load
    def make_File_Types(self, data, **kwargs):
        return Model_File_Types(**data)
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from app.app import db, ma
from marshmallow import post_load
from app.Models.Model_Multimedia import Model_Multimedia

class Model_Type(db.Model):
	#Atributos
	__tablename__ = 'TBL_TYPE'
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False, unique = True)
	description = Column(Text, nullable = False, unique = True)
	#Foraneos
	#Relaciones
	multimedia = relationship('Model_Multimedia', backref = 'Type', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Type(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Type

    @post_load
    def make_Type(self, data, **kwargs):
        return Model_Type(**data)
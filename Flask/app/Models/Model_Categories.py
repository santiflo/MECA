from sqlalchemy import Boolean, Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Documentaries import Model_Documentaries

class Model_Categories(db.Model):
	#Atributos
	__tablename__ = 'TBL_CATEGORIES'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	#Foraneos
	#Relaciones
	documentaries = relationship('Model_Documentaries', backref = 'Categories', lazy = 'dynamic')
	#Trigger

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Categories(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Model_Categories

	@post_load
	def make_Categories(self, data, **kwargs):
		return Model_Categories(**data)
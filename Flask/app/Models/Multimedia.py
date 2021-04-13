from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from app.app import db
from app.Models import Documentaries, Type

class Multimedia(db.Model):
	#Atributos
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable= False, unique = True)
	#Foraneos
	documentalId = Column(Integer, ForeignKey('documentaries.id'), nullable = False, unique = True)
	TypeId = Column(Integer, ForeignKey('type.id'), nullable = False)
	#Relaciones
	documentaries = relationship('Documentaries', backref = 'Multimedia')
	Type = relationship('type', backref = 'Multimedia')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
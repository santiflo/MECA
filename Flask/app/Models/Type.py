from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from app.app import db
from app.Models import Multimedia

class Type(db.Model):
	#Atributos
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False, unique = True)
	description = Column(Text, nullable = False, unique = True)
	#Foraneos
	#Relaciones
	multimedia = relationship('Multimedia', backref = 'Type', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

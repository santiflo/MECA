from sqlalchemy import Boolean, Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from app.app import db
from app.Models import Documentaries


class Users(db.Model):
	#Atributos
	id = Column(Integer, primary_key = True)
	name = Column(String(20), nullable = False)
	email = Column(String(50), nullable = False, unique = True)
	password = Column(String(20), nullable = False)
	username	 = Column(String(20), nullable = False, unique = True)
	#Foraneos
	#Relaciones
	documental = db.relationship('Documentaries', backref ='Users', lazy ='dynamic')
#	Trigger        
#	__table_args__ = (
#		db.CheckConstraint('length("password") >= 7', name='password_min_length')
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))
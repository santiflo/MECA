from sqlalchemy import Boolean, Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Documentaries import Model_Documentaries


class Model_Users(db.Model):
	#Atributos
	__tablename__ = 'TBL_USERS'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	email = Column(String(100), nullable = False, unique = True)
	password_hash = Column(String(128), nullable = False)
	username = Column(String(50), nullable = False, unique = True)
	admin = Column(Boolean, nullable = False, default = False)
	#Foraneos
	#Relaciones
	documentaries = db.relationship('Model_Documentaries', backref ='Users', lazy ='dynamic')
	#Trigger        
	#	__table_args__ = (db.CheckConstraint('length("password") >= 7', name='password_min_length')
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)	

class Schema_Users(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Users

    @post_load
    def make_Users(self, data, **kwargs):
        return Model_Users(**data)


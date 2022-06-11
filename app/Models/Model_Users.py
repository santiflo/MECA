from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Virtual_Expositions import Model_Virtual_Expositions
from app.Models.Model_Multimedia import Model_Multimedia
from app.Models.Model_Comments import Model_Comments
from app.Models.Model_Questions import Model_Questions

class Model_Users(db.Model):
	#Atributos
	__tablename__ = 'TBL_USERS'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	last_name_1 = Column(String(50), nullable = True)
	last_name_2 = Column(String(50), nullable = True)
	email = Column(String(100), nullable = False, unique = True)
	password_hash = Column(String(128), nullable = False)
	admin = Column(Integer, nullable = False, default = 0) # 0 user, 1 = admin
	born_date = Column(DateTime, nullable = True)
	describe = Column(Text, nullable = True)
	verify_email = Column(Boolean, nullable = False, default = False)
	picture = Column(Text, nullable = True, default = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Stick_Figure.svg/170px-Stick_Figure.svg.png?20070219055013')
	req_admin = Column(Integer, nullable = False, default = 0)
	#Foraneos
	#Relaciones
	virtual_expositions = db.relationship('Model_Virtual_Expositions', backref ='Users', lazy ='dynamic')
	multimedia = db.relationship('Model_Multimedia', backref ='Users', lazy ='dynamic')
	comments = db.relationship('Model_Comments', backref ='Users', lazy ='dynamic')
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


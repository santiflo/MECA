from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Multimedia import Model_Multimedia
from app.Models.Model_Comments import Model_Comments


class Model_Virtual_Expositions(db.Model):
	#Atributos
	__tablename__ = 'TBL_VIRTUAL_EXPOSITIONS'
	id = Column(Integer, primary_key = True)
	title = Column(String(100), nullable = False, default = 'blank name')
	description = Column(Text, default = 'blank description')
	creation_date = Column(DateTime, default = datetime.utcnow)
	number_views = Column(Integer, nullable = False, default = 0)
	picture = Column(Text, nullable = True, default = 'https://image.shutterstock.com/image-vector/green-school-chalkboard-frame-vector-600w-1478673725.jpg')
	audio = Column(Text, nullable = True, default = '') 
	background = Column(Text, nullable = True, default = '')
	bibliography = Column(Text, nullable = True, default = '')
	structure = Column(String(1), nullable = False, default = 0)
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USERS.id'), nullable = False)
	#Relaciones
	Multiemedia = db.relationship('Model_Multimedia', backref = 'Virtual_Expositions', lazy = 'dynamic')
	Comment = db.relationship('Model_Comments', backref = 'Virtual_Expositions', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))

class Schema_Virtual_Expositions(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Virtual_Expositions
        include_fk = True

    @post_load
    def make_Virtual_Expositions(self, data, **kwargs):
        return Model_Virtual_Expositions(**data)
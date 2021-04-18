from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.app import db, ma
from marshmallow import post_load
from app.Models.Model_Multimedia import Model_Multimedia


class Model_Documentaries(db.Model):
	#Atributos
	__tablename__ = 'TBL_DOCUMENTARIES'
	id = Column(Integer, primary_key = True)
	description = Column(Text, default = 'blank description')
	creation_date = Column(DateTime, default = datetime.utcnow)
	name = Column(String(100), nullable = False, default = 'blank name')
	#Foraneos
	userId = Column(Integer, ForeignKey('TBL_USERS.id'), nullable = False, unique = True)
	#Relaciones
	Multiemedia = db.relationship('Model_Multimedia', backref = 'Documentaries', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))

class Schema_Documentaries(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Documentaries
        include_fk = True

    @post_load
    def make_Documentaries(self, data, **kwargs):
        return Model_Documentaries(**data)
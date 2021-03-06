from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_File import Model_File


class Model_Documentaries(db.Model):
	#Atributos
	__tablename__ = 'TBL_DOCUMENTARIES'
	id = Column(Integer, primary_key = True)
	description = Column(Text, default = 'blank description')
	creation_date = Column(DateTime, default = datetime.utcnow)
	name = Column(String(100), nullable = False, default = 'blank name')
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USERS.id'), nullable = False, unique = True)
	category_id = Column(Integer, ForeignKey('TBL_CATEGORIES.id'))
	#Relaciones
	file = db.relationship('Model_File', backref = 'Documentaries', lazy = 'dynamic')
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
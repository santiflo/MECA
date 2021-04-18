from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from app.app import db, ma
from marshmallow import post_load

class Model_Multimedia(db.Model):
	#Atributos
	__tablename__ = 'TBL_MULTIMEDIA'
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable= False, unique = True)
	#Foraneos
	documental_id = Column(Integer, ForeignKey('TBL_DOCUMENTARIES.id'), nullable = False, unique = True)
	type_id = Column(Integer, ForeignKey('TBL_TYPE.id'), nullable = False)
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Multimedia(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Multimedia
        include_fk = True

    @post_load
    def make_Multimedia(self, data, **kwargs):
        return Model_Multimedia(**data)
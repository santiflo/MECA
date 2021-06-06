from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_File(db.Model):
	#Atributos
	__tablename__ = 'TBL_FILE'
	id = Column(Integer, primary_key = True)
	name = Column(String(255), nullable= False, unique = True)
	#Foraneos
	documental_id = Column(Integer, ForeignKey('TBL_DOCUMENTARIES.id'), nullable = False, unique = True)
	file_type_id = Column(Integer, ForeignKey('TBL_FILE_TYPES.id'), nullable = False)
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_File(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_File
        include_fk = True

    @post_load
    def make_File(self, data, **kwargs):
        return Model_File(**data)
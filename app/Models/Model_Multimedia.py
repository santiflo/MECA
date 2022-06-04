from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, Text
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_Multimedia(db.Model):
	#Atributos
	__tablename__ = 'TBL_MULTIMEDIA'
	id = Column(Integer, primary_key = True)
	path = Column(Text, nullable = True, unique = True)
	text = Column(Text, nullable = True)

	#Foraneos
	virtual_exposition_id = Column(Integer, ForeignKey('TBL_VIRTUAL_EXPOSITIONS.id'), nullable = False)
	user_id = Column(Integer, ForeignKey('TBL_USERS.id'), nullable = False)
	type_id = Column(Integer, ForeignKey('TBL_TYPES.id'), nullable = False) # Titulo = 1, Texto = 2, Video = 3, Audio = 4, Imagen = 5 y Subtitulo = 6
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
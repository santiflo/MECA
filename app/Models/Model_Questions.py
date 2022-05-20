from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Answers import Model_Answers

class Model_Questions(db.Model):
	#Atributos
	__tablename__ = 'TBL_QUESTIONS'
	id = Column(Integer, primary_key = True)
	name = Column(String(100), nullable = False, unique = True)
	description = Column(Text, nullable = False)
	date = Column(DateTime, nullable = False, default = datetime.utcnow)
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USERS.id'), nullable = False)
	#Relaciones
	answers = relationship('Model_Answers', backref = 'Questions', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Questions(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Questions
        include_fk = True

    @post_load
    def make_Questions(self, data, **kwargs):
        return Model_Questions(**data)
from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_Answers(db.Model):
	#Atributos
	__tablename__ = 'TBL_ANSWERS'
	id = Column(Integer, primary_key = True)
	answers = Column(Text, nullable = False)
	date = Column(DateTime, nullable = False, default = datetime.utcnow)
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USERS.id'), nullable = False)
	question_id = Column(Integer, ForeignKey('TBL_QUESTIONS.id'), nullable = False)
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Answers(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Answers
        include_fk = True

    @post_load
    def make_Answers(self, data, **kwargs):
        return Model_Answers(**data)
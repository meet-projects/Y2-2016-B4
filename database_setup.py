from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Person(Base):
	__tablename__ = 'person' 
	id = Column(Integer, primary_key=True)
	name = Column(String)  
	gender = Column(String)
	nationality = Column(String)

class Fact(Base): 
	__tablename__ = 'facts' 
	id = Column(Integer, primary_key=True)
	tribe = Column(String)
	statement = Column(String)
	correct_answer = Column(String)

class Answers(Base): 
	__tablename__ = 'answers' 
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship('Person')
	fact_id = Column(Integer, ForeignKey('facts.id'))
	fact = relationship('Fact')
	answer = Column(String)
	

#PLACE YOUR TABLE SETUP INFORMATION HERE
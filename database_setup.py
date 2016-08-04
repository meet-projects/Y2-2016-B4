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
	#f1 = Column(String)
	#f2 = Column(String)
	#f3 = Column(String)
	#f4 = Column(String)
	#f5 = Column(String)
	#a1 = Column(String)
	#a2 = Column(String)
	#a3 = Column(String)
	#a4 = Column(String)
	#a5 = Column(String)


class Answers(Base): 
	__tablename__ = 'answers' 
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer)
	fact_id = Column(Integer)
	answer = Column(String)
	# tribes = Column(String)
	# f1 = Column(String)
	# f2 = Column(String)
	# f3 = Column(String)
	# f4 = Column(String)
	# f5 = Column(String)
	# a1 = Column(String)
	# a2 = Column(String)
	# a3 = Column(String)
	# a4 = Column(String)
	# a5 = Column(String)


#PLACE YOUR TABLE SETUP INFORMATION HERE
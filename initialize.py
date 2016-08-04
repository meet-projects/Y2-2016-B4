from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.
fact1=Fact(tribe="Israeli",statement="they are here",correct_answer="True")
fact2=Fact(tribe="Israeli",statement="they cxzare here",correct_answer="True")
fact3=Fact(tribe="Israeli",statement="they arecccc here",correct_answer="True")
session.add(fact1)
session.add(fact2)
session.add(fact3)
session.commit()
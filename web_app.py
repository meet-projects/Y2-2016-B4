
from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



#YOUR WEB APP CODE GOES HERE



@app.route('/choose')
def choose():
	facts=session.query(Fact).all()
	tribes = set()
	for fact  in facts :
		tribes.add(fact.tribe)
	return render_template("choose.html" tribes= tribes)








if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, redirect, url_for, request
from flask import session as flask_session
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
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		name = request.form['name']
		person = session.query(Person).filter_by(name=name).first()
		if person is None:
			return redirect(url_for('login'))
		else:
			flask_session['name'] = name
			return redirect(url_for('choose'))

@app.route('/signup', methods=['POST'])
def signup():
	name=request.form['name']
	gender=request.form['gender']
	nationality=request.form['nationality']

	person = session.query(Person).filter_by(name=name).first()
	if person is None:
		new_person=Person(name=name, gender=gender, nationality=nationality)
		session.add(new_person)
		session.commit()
		flask_session['name'] = name
		return redirect(url_for('choose'))
	else:
		return redirect(url_for('signup'))



@app.route('/choose')
def choose():
	if 'name' in flask_session:
		person = session.query(Person).filter_by(name=flask_session['name']).first()
		facts=session.query(Fact).all()
		tribes = set()
		for fact  in facts :
			tribes.add(fact.tribe)
		return render_template("choose.html", tribes= tribes)

	else:
		return redirect(url_for('login'))





@app.route('/facts/<string:tribe_name>/', methods=['GET', 'POST'])
def facts(tribe_name):
	if 'name' in flask_session:
		person = session.query(Person).filter_by(name=flask_session['name']).first()
		
		facts = session.query(Fact).filter_by(tribe=tribe_name).all()
		if request.method == 'GET':
			return render_template('facts.html', facts=facts, tribe_name=tribe_name)
		else:
			for fact in facts:
				answer = request.form['tf' + str(fact.id)]
				new_answer_row = Answers(person_id=person.id,
										 fact_id=fact.id,
										 answer=answer)
				session.add(new_answer_row)
			session.commit()

			return redirect(url_for('answers', tribe_name = tribe_name ))
	else:
		return redirect(url_for('login'))
@app.route('/leaderboard', methods=['Get'])
def  leaderboard():
	people = session.query(Person).all()
	for person in people:
		answers_for_person =  session.query(Answers).filter_by(person_id=person.id)
		score = 0
		for answer in answers_for_person:
			if answer.answer == answer.fact.correct_answer:
				score += 1
		person.score = score
	return render_template('leaderboard.html', people = people)

@app.route('/answers/<string:tribe_name>')
def answers(tribe_name):
    if 'name' in flask_session:
        person = session.query(Person).filter_by(name=flask_session['name']).first()
        
        answers_for_person = session.query(Answers).filter_by(person_id=person.id).all()
        answers=[answer for answer in answers_for_person if answer.fact.tribe==tribe_name]    

        return render_template('answers.html', answers=answers)
    else:
        return redirect(url_for('login'))





app.secret_key = '234xz0v9z09d8f0912395rt0'
if __name__ == '__main__':
    app.run(debug=True)

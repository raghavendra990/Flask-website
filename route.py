from flask import Flask, url_for , request, render_template;
from app import app
import redis;

	#r =  redis.StrictRedis();
	#r = reis.StrictRedis(host= 'localhost',port=6379, db=0);
r = redis.StrictRedis(host= 'localhost',port=6379, db=0, charset= "utf-8", decode_responses =True );

@app.route('/')
def hello():
	
	#r =  redis.StrictRedis();
	#r = reis.StrictRedis(host= 'localhost',port=6379, db=0);

	createLink = "<a href= '"+ url_for('create') + "'>Create a question</a>"
	return """<html>
					<head>
						<title>Hello,world!</title>
					</head>
					<body>
						"""+ createLink+"""
					</body>
				</html>""";

@app.route('/create', methods= ['GET', 'POST'])
def create():
	if request.method == 'GET':
		# sedn the user the form
		return render_template('createQuestion.html');
	elif request.method =='POST':
		# read from data and save it 
		title = request.form['title'];
		question = request.form['question'];
		answer = request.form['answer'];

		# store dat in dat store
		# # please code here
		r.set(title+':question',question)
		r.set(title+':answer', answer)




		return render_template('createdQuestion.html', question = question);

	else:
		return "<h2>invalid request</h2>"

@app.route('/question/<title>', methods = ['GET', 'POST'])
def question(title):
	if request.method == 'GET':
		# send the user the form
		question  = r.get(title+':question')
		# read question from data here
		return render_template('answerQuestion.html', question  = question);
	elif  request.method == 'POST':
		# User attemted to answer . chech if they are correct

		submittedAnswer = request.form['submittedAnswer']

		

		

		# Read answer form dara store
		# add code
		answer =  r.get(title+':answer');

		if submittedAnswer == answer:
			return render_template('correct.html')
		else:
			return render_template('incorrect.html', submittedAnswer = submittedAnswer , answer =  answer);
	else:
		return '<h2> Invalid request</h2>';





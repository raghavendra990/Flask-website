"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#code start from here

@app.route('/')
def hello():
	return """<html>
					<head>
						<title>Hello,world!</title>
					</head>
					<body>
						<h1>Hello, Susan!</h1>
					</body>
				</html>""";
@app.route('/create')
def create():
	return "<h1>this is the create page !</h1>"
	

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

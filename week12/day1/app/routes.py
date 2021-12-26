import json

import flask

from app import app
from app.forms import Register


@app.route('/', methods=['GET'])
def index():
	return flask.render_template('index.html', new_color=False)


@app.route('/blank/<color>', methods=['GET'])
def blank(color):
	return flask.render_template('blank.html', color=color)


@app.route('/users/<name>', methods=['POST'])
def add_blank(name):
	users = []
	with open('../examplle.json', 'r') as f:
		users = json.load(f)

	users.append({'name': name})

	with open('../examplle.json', 'w') as f:
		json.dump(users, f, indent=2)


@app.route('/myform', methods=("GET", "POST"))
def myform():

	registerForm = Register()

	if registerForm.validate_on_submit(): # Check if the form has been filled
		username = registerForm.username.data # Get
		password = registerForm.password.data #   The
		bio = registerForm.bio.data      #     Data

		print("Here is what I got from the form:")
		print("username:", username)
		print("password:", password)
		print("bio:", bio)
		# Do something with the data

		return flask.redirect('/')
	return flask.render_template("register.html", form=registerForm)

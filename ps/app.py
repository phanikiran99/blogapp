# -*- coding: utf-8 -*-

import logging   # for loggin information.

# import all required flask functions and modules

from flask import Flask 
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user
from flask_login import login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy

# 
# from flask.ext.login import LoginManager, current_user
# from flask.ext.login import login_user, login_required, logout_user
# from flask.ext.sqlalchemy import SQLAlchemy


# import application related methods,configs,forms etc
from ps import config,filters
from ps.forms import LoginForm,signupForm, SearchForm
from ps.models import User,Base

# Import Watson and other APi related 

import requests


# Create Application instance
app = Flask(__name__)
app.config.from_object(config)

# Load Database Objects
db = SQLAlchemy(app)
db.Model = Base
flage1 = 1

results_title = []
results_content = []

# login manager 
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please login to Access ps Dashboard, Contact psRO incase you dont have an id or any password issues"

@login_manager.user_loader
def load_user(user_id):
	return db.session.query(User).get(user_id)

# Load custom Jinja filters from the `filters` module.
filters.init_app(app)

# loggin information when debug is set to false
if not app.debug:
	app.logger.setHandler(logging.StreamHandler()) #log to stderr
	app.logger.setLevel(logging.INFO)


@app.errorhandler(404)
def error_not_found(err):
	return render_template('error/not_found.html'), 404

@app.route('/')
def index_page():
	return render_template('index.html')

@app.route('/searchdoc/',methods=['GET','POST'])
@login_required
def search_doc():
	loading=False
	form = SearchForm(request.form)
	results_title = []
	results_content = []
	if request.method == 'POST':
		loading=True
		searchkey = form.searchKey.data.strip()
# 		search = 1
		error = 'Not Found'
# 		srchTerm = ""
		if not searchkey:
			return render_template('search.html',form=form,error="Enter some thing to search",results_content=results_content,results_title=results_title,loading=True)
		else:
			results_title = ['results_title'+ str(i) for i in range(20) if i%2 == 0]
			results_content = ['results_content'+ str(i) for i in range(10)]
			return render_template('search.html',form=form,results_content=results_content,results_title=results_title,loading=False)
	return render_template('search.html',form=form,results_content=results_content,results_title=results_title,loading=True)

@app.route('/welcome/')
@login_required
def welcome_page():
	return render_template('welcome.html')

@app.route('/login/',methods=['GET','POST'])
def login():
	# print current_user
	if current_user.is_authenticated():
		return redirect(url_for('welcome_page'))
	form = LoginForm(request.form)
	error = None
	if request.method == 'POST' and form.validate():
		email = form.username.data.lower().strip()
		password = form.password.data.lower().strip()
		user, authenticated = \
			User.authenticate(db.session.query, email, password)
		if authenticated:
			login_user(user)
			return redirect(url_for('welcome_page'))
		else:
			error = "Invalid Credentials, Please try again"
	return render_template('user/login.html',form=form,error=error)

@app.route('/logout/')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/signup/',methods=['GET','POST'])
def signup():
	if current_user.is_authenticated():
		return redirect(url_for('welcome_page'))
	form = signupForm(request.form)
	error = None
	if request.method == 'POST' and form.validate():
		email = form.username.data.lower().strip()
		password = form.password.data.lower().strip()
		user = User(email=form.username.data.lower().strip(), password=form.password.data.lower().strip())
		db.session.add(user)
		db.session.commit()
		user, authenticated = \
			User.authenticate(db.session.query, email, password)
		if authenticated:
			login_user(user)
			return redirect(url_for('welcome_page'))
		else:
			error = "Something Wrong Happened!! Please Contact us"
			return render_template('user/signup.html',form=form,error=error)
	return render_template('user/signup.html',form=form,error=error)		
'''			
@app.route('/searchdoc/',methods=['GET','POST'])
def searchdoc():
	if current_user.is_authenticated():
		return render_template('error/not_found.html')
	else:
		return redirect(url_for('login'))

	if authenticated:
		login_user(user)
		return render_template('error/not_found.html')
	else:
		error = "Something Wrong Happened!! Please Contact us"
		return render_template('user/signup.html',form=form,error=error)
    return str(2) # render_template('index.html')
'''
@app.route('/searchwiki/',methods=['GET','POST'])
def searchwiki():
		return render_template('not_found.html')

@app.route('/searchiAssi/',methods=['GET','POST'])	
def searchiAssi():
		return render_template('not_found.html')

@app.route('/langconv/',methods=['GET','POST'])	
def langconv():
		return render_template('not_found.html')
	
@app.route('/testplanner/',methods=['GET','POST'])		
def testplanner():
		return render_template('not_found.html')

@app.route('/reqanalysis/',methods=['GET','POST'])
def reqanalysis():
		return render_template('not_found.html')
""" forms to render HTML pages """ 
from wtforms import Form, TextField, PasswordField
from wtforms import TextAreaField, TextField
from wtforms.validators import Length, required
from wtforms.fields.core import StringField

class LoginForm(Form):
	"""Render HTML input for user login form"""
	username = TextField('Username', [required()])
	password = PasswordField('Password', [required()])

class signupForm(Form):
	uname = TextField('uName',[required()])
	username = TextField('Username',[required()])
	password = PasswordField('Password',[required()])
	
class SearchForm(Form):
	searchKey = TextField('searchKey')
# 	results_title = StringField('results_title')
# 	results_content = StringField('results_content')
# 	
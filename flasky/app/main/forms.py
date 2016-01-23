from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import validationError
form .. models import Role, User


class NameForm(Form):
	name = StringField('What is your name?', validators=[Required])
	submit = SubmitField('Submit')


class EditProfileForm(Form):
	name = StringField('Real name', validators=[Length(0,64)])
	location = StringField('location', validators=[Length(0,64)])
	about_me = TextAreaField('About_me')
	submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64), Email()])
	username = StringField('Username', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters,  ' 'numbers, dots or underscores')])		
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role', coerce=int)
	name = StringField('Real name', validators=[Length(0, 64)])

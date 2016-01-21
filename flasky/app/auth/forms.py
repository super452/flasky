from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForms(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('keep me logged in')
	submit = SubmitField('Log in')

class RegistrationForms(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	username = StringField('username',validators=[Required(),Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ''numbers,dots or underscores')])
	password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Register')
	
	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')
			
	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

class ChangePasswordForm(Form):
	old_password = PasswordField('old_password', validators=[Required])
	password = PasswordField('New password', validators=[Required(), EqualTo('password2', message='Password must match')])
	password2 = PasswordField('Confirm New password', validators=[Required()])
	submit = SubmitField('Update Password')

class PasswordResetRequestForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	submit = SubmitField('Reset Password')

class PasswordResetForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('New Password', validators=[Required(), EqualTo('password2', message='Passwords nust match')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Reset Password')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first() is None:
			raise ValidationError('Unknown email address.')
	
class ChangeEmailForm(Form):
	email = StringField('New Email', validators=[Required(), Length(1, 64),
                                                Email()])
	password = PasswordField('Password', validators=[Required()])
 	submit = SubmitField('Update Email Address')

	def validate_email(self, field):
       		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import EqualTo, DataRequired, Email

class RegisterUser(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    email = EmailField(label='Email:', validators=[Email()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Register')

class LoginUser(FlaskForm):
    email = EmailField(label='Email:', validators=[Email()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    login = SubmitField(label='Sign In')

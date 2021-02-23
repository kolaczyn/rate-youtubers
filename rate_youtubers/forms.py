from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=3, max=32)])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[InputRequired(), EqualTo('password')])

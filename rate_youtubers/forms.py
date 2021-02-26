from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
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


class YoutuberForm(FlaskForm):
    id = StringField('ID', validators=[InputRequired(), Length(min=24, max=24)])
    name = StringField('Name', validators=[InputRequired(), Length(max=20)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(max=1000)])

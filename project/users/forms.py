from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=2, max=64)])

    surname = StringField(
        'Surname',
        validators=[DataRequired(), Length(min=2, max=64)])

    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])

    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)])

    confirm = PasswordField(
        'Repeat password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])

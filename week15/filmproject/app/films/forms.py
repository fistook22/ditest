from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField
from wtforms.validators import data_required


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[data_required()])
    release_date = DateField('Release', validators=[data_required()])
    available_in_countries = StringField('Available')
    category = StringField('Category')
    director = StringField('Director')
    submit = SubmitField('Add a New Film')


class AddDirectorForm(FlaskForm):
    first_name = StringField('Name', validators=[data_required()])
    last_name = StringField('Lname', validators=[data_required()])
    submit = SubmitField('Add a New Director')


class SignUp(FlaskForm):
    username = StringField('Username', validators=[data_required()])
    password1 = PasswordField('Password', validators=[data_required()])
    password2 = PasswordField('Confirm', validators=[data_required()])
    submit = SubmitField('Register')


class Login(FlaskForm):
    username = StringField('Username', validators=[data_required()])
    password = PasswordField('Password', validators=[data_required()])
    submit = SubmitField('Login')
